#!/usr/bin/env python3
"""Adapter: sarvam_api (Level-3 paid API, Sarvam Document AI / Sarvam Vision).

Facts verified from official docs 2026-09-13 (docs.sarvam.ai):
- POST https://api.sarvam.ai/doc-ai/v1/job/digitise
- header: `api-subscription-key: <SARVAM_API_KEY>` (Bearer also accepted)
- multipart form: file=<page.png>, language=<te-IN|ta-IN|kn-IN|ml-IN>, output_format=<md|html|json>
- model: Sarvam Vision 1.5 (model id `sarvam-vision`, 3B VLM, 23 langs)
- async job: poll GET /doc-ai/v1/job/<id>/status, output via /download-url (ZIP)
- pricing: Rs.0.5/page (Document Digitization API); Rs.100 free credits on signup
- limits: 10 pages/job, 200MB/file, 10 req/min on doc-ai
No key configured => DRY-RUN (zero network, zero cost). Key arrives => one
env var, real calls, same harness.

Round-1 hardening (2026-09-30, audit findings A1-a..d):
- language comes from pages_manifest.json by page_id (render stem); an unknown
  page RAISES instead of silently defaulting to te-IN. mixed_book_page is
  recorded in last_meta so scoring can stratify it (L8: tag = ID label).
- output parsing collects `text` fields only; an unrecognised payload returns
  "" with last_meta["error"] set and the raw payload kept in last_raw —
  never str(result) scored as OCR text.
- every HTTP request is throttled to <= 10 req/min; polling has a hard timeout.
- one page per job (simplest correct unit for a 4-page gate; cost is per page).
Wire details marked TODO-VERIFY are confirmed or corrected at the 4-page gate.
"""
from __future__ import annotations

import io
import json
import os
import time
import unicodedata
import zipfile
from pathlib import Path
from typing import Any, Optional

from . import BaseEngine, register

BASE = "https://api.sarvam.ai/doc-ai/v1"
ENDPOINT = f"{BASE}/job/digitise"
KEY_ENV = "SARVAM_API_KEY"
POLL_S = 5
POLL_TIMEOUT_S = 600
MIN_REQ_INTERVAL_S = 6.0  # 10 req/min doc-ai limit
PRICE_INR_PER_PAGE = 0.5  # docs 2026-09-13; re-verify at gate
DRY_RUN_TEXT = "<dry-run: sarvam_api not configured — set SARVAM_API_KEY>"
LANG_MAP = {"te": "te-IN", "ta": "ta-IN", "kn": "kn-IN", "ml": "ml-IN"}
MANIFEST = Path(__file__).resolve().parents[1] / "pages_manifest.json"
TEXT_KEYS = ("text",)


def _load_manifest() -> dict[str, dict]:
    if not MANIFEST.exists():
        return {}
    return {m["page_id"]: m for m in json.loads(MANIFEST.read_text(encoding="utf-8"))}


def collect_text(obj: Any) -> list[str]:
    """Depth-first, document-order list of string values under `text` keys."""
    out: list[str] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in TEXT_KEYS and isinstance(v, str):
                out.append(v)
            else:
                out.extend(collect_text(v))
    elif isinstance(obj, list):
        for v in obj:
            out.extend(collect_text(v))
    return out


class SarvamBatchAPI(BaseEngine):
    name = "sarvam_api"
    version = "sarvam-vision-1.5 (doc-ai v1)"

    def __init__(self):
        self.key = os.environ.get(KEY_ENV)
        self.dry_run = not self.key
        self._manifest = _load_manifest()
        self._last_req = 0.0
        self.last_meta: dict = {}
        self.last_raw: Optional[bytes] = None

    def language_for(self, png_path: Path) -> str:
        """Sarvam language code from the manifest (lang_hint overrides)."""
        if self.lang_hint:
            lang = self.lang_hint
        else:
            page = self._manifest.get(Path(png_path).stem)
            if page is None:
                raise ValueError(f"{Path(png_path).stem}: not in pages_manifest.json — "
                                 "refusing to guess a language")
            lang = page["lang"]
        if lang not in LANG_MAP:
            raise ValueError(f"unsupported lang {lang!r}")
        return LANG_MAP[lang]

    def _throttle(self) -> None:
        wait = MIN_REQ_INTERVAL_S - (time.monotonic() - self._last_req)
        if wait > 0:
            time.sleep(wait)
        self._last_req = time.monotonic()

    def run(self, png_path: Path) -> str:
        png_path = Path(png_path)
        page = self._manifest.get(png_path.stem, {})
        self.last_meta = {"page_id": png_path.stem,
                          "mixed_book_page": page.get("mixed_book_page"),
                          "error": None}
        self.last_raw = None
        if self.dry_run:
            return DRY_RUN_TEXT
        lang = self.language_for(png_path)
        self.last_meta["lang_param"] = lang

        import requests
        headers = {"api-subscription-key": self.key}

        self._throttle()
        with open(png_path, "rb") as f:
            resp = requests.post(ENDPOINT, headers=headers, timeout=60,
                                 files={"file": (png_path.name, f, "image/png")},
                                 data={"language": lang, "output_format": "json"})
        resp.raise_for_status()
        job_id = resp.json()["job_id"]  # TODO-VERIFY at gate
        self.last_meta["job_id"] = job_id

        status_url = f"{BASE}/job/{job_id}/status"
        deadline = time.monotonic() + POLL_TIMEOUT_S
        while True:
            time.sleep(POLL_S)
            self._throttle()
            resp = requests.get(status_url, headers=headers, timeout=30)
            resp.raise_for_status()
            status = resp.json()
            if status.get("status") == "completed":
                break
            if status.get("status") == "failed":
                raise RuntimeError(f"Sarvam job {job_id} failed: {status}")
            if time.monotonic() > deadline:
                raise TimeoutError(f"Sarvam job {job_id} not done after {POLL_TIMEOUT_S}s")

        url = status.get("download_url")
        if not url:  # TODO-VERIFY at gate: dedicated download-url endpoint
            self._throttle()
            r = requests.get(f"{BASE}/job/{job_id}/download-url", headers=headers, timeout=30)
            r.raise_for_status()
            url = r.json().get("download_url") or r.json().get("url")
        self._throttle()
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        self.last_raw = resp.content
        return self._extract_zip(resp.content)

    def _extract_zip(self, blob: bytes) -> str:
        parts: list[str] = []
        with zipfile.ZipFile(io.BytesIO(blob)) as z:
            for name in sorted(z.namelist()):
                if name.endswith(".json"):
                    with z.open(name) as f:
                        parts.extend(collect_text(json.load(f)))
        if not parts:
            self.last_meta["error"] = "unparsed_output"  # raw kept in last_raw
            return ""
        return unicodedata.normalize("NFC", "\n".join(p for p in parts if p.strip()))


register(SarvamBatchAPI())
