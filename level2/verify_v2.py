#!/usr/bin/env python3
"""Verification Suite v2 — beyond verify_all.py.

Adds:
  - coverage_ge6 (>=6/10 engines produce nonempty text; renamed from 'consensus')
  - true consensus (>=6 engines AND median pairwise token Jaccard >= 0.5)
  - B9 char 5-gram consensus (family-deduped votes, median pairwise Jaccard >= 0.6)
  - B11 CER/WER floor vs PDF-layer GT -> CER_STAGE3B.json (Stage-3b preference pairs)
  - B11.1 GT-quality gate (C2 14 Sep): Indic-tagged pages whose layer is <15% Indic
    = legacy-font mojibake -> CER/WER nulled (reason legacy_mojibake_layer), never ranked
  - B12 L1-gold cross-check CER -> l1_crosscheck
  - B16 line-count sanity (<50% of GT lines on dense pages, GT >= 10 lines)
  - B6 absent packs surfaced per engine in LEADERBOARD.md
  - B22 regression alarm vs previous run (baseline kept in _verify_v2_previous.json)
  - repetition-loop detection (n-gram redundancy)
  - charset hallucination (script X output on script Y page), with
    manifest dominant_script cross-check and manifest_tag_suspects
  - JSON schema validation of every pack (missing tracked explicitly)
  - per-page runtime telemetry from HEARTBEAT.jsonl (median ms/page, pages/hour)
  - script-sliced leaderboard (LEADERBOARD_BY_SCRIPT.md)
  - consolidated CSV: page_id x engine matrix
Outputs: reports/VERIFY_V2_SUMMARY.json, reports/MATRIX.csv, reports/LEADERBOARD.md,
          reports/LEADERBOARD_BY_SCRIPT.md, reports/TRUE_CONSENSUS.json, reports/FAILURE_TAXONOMY.md,
          reports/CER_STAGE3B.json
"""
from __future__ import annotations

import csv
import hashlib
import json
import time
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
OUT = L2 / "out"
REPORTS = L2 / "reports"

ENGINES = [
    "tesseract_indic", "openbharatocr", "easyocr", "paddleocr_indic",
    "indicphotoocr", "rapidocr", "tesseract_bilingual", "doctr",
    "surya", "anuvaad_tesseract",
]

SCRIPT_RANGES = {
    "Telugu": (0x0C00, 0x0C7F), "Tamil": (0x0B80, 0x0BFF),
    "Kannada": (0x0C80, 0x0CFF), "Malayalam": (0x0D00, 0x0D7F),
    "Devanagari": (0x0900, 0x097F), "Latin": (0x0041, 0x007A),
}

SCRIPT_BUCKETS = ["Latin", "Telugu", "Tamil", "Kannada", "Malayalam", "Devanagari"]

REQUIRED_KEYS = {"page_id", "source", "lang", "script", "quality_tier",
                 "image", "regions", "ocr_engine"}
REQ_REGION_KEYS = {"region_id", "cls", "bbox_xyxy", "text"}

L1_DIR = ROOT / "arc_level_1" / "labeled"
L1_LANGS = ("te", "ta", "kn", "ml")

# tesseract-family engines mirror one model — one vote in family/5-gram consensus
FAMILY = {
    "tesseract_family": {"tesseract_indic", "tesseract_bilingual",
                         "anuvaad_tesseract", "openbharatocr"},
}


def family_of(e: str) -> str:
    for fam, members in FAMILY.items():
        if e in members:
            return fam
    return e


FAMILY_MEMBERS = FAMILY["tesseract_family"]


def cer_norm(text: str) -> str:
    """NFC, lowercase, whitespace collapsed to single spaces — CER/WER basis."""
    t = unicodedata.normalize("NFC", text).lower()
    return " ".join(t.split())


def char_ngrams(t: str, n: int = 5) -> set[str]:
    """Char n-gram SET of a whitespace-stripped string (B9 basis)."""
    s = "".join(t.split())
    if len(s) < n:
        return set()
    return {s[i:i+n] for i in range(len(s) - n + 1)}


def edit_distance(a, b) -> int:
    """Levenshtein via Myers bit-vector (exact S+D+I; lists allowed for words)."""
    if a == b:
        return 0
    m, n = len(a), len(b)
    if m == 0:
        return n
    if n == 0:
        return m
    if m > 950:
        a, b, m, n = b, a, n, m
    peq: dict = {}
    for i, c in enumerate(a):
        peq[c] = peq.get(c, 0) | (1 << i)
    full = (1 << m) - 1
    msb = 1 << (m - 1)
    pv, mv, score = full, 0, m
    for c in b:
        eq = peq.get(c, 0)
        xv = eq | mv
        xh = (((eq & pv) + pv) ^ pv) | eq
        ph = mv | (~(xh | pv) & full)
        mh = pv & xh
        if ph & msb:
            score += 1
        elif mh & msb:
            score -= 1
        ph = ((ph << 1) | 1) & full
        mh = (mh << 1) & full
        pv = mh | (~(xv | ph) & full)
        mv = xv & ph
    return score


def build_index() -> dict[str, dict[str, Path]]:
    """engine -> {page_id: pack path} for every pack on disk."""
    idx = {}
    for e in ENGINES:
        m: dict[str, Path] = {}
        d = OUT / e
        if d.exists():
            for p in sorted(d.rglob("*.json")):
                m.setdefault(p.stem, p)
        idx[e] = m
    return idx


def pack_text(path: Path) -> str | None:
    """Joined region text; None when the pack JSON is unreadable."""
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
        return "\n".join(r.get("text", "") for r in obj.get("regions", []))
    except Exception:
        return None


def schema_state(path: Path | None) -> str:
    """'ok' | 'bad_schema' | 'bad_json' | 'missing' for one pack path."""
    if path is None:
        return "missing"
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return "bad_json"
    if not REQUIRED_KEYS.issubset(obj.keys()):
        return "bad_schema"
    for r in obj.get("regions", []):
        if not REQ_REGION_KEYS.issubset(r.keys()):
            return "bad_schema"
        bb = r.get("bbox_xyxy")
        if not (isinstance(bb, list) and len(bb) == 4):
            return "bad_schema"
    return "ok"


def script_of(text: str) -> str | None:
    h = Counter()
    for ch in text:
        cp = ord(ch)
        for name, (lo, hi) in SCRIPT_RANGES.items():
            if lo <= cp <= hi:
                h[name] += 1
                break
    return h.most_common(1)[0][0] if h else None


def normalized_tokens(text: str) -> set[str]:
    """NFC, lowercase, whitespace tokens with punctuation/symbols stripped."""
    t = unicodedata.normalize("NFC", text).lower()
    out = set()
    for w in t.split():
        w = "".join(c for c in w if unicodedata.category(c)[0] not in ("P", "S"))
        if w:
            out.add(w)
    return out


def jaccard(a: set[str], b: set[str]) -> float:
    u = a | b
    return len(a & b) / len(u) if u else 1.0


def loop_redundancy(text: str) -> float:
    """0..1 — fraction of 8-grams that repeat. >0.6 = collapse loop."""
    words = text.split()
    if len(words) < 16:
        return 0.0
    grams = [" ".join(words[i:i+8]) for i in range(len(words) - 7)]
    uniq = len(set(grams))
    return 1 - (uniq / len(grams))


def garbage_ratio(text: str) -> float:
    """0..1 — chars that are neither letter/mark/number nor common punct/space vs total."""
    t = text.strip()
    if not t:
        return 0.0
    ok = set(" \n\t.,;:!?\"'()-–—/|।॥%₹")
    letters = sum(1 for c in t if unicodedata.category(c)[0] in ("L", "M", "N"))
    noise = sum(1 for c in t if unicodedata.category(c)[0] not in ("L", "M", "N", "Z") and c not in ok)
    return round(noise / max(len(t), 1), 3)


def nfc_ok(text: str) -> bool:
    return unicodedata.normalize("NFC", text) == text


NATIVE_DIGIT_RANGES = [(0x0C66, 0x0C6F), (0x0BE6, 0x0BEF), (0x0CE6, 0x0CEF),
                       (0x0D66, 0x0D6F), (0x0966, 0x096F)]


def digit_profile(text: str) -> dict:
    native = ascii_ = 0
    for ch in text:
        cp = ord(ch)
        if any(lo <= cp <= hi for lo, hi in NATIVE_DIGIT_RANGES):
            native += 1
        elif "0" <= ch <= "9":
            ascii_ += 1
    return {"native": native, "ascii": ascii_}


def english_leak(text: str, page_script: str) -> bool:
    """Indic-script page whose output is overwhelmingly ASCII words (not digits/punct)."""
    if page_script == "Latin":
        return False
    words = [w for w in text.split() if len(w) >= 3]
    if len(words) < 5:
        return False
    ascii_words = sum(1 for w in words if all(ord(c) < 128 for c in w))
    return ascii_words / len(words) > 0.9


def heartbeat_stats() -> dict:
    """Per-engine median ms/page + pages/hour from HEARTBEAT.jsonl (latest per page wins)."""
    hb = L2 / "HEARTBEAT.jsonl"
    acc = {e: {"dur_entries": 0, "fail_entries": 0,
               "pages": {}}
           for e in ENGINES}
    if hb.exists():
        with hb.open(encoding="utf-8") as f:
            for line in f:
                try:
                    o = json.loads(line)
                except Exception:
                    continue
                e = o.get("engine")
                if e not in acc:
                    continue
                if o.get("fail"):
                    acc[e]["fail_entries"] += 1
                d = o.get("dur_ms")
                if d is None:
                    continue
                acc[e]["dur_entries"] += 1
                pid = o.get("page_id")
                prev = acc[e]["pages"].get(pid)
                if prev is None or o.get("t", 0) >= prev[0]:
                    acc[e]["pages"][pid] = (o.get("t", 0), d)
    out = {}
    for e in ENGINES:
        durs = sorted(d for _, d in acc[e]["pages"].values())
        m = median(durs) if durs else None
        out[e] = {
            "heartbeat_dur_entries": acc[e]["dur_entries"],
            "heartbeat_fail_entries": acc[e]["fail_entries"],
            "distinct_pages_timed": len(durs),
            "median_ms_per_page": round(m) if m is not None else None,
            "pages_per_hour": round(3_600_000 / m, 1) if m else None,
        }
    return out


def pdf_text_by_page(manifest: list[dict]) -> dict[str, str]:
    """page_id -> PDF text-layer text ('' when unavailable); one open per unique raw PDF."""
    out = {it["page_id"]: "" for it in manifest}
    try:
        import pymupdf
    except ImportError:
        return out
    by_raw = defaultdict(list)
    for it in manifest:
        by_raw[it["raw_path"]].append(it)
    for raw, items in by_raw.items():
        rp = ROOT / raw
        if not rp.exists():
            continue
        try:
            doc = pymupdf.open(rp)
        except Exception:
            continue
        for it in items:
            try:
                out[it["page_id"]] = doc[int(it["page_index"])].get_text()
            except Exception:
                pass
        doc.close()
    return out


def load_l1_gold() -> dict[str, str]:
    """page_id -> joined L1 region text from arc_level_1/labeled/{te,ta,kn,ml}."""
    out: dict[str, str] = {}
    for lang in L1_LANGS:
        d = L1_DIR / lang
        if not d.exists():
            continue
        for p in sorted(d.glob("*.json")):
            try:
                obj = json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                continue
            pid = obj.get("page_id") or p.stem
            out[pid] = "\n".join(r.get("text", "") for r in obj.get("regions", []))
    return out


def manifest_render_check() -> dict:
    """Items 41/58/59/60: manifest integrity + render checksum sanity from disk."""
    manifest = json.loads((L2 / "pages_manifest.json").read_text(encoding="utf-8"))
    renders = L2 / "renders_shared"
    out = {"n_manifest": len(manifest), "missing_raw": [], "bad_page_index": [],
           "locked_pdfs": [], "missing_render": [], "stale_render": [],
           "render_noise": 0}
    seen_raw = {}
    locked = set()
    try:
        import pymupdf
    except ImportError:
        pymupdf = None
    for item in manifest:
        raw = ROOT / item["raw_path"]
        if not raw.exists():
            out["missing_raw"].append(item["page_id"])
            continue
        if not (0 <= int(item["page_index"]) < int(item["pdf_pages"])):
            out["bad_page_index"].append(item["page_id"])
        rp = str(raw)
        if rp not in seen_raw:
            seen_raw[rp] = True
            if pymupdf is not None:
                try:
                    doc = pymupdf.open(raw)
                    if doc.needs_pass:
                        locked.add(rp)
                    doc.close()
                except Exception:
                    pass
        png = renders / f"{item['page_id']}.png"
        if not png.exists():
            out["missing_render"].append(item["page_id"])
        else:
            if png.stat().st_size < 2000:
                out["stale_render"].append(item["page_id"])
    out["locked_pdfs"] = sorted(locked)
    out["render_noise"] = len([p for p in renders.glob("*_bin.png")]) if renders.exists() else 0
    if renders.exists():
        out["n_renders"] = len([p for p in renders.glob("*_*.png") if not p.name.endswith("_bin.png")])
    else:
        out["n_renders"] = 0
    return out


def main() -> None:
    t_start = time.time()
    REPORTS.mkdir(exist_ok=True)
    manifest = json.loads((L2 / "pages_manifest.json").read_text(encoding="utf-8"))
    idx = build_index()
    gt = pdf_text_by_page(manifest)
    # task 7: ONE extraction cache reused by all engines + all checks
    gt_raw: dict[str, str] = {pid: (gt.get(pid, "") or "").strip() for pid in (it["page_id"] for it in manifest)}
    gt_norm: dict[str, str] = {pid: cer_norm(t) for pid, t in gt_raw.items()}
    gt_words: dict[str, list[str]] = {pid: t.split() for pid, t in gt_norm.items()}
    l1_gold = load_l1_gold()
    l1_norm: dict[str, str] = {pid: cer_norm(t) for pid, t in l1_gold.items()}
    l1_words: dict[str, list[str]] = {pid: t.split() for pid, t in l1_norm.items()}

    agg = {e: {"empty": 0, "thin": 0, "loop": 0, "checked": 0, "missing": 0,
               "chars": [], "garbage": [], "nfc_bad": 0, "eng_leak": 0,
               "native_digits": 0,
               "ascii_digits_on_indic": 0, "cap_l1": [], "cap_pdf": [],
               "by_script": defaultdict(list), "by_script_packs": defaultdict(int),
               "by_script_thin": defaultdict(int),
               "by_script_cap": defaultdict(list)} for e in ENGINES}
    coverage_count = 0
    coverage_pages = []
    true_consensus_pages = []
    family_consensus_pages = []
    fam_detail: dict[str, dict] = {}
    true_consensus_detail: dict[str, dict] = {}
    matrix_rows = []
    halluc = []
    suspect_pages: dict[str, dict] = {}
    schema_bad = []
    schema_missing = []
    text_hash: dict[str, set[str]] = {e: set() for e in ENGINES}
    dup_texts: dict[str, dict[str, int]] = {e: {} for e in ENGINES}
    # B9 char 5-gram consensus (law spec) — family-deduped votes
    consensus5_pages = []
    consensus5_detail: dict[str, dict] = {}
    # B11 CER/WER floor vs PDF-layer GT (Stage-3b preference-pair labels)
    cer_per_page: dict[str, dict] = {}
    cer_collect: dict[str, list[float]] = {e: [] for e in ENGINES}
    wer_collect: dict[str, list[float]] = {e: [] for e in ENGINES}
    best_engine_wins: Counter = Counter()
    # B12 L1-gold cross-check
    l1_cer_collect: dict[str, list[float]] = {e: [] for e in ENGINES}
    l1_cer_gt1: dict[str, list[str]] = {e: [] for e in ENGINES}
    gt_thin_counts: dict[str, int] = {e: 0 for e in ENGINES}
    mojibake_page_count = 0
    # B16 line-count sanity
    lines_short: dict[str, list[str]] = {e: [] for e in ENGINES}

    for item in manifest:
        pid = item["page_id"]
        dom = item.get("dominant_script")
        row = {"page_id": pid, "dominant_script": dom,
               "mixed_book": item.get("mixed_book_page", False)}
        live_engines = 0
        page_tokens: dict[str, set[str]] = {}
        page_scripts: dict[str, str] = {}
        fam_tokens: dict[str, set[str]] = {}
        fam_5grams: dict[str, set[str]] = {}
        page_row_cer: dict[str, dict] = {}
        gtn = gt_norm.get(pid, "")
        gt_w = gt_words.get(pid, [])
        l1n = l1_norm.get(pid)
        l1_w = l1_words.get(pid, [])
        gt_lines = len([ln for ln in gt_raw.get(pid, "").splitlines() if ln.strip()])
        # GT-quality gate (C2, 14 Sep): Indic-tagged pages whose PDF layer is
        # <15% Indic are legacy-font mojibake — CER vs them is meaningless.
        # Null the page (all engines) with reason; never feeds rankings.
        gt_mojibake = False
        if dom in ("Telugu", "Tamil", "Kannada", "Malayalam", "Devanagari"):
            raw_gt = gt_raw.get(pid, "") or ""
            if raw_gt.strip():
                n_indic = sum(1 for c in raw_gt if 0x0900 <= ord(c) <= 0x0DFF)
                if n_indic / len(raw_gt.strip()) < 0.15:
                    gt_mojibake = True
        if gt_mojibake:
            mojibake_page_count += 1
        for e in ENGINES:
            p = idx[e].get(pid)
            state = schema_state(p)
            if state == "missing":
                schema_missing.append(f"{e}/{pid}")
                agg[e]["missing"] += 1
                row[e] = None
                if len(gtn) < 200:
                    page_row_cer[e] = {"cer": None, "wer": None,
                                       "gt_chars": len(gtn),
                                       "reason": "gt_thin"}
                continue
            if state != "ok":
                schema_bad.append(f"{e}/{pid}")
            row[e] = 0
            txt = (pack_text(p) or "").strip()
            agg[e]["checked"] += 1
            if dom:
                agg[e]["by_script_packs"][dom] += 1
            if not txt:
                agg[e]["empty"] += 1
                if gt_mojibake:
                    page_row_cer[e] = {"cer": None, "wer": None,
                                       "gt_chars": len(gtn),
                                       "reason": "legacy_mojibake_layer"}
                elif len(gtn) < 200:
                    page_row_cer[e] = {"cer": None, "wer": None,
                                       "gt_chars": len(gtn),
                                       "reason": "gt_thin"}
                else:
                    cer_collect[e].append(1.0)
                    wer_collect[e].append(1.0)
                    page_row_cer[e] = {"cer": 1.0, "wer": 1.0,
                                       "gt_chars": len(gtn)}
                continue
            row[e] = len(txt)
            live_engines += 1
            agg[e]["chars"].append(len(txt))
            if len(txt) < 30:
                agg[e]["thin"] += 1
            if dom:
                agg[e]["by_script"][dom].append(len(txt))
                if len(txt) < 30:
                    agg[e]["by_script_thin"][dom] += 1
            etxt = cer_norm(txt)
            eng_words = etxt.split()
            if gt_mojibake:
                # legacy-font mojibake layer (C2): CER/WER vs it is noise
                page_row_cer[e] = {"cer": None, "wer": None,
                                   "gt_chars": len(gtn),
                                   "reason": "legacy_mojibake_layer"}
            elif len(gtn) >= 200:
                ratio = round(len(etxt) / len(gtn), 3)
                agg[e]["cap_pdf"].append(ratio)
                if dom:
                    agg[e]["by_script_cap"][dom].append(ratio)
                ed = edit_distance(etxt, gtn)
                cer = round(ed / len(gtn), 4)
                cer_collect[e].append(cer)
                wer = (round(edit_distance(eng_words, gt_w) / len(gt_w), 4)
                       if gt_w else None)
                if wer is not None:
                    wer_collect[e].append(wer)
                page_row_cer[e] = {"cer": cer, "wer": wer,
                                   "gt_chars": len(gtn)}
            else:
                gt_thin_counts[e] += 1
                page_row_cer[e] = {"cer": None, "wer": None,
                                   "gt_chars": len(gtn),
                                   "reason": "gt_thin"}
            # B12: same CER vs L1 gold text (>=200 chars)
            if l1n is not None and len(l1n) >= 200:
                l1_cer = round(edit_distance(etxt, l1n) / len(l1n), 4)
                l1_cer_collect[e].append(l1_cer)
                if l1_cer > 1.0:
                    l1_cer_gt1[e].append(pid)
            # B16: dense GT pages, engine emitted <50% of GT lines
            if gt_lines >= 10:
                eng_lines = len(txt.splitlines())
                if eng_lines < gt_lines * 0.5:
                    lines_short[e].append(pid)
            l1 = item.get("l1_chars") or 0
            if l1 > 200:
                agg[e]["cap_l1"].append(round(len(txt) / l1, 3))
            if loop_redundancy(txt) > 0.6:
                agg[e]["loop"] += 1
            gr = garbage_ratio(txt)
            if gr > 0.3:
                agg[e]["garbage"].append(f"{pid}({gr})")
            if not nfc_ok(txt):
                agg[e]["nfc_bad"] += 1
            if english_leak(txt, dom or "Latin"):
                agg[e]["eng_leak"] += 1
            dp = digit_profile(txt)
            if dp["native"]:
                agg[e]["native_digits"] += 1
            if dom and dom != "Latin" and dp["ascii"] > 10 and dp["native"] == 0:
                agg[e]["ascii_digits_on_indic"] += 1
            h = hashlib.sha1(txt[:400].encode("utf-8")).hexdigest()
            text_hash[e].add(h)
            dup_texts[e][h] = dup_texts[e].get(h, 0) + 1
            toks = normalized_tokens(txt)
            if toks:
                page_tokens[e] = toks
                fam = family_of(e)
                # family union: tesseract-mirror engines pool their tokens as ONE vote
                fam_tokens[fam] = fam_tokens.get(fam, set()) | set(toks)
            grams = char_ngrams(etxt, 5)
            if grams:
                fam = family_of(e)
                fam_5grams[fam] = fam_5grams.get(fam, set()) | grams
            s = script_of(txt)
            if s:
                page_scripts[e] = s
        if page_row_cer:
            scored = [(e, v["cer"]) for e, v in page_row_cer.items()
                      if v.get("cer") is not None]
            if scored:
                best_engine_wins[min(scored, key=lambda kv: kv[1])[0]] += 1
            cer_per_page[pid] = page_row_cer
        if live_engines >= 6:
            coverage_count += 1
            coverage_pages.append(pid)
        if len(page_tokens) >= 6:
            engs = sorted(page_tokens)
            js = [jaccard(page_tokens[engs[i]], page_tokens[engs[j]])
                  for i in range(len(engs)) for j in range(i + 1, len(engs))]
            mj = median(js)
            true_consensus_detail[pid] = {
                "engines_with_text": len(page_tokens),
                "median_pairwise_jaccard": round(mj, 4)}
            if mj >= 0.5:
                true_consensus_pages.append(pid)
        # family-grouped consensus: tesseract-family mirrors count as ONE engine
        if len(fam_tokens) >= 6:
            fams = sorted(fam_tokens)
            fjs = [jaccard(fam_tokens[fams[i]], fam_tokens[fams[j]])
                   for i in range(len(fams)) for j in range(i + 1, len(fams))]
            fmj = median(fjs)
            fam_detail[pid] = {
                "independent_votes": len(fams),
                "median_pairwise_jaccard": round(fmj, 4)}
            if fmj >= 0.5:
                family_consensus_pages.append(pid)
        # B9: char 5-gram consensus — family-deduped votes, median pairwise >= 0.6
        if len(fam_5grams) >= 6:
            keys = sorted(fam_5grams)
            grams_js = [jaccard(fam_5grams[keys[i]], fam_5grams[keys[j]])
                        for i in range(len(keys)) for j in range(i + 1, len(keys))]
            g5 = median(grams_js)
            consensus5_detail[pid] = {
                "independent_votes": len(keys),
                "median_pairwise_jaccard_5gram": round(g5, 4)}
            if g5 >= 0.6:
                consensus5_pages.append(pid)
        if not item.get("mixed_book_page", False) and dom and dom != "unknown":
            votes = Counter(s for s in page_scripts.values()
                            if s and s != "Latin" and s != dom)
            for s, n in votes.most_common():
                if n >= 3:
                    suspect_pages[pid] = {
                        "page_id": pid, "lang_tag": item["lang"],
                        "dominant_script": dom, "output_script": s,
                        "engines": sorted(e for e, sc in page_scripts.items()
                                          if sc == s),
                        "note": ">=3 engines independently output this script; "
                                "suspected manifest dominant_script tag error"}
                else:
                    halluc.extend(
                        {"page": pid, "engine": e, "page_script": dom,
                         "output_script": s}
                        for e, sc in sorted(page_scripts.items()) if sc == s)
        matrix_rows.append(row)

    # P1: Hallucination count after removing manifest tag suspects
    # (true hallucinations = engines reading wrong script on correctly-tagged pages)
    suspect_pids = set(suspect_pages.keys())
    halluc_after_correction = [h for h in halluc if h["page"] not in suspect_pids]

    with open(REPORTS / "MATRIX.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(matrix_rows[0].keys()))
        w.writeheader()
        w.writerows(matrix_rows)

    hb = heartbeat_stats()
    summary = {}
    for e in ENGINES:
        a = agg[e]
        chars = sorted(a["chars"])
        med = chars[len(chars)//2] if chars else 0
        p10 = chars[len(chars)//10] if chars else 0
        p90 = chars[int(len(chars)*0.9)] if chars else 0
        dup_max = max(dup_texts[e].values()) if dup_texts[e] else 0
        caps_l1 = sorted(a["cap_l1"])
        med_cap_l1 = caps_l1[len(caps_l1)//2] if caps_l1 else None
        caps_pdf = sorted(a["cap_pdf"])
        med_cap_pdf = caps_pdf[len(caps_pdf)//2] if caps_pdf else None
        by_script_med = {s: (sorted(v)[len(v)//2] if v else 0)
                         for s, v in sorted(a["by_script"].items())}
        summary[e] = {
            "checked": a["checked"],
            "missing_packs": a["missing"],
            "empty_rate": round(a["empty"] / a["checked"], 3) if a["checked"] else None,
            "thin_pages_lt30": a["thin"],
            "loop_pages": a["loop"],
            "median_chars": med,
            "median_capture_vs_l1": med_cap_l1,
            "median_capture_vs_pdf": med_cap_pdf,
            "by_script_median_chars": by_script_med,
            "p10_chars": p10,
            "p90_chars": p90,
            "total_output_chars": sum(chars),
            "garbage_pages_gt30pct": len(a["garbage"]),
            "garbage_examples": a["garbage"][:5],
            "nfc_violations": a["nfc_bad"],
            "english_leak_pages": a["eng_leak"],
            "lines_short_vs_gt": len(lines_short[e]),
            "native_digit_pages": a["native_digits"],
            "ascii_digits_on_indic_pages": a["ascii_digits_on_indic"],
            "distinct_output_hashes": len(text_hash[e]),
            "max_duplicate_pages": dup_max,
            **hb[e],
        }
        summary[e]["median_cer_vs_pdf"] = (round(median(cer_collect[e]), 4)
                                           if cer_collect[e] else None)
        summary[e]["median_wer_vs_pdf"] = (round(median(wer_collect[e]), 4)
                                           if wer_collect[e] else None)
        summary[e]["cer_pairs_vs_pdf"] = len(cer_collect[e])
        summary[e]["l1_crosscheck"] = {
            "median_cer_vs_l1": round(median(l1_cer_collect[e]), 4) if l1_cer_collect[e] else None,
            "l1_pages_compared": len(l1_cer_collect[e]),
            "l1_cer_gt1_pages": len(l1_cer_gt1[e]),
            "l1_cer_gt1_examples": l1_cer_gt1[e][:10],
        }
        summary[e]["lines_short_50pct"] = {
            "count": len(lines_short[e]),
            "page_ids": lines_short[e][:50],
        }

    (REPORTS / "TRUE_CONSENSUS.json").write_text(
        json.dumps({
            "definition": ">=6 engines with tokenizable output AND "
                          "median pairwise token-Jaccard >= 0.5 "
                          "(NFC, lowercase, punct-stripped, whitespace tokens)",
            "count": len(true_consensus_pages),
            "page_ids": true_consensus_pages,
            "per_page": true_consensus_detail,
            "family_consensus": {
                "definition": "tesseract-family (tesseract_indic, tesseract_bilingual, "
                              "anuvaad_tesseract, openbharatocr) pooled as ONE vote; "
                              ">=6 independent votes AND median pairwise Jaccard >= 0.5",
                "count": len(family_consensus_pages),
                "page_ids": family_consensus_pages,
                "per_page": fam_detail,
            },
            "consensus_5gram": {
                "definition": "char 5-gram SETS (NFC, lowercase, whitespace-stripped); "
                              "family-deduped votes (tesseract-family pooled as ONE vote "
                              "via union of 5-gram sets); >=6 independent votes AND "
                              "median pairwise Jaccard >= 0.6 (Law B9 spec)",
                "count": len(consensus5_pages),
                "page_ids": consensus5_pages,
                "per_page": consensus5_detail,
            },
        }, ensure_ascii=False, indent=1), encoding="utf-8")

    median_cer_per_engine = {e: summary[e]["median_cer_vs_pdf"] for e in ENGINES}
    best_engine_per_page = {}
    for item in manifest:
        pid = item["page_id"]
        row_c = cer_per_page.get(pid, {})
        scored = [(e, v["cer"]) for e, v in row_c.items() if v.get("cer") is not None]
        if scored:
            best = min(scored, key=lambda kv: kv[1])[0]
            best_engine_per_page[pid] = {"best_engine": best,
                                         "cer": row_c[best]["cer"]}
    (REPORTS / "CER_STAGE3B.json").write_text(
        json.dumps({
            "definition": "Stage-3b preference-pair labels: CER/WER of engine output "
                          "vs PDF text-layer GT (NFC, lowercase, whitespace-collapsed; "
                          "Levenshtein). Pages with <200 GT chars: null CER, reason gt_thin.",
            "per_page": cer_per_page,
            "median_cer_per_engine": median_cer_per_engine,
            "best_engine_per_page": best_engine_per_page,
        }, ensure_ascii=False, indent=1), encoding="utf-8")

    out = {
        "coverage_ge6": coverage_count,
        "coverage_ge6_definition": "pages where >=6 engines produced nonempty OCR text",
        "coverage_ge6_page_ids": coverage_pages,
        "true_consensus_pages": len(true_consensus_pages),
        "true_consensus_definition": ">=6 engines with text AND median pairwise "
                                     "token Jaccard >= 0.5 (see TRUE_CONSENSUS.json)",
        "true_consensus_page_ids": true_consensus_pages,
        "consensus_5gram_pages": consensus5_pages,
        "consensus_5gram_count": len(consensus5_pages),
        "consensus_5gram_definition": "char 5-gram SETS (NFC, lowercase, whitespace-stripped); "
                                     "family-deduped (tesseract-family = ONE vote); "
                                     ">=6 independent votes AND median pairwise "
                                     "Jaccard >= 0.6 (Law B9)",
        "consensus_pages": {
            "consensus_pages_ge6_engines": coverage_count,
            "consensus_page_ids": coverage_pages,
            "deprecated": True,
            "note": "legacy key: old 'consensus' was coverage, not agreement; "
                    "kept one release for dashboard compat — use coverage_ge6 "
                    "or true_consensus_pages",
        },
        "consensus_pages_ge6_engines": coverage_count,
        "consensus_page_ids": coverage_pages,
        "consensus_pages_deprecated": True,
        "manifest_render_check": manifest_render_check(),
        "schema_violations": len(schema_bad),
        "schema_violation_examples": schema_bad[:20],
        "schema_missing_packs": len(schema_missing),
        "schema_missing_examples": schema_missing[:20],
        "hallucination_events": len(halluc),
        "hallucination_examples": halluc[:10],
        "hallucination_after_tag_correction": len(halluc_after_correction),
        "hallucination_after_tag_correction_examples": halluc_after_correction[:10],
        "manifest_tag_suspects": sorted(suspect_pages.values(),
                                        key=lambda x: x["page_id"]),
        "l1_crosscheck": {e: summary[e]["l1_crosscheck"] for e in ENGINES},
        "lines_short_50pct": {e: summary[e]["lines_short_50pct"]["count"]
                              for e in ENGINES},
        "cer_stage3b": {
            "file": "CER_STAGE3B.json",
            "pairs_with_gt": sum(len(v) for v in cer_per_page.values()),
            "gt_thin_entries": sum(gt_thin_counts.values()),
            "gt_mojibake_entries": mojibake_page_count,
            "median_cer_per_engine": median_cer_per_engine,
            "best_engine_wins": dict(best_engine_wins),
        },
        "gt_mojibake_pages": mojibake_page_count,
        "heartbeat": hb,
        "engines": summary,
        "total_packs": sum(len(idx[e]) for e in ENGINES),
        "runtime_seconds": round(time.time() - t_start, 1),
    }

    # B22: regression alarm vs previous run (first run = baseline, no alarm)
    prev_path = REPORTS / "_verify_v2_previous.json"
    regression_alarm = []
    if prev_path.exists():
        try:
            prev = json.loads(prev_path.read_text(encoding="utf-8"))
        except Exception:
            prev = None
        if prev:
            def prev_metric(path: list):
                o: object = prev
                for k in path:
                    if not isinstance(o, dict) or k not in o:
                        return None
                    o = o[k]
                return o
            scalars = [("coverage_ge6", ["coverage_ge6"], "higher"),
                       ("true_consensus", ["true_consensus_pages"], "higher"),
                       ("consensus_5gram", ["consensus_5gram_count"], "higher"),
                       ("schema_missing", ["schema_missing_packs"], "lower")]
            for e in ENGINES:
                scalars.append((f"{e}.empty_rate", ["engines", e, "empty_rate"], "lower"))
                scalars.append((f"{e}.median_chars", ["engines", e, "median_chars"], "higher"))
            for name, path, better in scalars:
                cur_v = prev_metric(path)
                new_v: object = out
                for k in path:
                    new_v = new_v.get(k) if isinstance(new_v, dict) else None
                if new_v is None or cur_v is None:
                    continue
                if not isinstance(new_v, (int, float)) or not isinstance(cur_v, (int, float)):
                    continue
                if cur_v == new_v:
                    continue
                if better == "higher":
                    if new_v < cur_v and cur_v > 0:
                        rel = (cur_v - new_v) / abs(cur_v)
                        if rel > 0.02:
                            regression_alarm.append(
                                {"metric": name, "previous": cur_v, "current": new_v,
                                 "rel_regression": round(rel, 4)})
                else:
                    grew_worse = new_v > cur_v
                    base = abs(cur_v) if cur_v != 0 else None
                    rel = ((new_v - cur_v) / base) if base else None
                    if grew_worse and (rel is None or rel > 0.02):
                        regression_alarm.append(
                            {"metric": name, "previous": cur_v, "current": new_v,
                             "rel_regression": round(rel, 4) if rel is not None else None})
            prev_packs = prev.get("total_packs")
            cur_packs = out.get("total_packs")
            if isinstance(prev_packs, int) and isinstance(cur_packs, int) \
                    and cur_packs < prev_packs:
                regression_alarm.append({"metric": "total_packs",
                                         "previous": prev_packs,
                                         "current": cur_packs,
                                         "rel_regression": round(
                                             (prev_packs - cur_packs) / prev_packs, 4)})
    out["regression_alarm"] = regression_alarm
    try:
        old = json.loads((REPORTS / "VERIFY_V2_SUMMARY.json").read_text(encoding="utf-8"))
        prev_path.write_text(json.dumps(old, ensure_ascii=False, indent=1),
                             encoding="utf-8")
    except Exception:
        prev_path.write_text("{}", encoding="utf-8")

    (REPORTS / "VERIFY_V2_SUMMARY.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    tax_lines = ["# Failure Taxonomy — per engine (disk-truth)", "",
                 "Labels: EMPTY (no text) | LOOP (8-gram redundancy >0.6) | GARBAGE (>30% noise chars) |",
                 "ENG_LEAK (Indic page, >90% ASCII words) | LINES_SHORT (<50% of PDF-layer lines",
                 "on dense pages, GT >= 10 lines — B16) | NFC_BAD (text_nfc not normalized) |",
                 "DUP (same text on many pages).", "",
                 "| engine | empty | loop | garbage | eng-leak | lines-short | nfc-bad | max-dup | p10/med/p90 chars |",
                 "|---|---|---|---|---|---|---|---|---|"]
    for e, s in summary.items():
        empty_n = round(s["empty_rate"] * 400) if s["empty_rate"] is not None else "—"
        tax_lines.append(f"| {e} | {empty_n} | {s['loop_pages']} | "
                         f"{s['garbage_pages_gt30pct']} | {s['english_leak_pages']} | {s['lines_short_50pct']['count']} | "
                         f"{s['nfc_violations']} | {s['max_duplicate_pages']} | {s['p10_chars']}/{s['median_chars']}/{s['p90_chars']} |")
    (REPORTS / "FAILURE_TAXONOMY.md").write_text("\n".join(tax_lines) + "\n", encoding="utf-8")

    alarm_bits = [f"{a['metric']}: {a['previous']} -> {a['current']}"
                  for a in regression_alarm]
    lines = ["# Engine Leaderboard (open policy, disk-truth)", ""]
    if regression_alarm:
        lines += [f"**⚠ REGRESSION vs previous run ({len(regression_alarm)} metric(s)): "
                  f"{'; '.join(alarm_bits)}**", ""]
    lines += ["**per-language numbers mix scripts; see LEADERBOARD_BY_SCRIPT.md**", "",
              "| engine | checked | absent | empty% | thin | loops | median chars | total chars | med capture vs PDF | CER_med | ms/page | pages/hour |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for e, s in sorted(summary.items(), key=lambda kv: -(kv[1]["total_output_chars"] or 0)):
        cap = s.get("median_capture_vs_pdf")
        if cap is None:
            cap = s.get("median_capture_vs_l1")
        empty_pct = f"{s['empty_rate']*100:.1f}" if s['empty_rate'] is not None else "?"
        cer_med = s.get("median_cer_vs_pdf")
        lines.append(f"| {e} | {s['checked']} | {s['missing_packs']} | {empty_pct}% | {s['thin_pages_lt30']} | "
                     f"{s['loop_pages']} | {s['median_chars']} | {s['total_output_chars']} | "
                     f"{cap if cap is not None else '—'} | {cer_med if cer_med is not None else '—'} | {s['median_ms_per_page'] or '—'} | "
                     f"{s['pages_per_hour'] or '—'} |")
    lines += ["", f"coverage pages (>=6 engines nonempty; renamed from 'consensus'): {coverage_count}/400",
              f"true consensus pages (>=6 engines, median pairwise Jaccard >= 0.5): "
              f"{len(true_consensus_pages)}/400 — reports/TRUE_CONSENSUS.json",
              f"consensus_5gram pages (B9: family-deduped char 5-gram sets, median pairwise >= 0.6): "
              f"{len(consensus5_pages)}/400",
              f"schema violations: {len(schema_bad)} | missing packs: {len(schema_missing)}",
              f"hallucination events: {len(halluc)} | manifest tag suspects: {len(suspect_pages)}",
              "", "details: FAILURE_TAXONOMY.md, LEADERBOARD_BY_SCRIPT.md, CER_STAGE3B.json"]
    (REPORTS / "LEADERBOARD.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    lines = ["# Leaderboard by dominant script (manifest dominant_script buckets)", "",
             "Per-language tables mix scripts (e.g. 'te' pages are 47 Telugu + 42 Latin + 11 Devanagari).",
             "This is the script-sliced view; capture ratio vs PDF text layer "
             "(pages with >=200-char layer only).", ""]
    for b in SCRIPT_BUCKETS:
        pids = [it["page_id"] for it in manifest if it.get("dominant_script") == b]
        n_gt = sum(1 for p in pids if len(gt.get(p, "").strip()) >= 200)
        lines += [f"## {b} — {len(pids)} pages "
                  f"(capture computed on {n_gt} pages with >=200-char PDF text layer)", "",
                  "| engine | packs | empty | thin(<30c) | median chars | median capture |",
                  "|---|---|---|---|---|---|"]
        rows = []
        for e in ENGINES:
            a = agg[e]
            packs = a["by_script_packs"].get(b, 0)
            lens = sorted(a["by_script"].get(b, []))
            caps = sorted(a["by_script_cap"].get(b, []))
            med = lens[len(lens)//2] if lens else 0
            mcap = caps[len(caps)//2] if caps else None
            rows.append((e, packs, packs - len(lens),
                         a["by_script_thin"].get(b, 0), med, mcap))
        for e, packs, empty_n, thin, med, mcap in sorted(rows, key=lambda r: -r[4]):
            lines.append(f"| {e} | {packs} | {empty_n} | {thin} | {med} | "
                         f"{mcap if mcap is not None else '—'} |")
        winner = max(rows, key=lambda r: r[4])
        lines += ["", f"winner by median chars: **{winner[0]}** ({winner[4]} chars)", ""]
    (REPORTS / "LEADERBOARD_BY_SCRIPT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"coverage_ge6 (was 'consensus'): {coverage_count}/400")
    print(f"true_consensus_pages (median pairwise Jaccard >= 0.5): {len(true_consensus_pages)}/400")
    print(f"consensus_5gram_pages (B9, median pairwise 5-gram Jaccard >= 0.6): {len(consensus5_pages)}/400")
    if regression_alarm:
        print(f"⚠ REGRESSION ({len(regression_alarm)}): {'; '.join(alarm_bits)}")
    print(f"schema violations: {len(schema_bad)} | missing packs: {len(schema_missing)}")
    print(f"hallucinations: {len(halluc)} | manifest tag suspects: {len(suspect_pages)} "
          f"({', '.join(sorted(suspect_pages)) or 'none'})")
    mc = out["manifest_render_check"]
    print(f"manifest: missing_raw={len(mc['missing_raw'])} bad_index={len(mc['bad_page_index'])} "
          f"locked_pdfs={len(mc['locked_pdfs'])} missing_render={len(mc['missing_render'])} "
          f"tiny_render={len(mc['stale_render'])}")
    for e, s in summary.items():
        l1x = s["l1_crosscheck"]
        print(f"{e:<22} chk={s['checked']:>3} miss={s['missing_packs']:>3} empty={s['empty_rate']} "
              f"thin={s['thin_pages_lt30']:>3} loops={s['loop_pages']:>3} medChars={s['median_chars']:>5} "
              f"leak={s['english_leak_pages']:>2} dup={s['max_duplicate_pages']:>2} "
              f"CERpdf={s['median_cer_vs_pdf'] if s['median_cer_vs_pdf'] is not None else '—'} "
              f"CERl1={l1x['median_cer_vs_l1'] if l1x['median_cer_vs_l1'] is not None else '—'} "
              f"l1gt1={l1x['l1_cer_gt1_pages']:>3} linesShort={s['lines_short_50pct']['count']:>3} "
              f"ms={s['median_ms_per_page'] or '—'} pph={s['pages_per_hour'] or '—'}")
    print(f"best-engine wins (min CER/page): {dict(best_engine_wins)}")
    print(f"runtime: {out['runtime_seconds']}s")
    print("\nwrote: MATRIX.csv, VERIFY_V2_SUMMARY.json, TRUE_CONSENSUS.json, "
          "LEADERBOARD.md, LEADERBOARD_BY_SCRIPT.md, FAILURE_TAXONOMY.md, CER_STAGE3B.json")


if __name__ == "__main__":
    main()
