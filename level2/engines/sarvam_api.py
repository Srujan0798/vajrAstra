#!/usr/bin/env python3
"""Adapter: sarvam_api (Level-3 paid API, Sarvam Document AI / Sarvam Vision).

Facts verified from official docs 2026-09-13 (docs.sarvam.ai):
- POST https://api.sarvam.ai/doc-ai/v1/job/digitise
- header: `api-subscription-key: <SARVAM_API_KEY>`
- multipart form: file=<page.png>, language=<te-IN|ta-IN|kn-IN|ml-IN>,
  output_format=<md|html|json>; language is OMITTED for mixed_book_page pages
- model: Sarvam Vision 1.5 (model id `sarvam-vision`, 3B VLM, 23 langs)
- async job: poll GET /doc-ai/v1/job/<id>/status, output via /download-url (ZIP)
- pricing: Rs.0.5/page (Document Digitization API); Rs.100 free credits
- limits: 10 pages/job, 200MB/file, 10 req/min on doc-ai
No key configured => DRY-RUN (zero network, zero cost).
"""
from __future__ import annotations

import io
import json
import os
import time
import zipfile
from pathlib import Path
from typing import Any, Optional

from . import BaseEngine, register

ENDPOINT = "https://api.sarvam.ai/doc-ai/v1/job/digitise"
KEY_ENV = "SARVAM_API_KEY"
POLL_S = 5
POLL_TIMEOUT_S = 180
REQ_INTERVAL_S = 6.0
MAX_PAGES_PER_JOB = 10
DRY_RUN_TEXT = "<dry-run: sarvam_api not configured — set SARVAM_API_KEY>"
LANG_MAP = {"te": "te-IN", "ta": "ta-IN", "kn": "kn-IN", "ml": "ml-IN"}

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / "level2" / "pages_manifest.json"
RAW_DIR = ROOT / "out_level3" / "raw"

_MANIFEST: Optional[dict] = None
_last_submit = 0.0


def _manifest() -> dict:
    global _MANIFEST
    if _MANIFEST is None:
        with open(MANIFEST_PATH, encoding="utf-8") as f:
            _MANIFEST = {rec["page_id"]: rec for rec in json.load(f)}
    return _MANIFEST


def _throttle() -> None:
    global _last_submit
    wait = REQ_INTERVAL_S - (time.monotonic() - _last_submit)
    if wait > 0:
        time.sleep(wait)
    _last_submit = time.monotonic()


class SarvamAPI(BaseEngine):
    name = "sarvam_api"
    version = "sarvam-vision-1.5 (doc-ai v1)"

    def __init__(self):
        self.key = os.environ.get(KEY_ENV)
        self.dry_run = not self.key
        self.last_meta: dict = {}
        self.last_error: Optional[str] = None

    def lang_param(self, png_path: Path) -> tuple[Optional[str], dict]:
        """(language tag or None, manifest record). Never defaults. Raises on unknown page."""
        pid = Path(png_path).stem
        rec = _manifest().get(pid)
        if rec is None:
            raise KeyError(f"unknown page_id (not in pages_manifest.json): {pid}")
        if rec.get("mixed_book_page"):
            return None, rec
        return LANG_MAP.get(rec["lang"]), rec

    def run(self, png_path: Path) -> str:
        self.last_error = None
        self.last_meta = {"page_id": Path(png_path).stem}
        if self.dry_run:
            return DRY_RUN_TEXT

        import requests

        lang, rec = self.lang_param(png_path)
        self.last_meta.update({
            "lang_param": lang,
            "mixed_book_page": bool(rec.get("mixed_book_page")),
        })

        _throttle()
        with open(png_path, "rb") as f:
            files = {"file": (Path(png_path).name, f, "image/png")}
            data: dict = {"output_format": "json"}
            if lang:
                data["language"] = lang
            headers = {"api-subscription-key": self.key}
            resp = requests.post(ENDPOINT, files=files, data=data, headers=headers, timeout=30)
            resp.raise_for_status()
            job_id = resp.json()["job_id"]
        self.last_meta["job_id"] = job_id

        status_url = f"https://api.sarvam.ai/doc-ai/v1/job/{job_id}/status"
        deadline = time.monotonic() + POLL_TIMEOUT_S
        while True:
            if time.monotonic() > deadline:
                raise TimeoutError(f"Sarvam job {job_id} exceeded {POLL_TIMEOUT_S}s")
            time.sleep(POLL_S)
            resp = requests.get(status_url, headers=headers, timeout=10)
            resp.raise_for_status()
            body = resp.json()
            status = body["status"]
            if status == "completed":
                break
            if status == "failed":
                raise RuntimeError(f"Sarvam job failed: {body}")

        resp = requests.get(body["download_url"], timeout=30)
        resp.raise_for_status()

        with zipfile.ZipFile(io.BytesIO(resp.content)) as z:
            for member in z.namelist():
                if member.endswith(".json"):
                    with z.open(member) as f:
                        result = json.load(f)
                    text = self._extract_text(result)
                    if self.last_error is not None:
                        RAW_DIR.mkdir(parents=True, exist_ok=True)
                        raw_path = RAW_DIR / f"{Path(png_path).stem}_{job_id}.json"
                        with open(raw_path, "w", encoding="utf-8") as f:
                            json.dump(result, f, ensure_ascii=False, indent=2)
                        self.last_meta["raw_saved"] = str(raw_path)
                        return ""
                    return text
        self.last_error = "empty_zip"
        return ""

    def _extract_text(self, node: Any) -> str:
        """Collect only `text` fields (recursive). Unknown shape => "" + last_error."""
        parts: list[str] = []

        def walk(n: Any) -> None:
            if isinstance(n, dict):
                for k, v in n.items():
                    if k == "text" and isinstance(v, str):
                        parts.append(v)
                    else:
                        walk(v)
            elif isinstance(n, list):
                for v in n:
                    walk(v)

        walk(node)
        if not parts:
            self.last_error = "unrecognized_payload"
            return ""
        return "\n".join(parts)


register(SarvamAPI())
