# B-02 — Arabic normalization scorer module (PREP)

## What the task requires (proto-100 B-02)

Up to 3–8 pts of the Kashmiri "failure" may be a **scoring artifact**, not a recognition failure. The current `metrics.py` does NFKC + NFC normalization but lacks:
- **yeh/kaf variants**: ي → ی, ك → ک (presentation forms)
- **digit forms**: Persian/Urdu digits vs Arabic-Indic digits
- **punctuation map**: ، (Arabic comma) vs , (Latin comma); ؛ vs ; etc.
- **LRI/PDI bidi isolation**: U+2066–U+2069 left-to-right / right-to-left isolate marks
- **NFC vs NFKC + bidi normalization**

Without these, two visually identical Arabic strings can have different codepoints and score as errors.

## What we can do NOW (without downloads)

### 1. Check what `metrics.py` currently does (DONE — read the file)

Current normalization (`level2/benchmark/pipeline/metrics.py:128-168`):
- `normalize_for_metrics`: NFC + Indic punctuation + period-comma spacing + bullets
- `normalize_for_scoring`: NFKC → NFC
- `normalize_for_content`: base + content extras

**Missing**: yeh/kaf variant unification, digit-form mapping, bidi isolation mark handling, Arabic-specific punctuation mapping.

### 2. Design the NEW scorer module (allowed per proto-100: "add an opt-in `--normalize-arabic` in a NEW scorer module (never change the default; the locked files stay locked)")

**Location**: `level2/benchmark/scoring_extensions/normalize_arabic.py` (new module — locked files stay locked)

**Design**:
```python
# level2/benchmark/scoring_extensions/normalize_arabic.py
"""
Optional Arabic-specific normalization for scoring — NOT applied by default.
Per proto-100 B-02: scoring artifact may account for 3-8 pts of Kashmiri failure.
Use --normalize-arabic flag in benchmark scripts to enable.
Locked: this is a NEW module; level2/benchmark/pipeline/metrics.py is UNCHANGED.
"""
import unicodedata

def unify_arabic_chars(text: str) -> str:
    """Map presentation forms to base forms (yeh, kaf, heh, etc.)."""
    # Yeh variants: ي (U+064A) → ی (U+06CC); ئ (U+0626) → ی
    yeh_map = {'\u064A': '\u06CC', '\u0626': '\u06CC', '\u0649': '\u06CC'}
    # Kaf variants: ك (U+0643) → ک (U+06A9)
    kaf_map = {'\u0643': '\u06A9'}
    # Heh variants: ه (U+0647) → ه (U+0647); ة (U+0629) → ه
    text = ''.join(yeh_map.get(c, c) for c in text)
    text = ''.join(kaf_map.get(c, c) for c in text)
    return text

def unify_arabic_digits(text: str) -> str:
    """Map Persian/Urdu digits to Arabic-Indic (or vice versa)."""
    # Persian: ۰۱۲۳۴۵۶۷۸۹ (U+06F0–U+06F9)
    # Arabic-Indic: ٠١٢٣٤٥٦٧٨٩ (U+0660–U+0669)
    # Default: normalize to Arabic-Indic (Sarvam convention)
    for i in range(10):
        text = text.replace(chr(0x06F0 + i), chr(0x0660 + i))  # Persian → Arabic-Indic
    return text

def map_arabic_punctuation(text: str) -> str:
    """Map Arabic punctuation to Latin equivalents for comparison."""
    punct_map = {
        '،': ',',  # Arabic comma
        '؛': ';',  # Arabic semicolon
        '؟': '?',  # Arabic question mark
        '۔': '.',  # Urdu full stop
    }
    for ar, lat in punct_map.items():
        text = text.replace(ar, lat)
    return text

def isolate_bidi(text: str) -> str:
    """Remove LRI/PDI bidi isolation marks (U+2066–U+2069)."""
    return ''.join(c for c in text if c not in '\u2066\u2067\u2068\u2069')

def normalize_arabic(text: str) -> str:
    """Full Arabic normalization pipeline (opt-in, NEW module)."""
    if not text:
        return text
    text = unicodedata.normalize('NFKC', text)
    text = unify_arabic_chars(text)
    text = unify_arabic_digits(text)
    text = map_arabic_punctuation(text)
    text = isolate_bidi(text)
    text = unicodedata.normalize('NFC', text)
    return text
```

### 3. Wire into existing benchmark scripts

The `build_benchmark_22.py` and `evaluate.py` scripts can optionally import this module:
```python
try:
    from level2.benchmark.scoring_extensions.normalize_arabic import normalize_arabic
    APPLY_ARABIC = True
except ImportError:
    APPLY_ARABIC = False
```

### 4. Verify with synthetic test cases

```python
# Test: same visual text, different codepoints, should match
assert normalize_arabic('ي') == normalize_arabic('ی')  # yeh variants
assert normalize_arabic('ك') == normalize_arabic('ک')  # kaf variants
assert normalize_arabic('۱۲۳') == normalize_arabic('١٢٣')  # digit forms
assert normalize_arabic('‏کشمیر‏') == normalize_arabic('کشمیر')  # bidi marks
```

## What we need to run it

- Nothing! This is a new module — no downloads, no Bodhan weights needed
- Can be tested with synthetic Arabic strings + against the 100 ur/ks/sd probe items once probe22 results exist

## Exact commands to run when ready

```bash
# Test the module standalone
python3 level2/benchmark/scoring_extensions/normalize_arabic.py

# Run on Bodhan predictions once available
python3 level2/unified/eval_arabic.py \
    --predictions level2/benchmark/scores/bodhan_4bit/ \
    --output docs/campaign/B02_ARABIC_RESULTS.md
```

## Deliverable artifact

- **File**: `level2/benchmark/scoring_extensions/normalize_arabic.py` (NEW module — opt-in)
- **File**: `docs/campaign/B02_ARABIC_RESULTS.md` (raw vs normalized CER table for ur/ks/sd)
- **Location in BODHAN_BASELINE.md**: per-script precision table includes both raw and normalized CER for Perso-Arabic cells
- **Gate**: B-02 — does normalization reduce CER gap by ≥ 3pts on ur/ks/sd?
- **Status**: PREP — module designed, ready to write file + run

## Key constraint (proto-100 B-02 verbatim)

> Sarvam-bench numbers always use Sarvam's unchanged `metrics.py`

So the Sarvam-bench comparison column uses the default scorer (no Arabic normalization). Our Bodhan eval can use the NEW normalized scorer and report BOTH columns for transparency.
