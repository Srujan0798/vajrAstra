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
"""
from __future__ import annotations

import io
import json
import os
import time
import unicodedata
import zipfile
from pathlib import Path
from typing import Optional
from uuid import uuid4

from . import BaseEngine, register

ENDPOINT = "https://api.sarvam.ai/doc-ai/v1/job/digitise"
KEY_ENV = "SARVAM_API_KEY"
POLL_S = 5
POLL_MAX = 60
_LANG = {"te": "te-IN", "ta": "ta-IN", "kn": "kn-IN", "ml": "ml-IN"}
DRY_RUN_TEXT = "<dry-run: sarvam_api not configured — set SARVAM_API_KEY>"


class SarvamAPI(BaseEngine):
    name = "sarvam_api"
    version = "sarvam-vision 1.5 (Document AI digitise, ₹0.5/page)"
    lang_hint: Optional[str] = None

    def _post(self, png_bytes: bytes, lang_hint: Optional[str]) -> dict:
        import urllib.request

        boundary = "vajraAstra-l3-" + uuid4().hex
        lang = _LANG.get(lang_hint or "te", "te-IN")
        parts = [
            ('file', "page.png", "image/png", png_bytes),
            ("language", None, None, lang.encode()),
            ("output_format", None, None, b"md"),
        ]
        body = io.BytesIO()
        for name, filename, ctype, data in parts:
            body.write(f"--{boundary}\r\n".encode())
            if filename:
                body.write(
                    f'Content-Disposition: form-data; name="{name}"; '
                    f'filename="{filename}"\r\nContent-Type: {ctype}\r\n\r\n'.encode()
                )
            else:
                body.write(
                    f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode()
                )
            body.write(data)
            body.write(b"\r\n")
        body.write(f"--{boundary}--\r\n".encode())
        req = urllib.request.Request(
            ENDPOINT,
            data=body.getvalue(),
            headers={
                "api-subscription-key": os.environ[KEY_ENV],
                "Content-Type": f"multipart/form-data; boundary={boundary}",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode("utf-8"))

    def _get(self, url: str) -> dict:
        import urllib.request

        req = urllib.request.Request(
            url, headers={"api-subscription-key": os.environ[KEY_ENV]}
        )
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode("utf-8"))

    def _poll(self, job_id: str) -> dict:
        st = {"status": "pending"}
        for _ in range(POLL_MAX):
            st = self._get(f"{ENDPOINT}/{job_id}/status")
            if str(st.get("status", "")).lower() in {
                "completed",
                "partially_completed",
                "failed",
                "rejected",
            }:
                return st
            time.sleep(POLL_S)
        raise TimeoutError(f"sarvam_api job {job_id} not terminal after {POLL_MAX} polls")

    def _download_md(self, job_id: str) -> str:
        dl = self._get(f"{ENDPOINT}/{job_id}/download-url")
        import urllib.request

        with urllib.request.urlopen(dl["url"], timeout=300) as r:
            blob = r.read()
        with zipfile.ZipFile(io.BytesIO(blob)) as zf:
            names = sorted(n for n in zf.namelist() if n.endswith((".md", ".txt")))
            if not names:
                names = sorted(n for n in zf.namelist() if not n.endswith(".json"))
            if not names:
                raise ValueError("sarvam_api download ZIP has no text file")
            return zf.read(names[0]).decode("utf-8")

    def run(self, png_path: Path) -> str:
        key = os.environ.get(KEY_ENV)
        if not key:
            return DRY_RUN_TEXT
        job = self._post(Path(png_path).read_bytes(), self.lang_hint)
        st = self._poll(job["job_id"])
        status = str(st.get("status", "")).lower()
        if status in ("failed", "rejected"):
            raise RuntimeError(f"sarvam_api job {job.get('job_id')}: {status}")
        if status != "completed" and st.get("usage", {}).get("pages_failed", 0):
            raise RuntimeError(f"sarvam_api partial failure: {st.get('usage')}")
        text = self._download_md(job["job_id"])
        return unicodedata.normalize("NFC", text)


register(SarvamAPI())
