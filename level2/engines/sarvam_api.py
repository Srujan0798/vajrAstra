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

class SarvamBatchAPI:
    name = "sarvam_batch_api"
    version = "sarvam-vision-1.5 (doc-ai v1)"
    
    def __init__(self):
        self.key = os.environ.get(KEY_ENV)
        self.dry_run = not self.key
    
    def run(self, png_path: Path) -> str:
        if self.dry_run:
            return "<dry-run: sarvam_batch_api not configured — set SARVAM_API_KEY>"
        
        import requests
        
        # Submit job
        with open(png_path, 'rb') as f:
            files = {'file': (png_path.name, f, 'image/png')}
            data = {'language': self._lang_from_path(png_path), 'output_format': 'json'}
            headers = {'api-subscription-key': self.key}
            
            resp = requests.post(ENDPOINT, files=files, data=data, headers=headers, timeout=30)
            resp.raise_for_status()
            job_id = resp.json()['job_id']
        
        # Poll for completion
        status_url = f"https://api.sarvam.ai/doc-ai/v1/job/{job_id}/status"
        headers = {'api-subscription-key': self.key}
        
        while True:
            time.sleep(POLL_S)
            resp = requests.get(status_url, headers=headers, timeout=10)
            resp.raise_for_status()
            status = resp.json()['status']
            if status == 'completed':
                break
            if status == 'failed':
                raise RuntimeError(f"Sarvam job failed: {resp.json()}")
        
        # Download result
        download_url = resp.json()['download_url']
        resp = requests.get(download_url, timeout=30)
        resp.raise_for_status()
        
        # Extract text from ZIP
        with zipfile.ZipFile(io.BytesIO(resp.content)) as z:
            for name in z.namelist():
                if name.endswith('.json'):
                    with z.open(name) as f:
                        result = json.load(f)
                        return self._extract_text(result)
        return ""
    
    def _lang_from_path(self, path: Path) -> str:
        lang_map = {'te': 'te-IN', 'ta': 'ta-IN', 'kn': 'kn-IN', 'ml': 'ml-IN'}
        return lang_map.get(path.stem[:2], 'te-IN')
    
    def _extract_text(self, result: dict) -> str:
        # Sarvam returns structured JSON; extract text fields
        if isinstance(result, dict) and 'text' in result:
            return result['text']
        return str(result)

# Register
from . import register, BaseEngine
register(SarvamBatchAPI())
