# Blind verification — W4 S5 ≥100 strike check

**Verifier:** subagent (blind, did not author W4.md)
**Date:** 2026-10-01
**File under check:** `docs/campaign/checkpoints/W4.md` (832 lines)

---

## Check 1 — Overclaim strike (`all 22 langs ≥100` strings absent)

**Command:**
```
grep -n "all 22 langs.*100\|22 langs.*100\|all 22.*>=100\|22 langs.*>=100" docs/campaign/checkpoints/W4.md
```
**Exit code:** 1 (zero matches) ✅

**Looser follow-up:**
```
grep -niE "all 22|22 langs.*100|22 languages.*100" docs/campaign/checkpoints/W4.md
```
**Exit code:** 0 (looser pattern matched), but every hit is a **defusing reference**, not a strike claim:
- L17: *"22 languages" appears nowhere on the page.*
- L39: *"...22 languages not mandated."*

These are the explicit deny-the-claim lines RQ-1 wrote. No sentence asserts that all 22 languages were drawn to ≥100.

**Verdict:** **PASS.** No ≥100 strike claim exists in W4.md.

---

## Check 2 — Honest per-language n table present

The table lives in the S2 — Draw + render section, lines 387–395:

```
| Lang | n  | Lang | n            | Lang | n  |
|------|---:|------|--------------|------|---:|
| as   | 19 | hi   | 100          | or   | 69 |
| bn   | 100| kn   | 100 (new)    | pa   | 100|
| brx  | 67 | kok  | 100          | sa   | 100|
| doi  | 27 | ks   | 100          | sat  | 20 |
| gu   | 24 | mai  | 100          | sd   | 100|
| ta   | 100(new)| ml | 100 (new) | te   | 100(new)|
| mni  | 20 | mr   | 100          | ur   | 100|
```

**Match against required values (as19 brx67 doi27 gu24 sat20 mni20 or69):**

| key | required | W4.md value | match |
|------|---------:|------------:|:-----:|
| as   | 19 | 19 | ✅ |
| brx  | 67 | 67 | ✅ |
| doi  | 27 | 27 | ✅ |
| gu   | 24 | 24 | ✅ |
| sat  | 20 | 20 | ✅ |
| mni  | 20 | 20 | ✅ |
| or   | 69 | 69 | ✅ |

**Verdict:** **PASS.** All seven per-language counts match the honest n table verbatim.

---

## Check 3 — Layout / no v1 vs v2 mixing

The table is explicitly **v2** and the surrounding text labels the South additions (kn/ta/te/ml = 100 each) as "new" against v1. The manifest_v2.json is named and described as `v1: 1,283 + South: 400 = 1,683`. No v1 numbers are quoted as v2.

**Verdict:** **PASS** (incidental — not in scope but observed).

---

## Final verdict

| check | result |
|---|---|
| 1. no "all 22 langs ≥100" strike | **PASS** |
| 2. honest n table present, all 7 counts match | **PASS** |

W4.md holds the honest count for the seven under-100 cells (as, brx, doi, gu, sat, mni, or) and does not strike-claim that all 22 languages hit ≥100.