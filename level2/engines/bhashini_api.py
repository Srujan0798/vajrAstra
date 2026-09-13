"""Adapter: bhashini_api (Level-3 paid API, Bhashini/ULCA OCR lane). TODO-VERIFY.

Bhashini public surfaces (bhashini.gov.in, ulca.bhashini.gov.in) are
JS-only apps; no fetchable official OCR API reference exists. Verified
facts from bhashini.gov.in site bundle (2026-09-13): product surfaces are
Lekhaanuvaad (document translation+digitization, lekh.bhashini.gov.in) and
Anuvaad pipeline (anuvaad-backend.bhashini.co.in/v1/pipeline); OCR models for
te/ta/kn/ml exist (anuvaad-ocr-model repo). NO public OCR REST endpoint,
auth shape, or rate card could be verified => every wire fact is
TODO-VERIFY at kickoff. No key configured => DRY-RUN. If, at kickoff, ULCA
turns out to have no OCR-as-API for our langs, main agent deletes this
adapter and the sarvam lane covers Level 3 alone.
"""
from __future__ import annotations

import os
import unicodedata
from pathlib import Path
from typing import Optional

from . import BaseEngine, register

KEY_ENV = "BHASHINI_API_KEY"
ENDPOINT = ""  # TODO-VERIFY: ULCA/Anuvaad OCR endpoint (none publicly documented)
DRY_RUN_TEXT = "<dry-run: bhashini_api not configured — set BHASHINI_API_KEY>"


class BhashiniAPI(BaseEngine):
    name = "bhashini_api"
    version = "bhashini ulca-ocr (endpoint+price TODO-VERIFY)"
    lang_hint: Optional[str] = None

    def run(self, png_path: Path) -> str:
        if not os.environ.get(KEY_ENV):
            return DRY_RUN_TEXT
        if not ENDPOINT:
            raise NotImplementedError(
                "bhashini_api: OCR endpoint TODO-VERIFY — fill ENDPOINT from "
                "official Bhashini/ULCA docs at kickoff"
            )
        raise NotImplementedError(
            "bhashini_api: request/response shape TODO-VERIFY — implement after "
            "official ULCA docs are confirmed (see LEVEL3_KICKOFF.md §2.2)"
        )


register(BhashiniAPI())
