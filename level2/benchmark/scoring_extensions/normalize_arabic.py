"""normalize_arabic — opt-in Arabic/Perso-Arabic normalization for scoring (proto-100 B-02).

Up to 3-8 pts of the Kashmiri "failure" may be a scoring artifact, not a recognition
failure (proto-100 B-02, citing R2 §A5, R7 N4, UrduMMLU pipeline).

This is a NEW module. The locked `level2/benchmark/pipeline/metrics.py` is NOT
modified. Call `normalize_arabic(text)` explicitly — the default scorer never
applies this normalization.

Maps presentation forms, digit variants, punctuation, and bidi marks so two
visually identical Arabic strings score as identical.

Sarvam-bench numbers always use Sarvam's unchanged `metrics.py` (per proto-100
B-02). For Bodhan eval, use this module and report BOTH raw and normalized CER.
"""

from __future__ import annotations

import unicodedata

YEH_MAP = {
    "\u064A": "\u06CC",  # ARABIC LETTER YEH → ARABIC LETTER FARSI YEH
    "\u0626": "\u06CC",  # ARABIC LETTER YEH WITH HAMZA ABOVE → FARSI YEH
    "\u0649": "\u06CC",  # ARABIC LETTER ALEF MAKSURA → FARSI YEH
}

KAF_MAP = {
    "\u0643": "\u06A9",  # ARABIC LETTER KAF → ARABIC LETTER KEHEH
}

HEH_MAP = {
    "\u0629": "\u0647",  # ARABIC LETTER TEH MARBUTA → ARABIC LETTER HEH
}

PUNCT_MAP = {
    "\u060C": ",",  # ARABIC COMMA
    "\u061B": ";",  # ARABIC SEMICOLON
    "\u061F": "?",  # ARABIC QUESTION MARK
    "\u06D4": ".",  # ARABIC FULL STOP
    "\u066A": "%",  # ARABIC PERCENT SIGN
    "\u066B": ",",  # ARABIC DECIMAL SEPARATOR
    "\u066C": ",",  # ARABIC THOUSANDS SEPARATOR
}

BIDI_ISOLATES = "\u2066\u2067\u2068\u2069"  # LRI/RLI/FSI/PDI

PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹"  # U+06F0..U+06F9
ARABIC_INDIC_DIGITS = "٠١٢٣٤٥٦٧٨٩"  # U+0660..U+0669


def unify_chars(text: str) -> str:
    out = []
    for c in text:
        out.append(YEH_MAP.get(c, KAF_MAP.get(c, HEH_MAP.get(c, c))))
    return "".join(out)


def unify_digits(text: str, direction: str = "persian_to_arabic_indic") -> str:
    if direction == "persian_to_arabic_indic":
        src, dst = PERSIAN_DIGITS, ARABIC_INDIC_DIGITS
    elif direction == "arabic_indic_to_persian":
        src, dst = ARABIC_INDIC_DIGITS, PERSIAN_DIGITS
    else:
        return text
    out = []
    for c in text:
        idx = src.find(c)
        out.append(dst[idx] if idx >= 0 else c)
    return "".join(out)


def map_punctuation(text: str) -> str:
    out = []
    for c in text:
        out.append(PUNCT_MAP.get(c, c))
    return "".join(out)


def strip_bidi_isolates(text: str) -> str:
    return "".join(c for c in text if c not in BIDI_ISOLATES)


def normalize_arabic(text: str, digit_direction: str = "persian_to_arabic_indic") -> str:
    """Full Arabic normalization pipeline (opt-in). Run BEFORE the default scorer."""
    if not text:
        return text
    text = unicodedata.normalize("NFKC", text)
    text = unify_chars(text)
    text = unify_digits(text, direction=digit_direction)
    text = map_punctuation(text)
    text = strip_bidi_isolates(text)
    text = unicodedata.normalize("NFC", text)
    return text


if __name__ == "__main__":
    tests = [
        ("يحيى", "یحیی"),       # yeh variants
        ("كشمير", "کشمیر"),       # kaf variants
        ("۱۲۳", "١٢٣"),            # digit forms (Persian → Arabic-Indic)
        ("\u2066كشمير\u2069", "کشمیر"),  # bidi isolates
        ("۔", "."),                  # Urdu full stop
        ("مكتب", "مکتب"),            # teh marbuta → heh
    ]
    print("normalize_arabic self-test:")
    all_pass = True
    for inp, expected in tests:
        out = normalize_arabic(inp)
        status = "PASS" if out == expected else "FAIL"
        if out != expected:
            all_pass = False
        print(f"  {status}: {inp!r} → {out!r} (expected {expected!r})")
    print(f"\n{'ALL PASS' if all_pass else 'SOME FAIL'}")
