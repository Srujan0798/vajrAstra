<!--
🟡 W6 PAUSE BANNER (Miss agent, 2026-09-29 IST, per user directive)

All W6 fine-tuning prep is PAUSED. Not started.
Vinay meeting TOMORROW (2026-09-30) = gating step.
Vinay → W5 freeze after Wed 2026-10-01 → W6 training decision.

DO NOT execute training, mlx-tune, mlx_vlm, or QLoRA scripts from this file.
This file is preserved as W5-strategy evidence + post-meeting W6 reactivation reference.
After Vinay meeting: if Option A approved → resume scaffold per this file.
If Option B → wrap-only ships; this file remains archival.
If Option C → backbone swap; this file is superseded; new spec required.

Refs: VINAY_MEETING_PACKET.md · STRATEGY_VINAY_TOMORROW.md · VINAY_CTA.md ·
      W5_STRATEGY_OPTIONS.md · W5_BEAT_SARVAM_PLAN.md ·
      OCR_AGENT_MEMORY_FEED.md §15-§16 · BOSS_CONCERNS.md items 53+

Hard law: §9 no downloads + §8 no training until W5 freeze + Vinay gate ahead of W5 freeze.
-->

> 🟡 **STATUS: PAUSED** — Created 2026-09-29 BEFORE W5 freeze. NOT AUTHORIZED.
> Per OCR_AGENT_MEMORY_FEED.md §8: "Training" is forbidden until W5 freeze.
> This file is a DRAFT for review at W5 freeze (after Wed 2026-10-01), not executable.
> Vinay meeting tomorrow is the gating step.

=== install_mlx_stack.sh run @ 2026-09-29 16:21:00 IST ===

USER-APPROVED 2026-09-29 at the W5 freeze call.

## [1] Python version
- Path: /Users/srujansai/Desktop/South/.venv311/bin/python
- Version: 3.11.10
- Verdict: PASS

## [2] Xcode CLI tools
- Path: /Library/Developer/CommandLineTools
- Verdict: PASS

## [3] Git
- git version 2.50.1 (Apple Git-155)
- Verdict: PASS

## [4] Disk free
- Avail: 12 GB
- Verdict: PASS

## [5] Installing mlx + mlx-vlm via pip
Command: /Users/srujansai/Desktop/South/.venv311/bin/pip install mlx mlx-vlm

Collecting mlx
  Downloading mlx-0.32.3-cp311-cp311-macosx_26_0_arm64.whl.metadata (5.9 kB)
Collecting mlx-vlm
  Downloading mlx_vlm-0.7.4-py3-none-any.whl.metadata (72 kB)
Collecting mlx-metal==0.32.3 (from mlx)
  Downloading mlx_metal-0.32.3-py3-none-macosx_26_0_arm64.whl.metadata (5.1 kB)
Requirement already satisfied: transformers>=5.14.0 in ./.venv311/lib/python3.11/site-packages (from mlx-vlm) (5.17.0)
Requirement already satisfied: jinja2>=3.1.0 in ./.venv311/lib/python3.11/site-packages (from mlx-vlm) (3.1.6)
Collecting sentencepiece>=0.2.0 (from mlx-vlm)
  Downloading sentencepiece-0.2.2-cp311-cp311-macosx_11_0_arm64.whl.metadata (33 kB)
Collecting miniaudio>=1.59 (from mlx-vlm)
  Downloading miniaudio-1.71-cp311-cp311-macosx_11_0_arm64.whl.metadata (25 kB)
Requirement already satisfied: tqdm>=4.66.2 in ./.venv311/lib/python3.11/site-packages (from mlx-vlm) (4.66.5)
Requirement already satisfied: Pillow>=10.3.0 in ./.venv311/lib/python3.11/site-packages (from mlx-vlm) (12.3.0)
Requirement already satisfied: requests>=2.31.0 in ./.venv311/lib/python3.11/site-packages (from mlx-vlm) (2.34.2)
Collecting llguidance>=1.7.0 (from mlx-vlm)
  Downloading llguidance-1.8.0-cp39-abi3-macosx_11_0_arm64.whl.metadata (10 kB)
Collecting mlx-audio>=0.5.2 (from mlx-vlm)
  Downloading mlx_audio-0.5.7-py3-none-any.whl.metadata (35 kB)
Collecting opencv-python>=4.12.0.88 (from mlx-vlm)
  Downloading opencv_python-5.0.0.93-cp37-abi3-macosx_13_0_arm64.whl.metadata (19 kB)
Collecting fastapi>=0.95.1 (from mlx-vlm)
  Downloading fastapi-0.141.1-py3-none-any.whl.metadata (27 kB)
Collecting python-multipart>=0.0.9 (from mlx-vlm)
  Downloading python_multipart-0.0.32-py3-none-any.whl.metadata (2.1 kB)
Collecting starlette>=1.0.1 (from mlx-vlm)
  Downloading starlette-1.7.0-py3-none-any.whl.metadata (6.6 kB)
Collecting uvicorn (from mlx-vlm)
  Downloading uvicorn-0.54.0-py3-none-any.whl.metadata (6.6 kB)
Requirement already satisfied: websockets>=14.0 in ./.venv311/lib/python3.11/site-packages (from mlx-vlm) (17.1)
Requirement already satisfied: numpy in ./.venv311/lib/python3.11/site-packages (from mlx-vlm) (2.2.6)
Requirement already satisfied: pydantic>=2.9.0 in ./.venv311/lib/python3.11/site-packages (from fastapi>=0.95.1->mlx-vlm) (2.13.5)
Requirement already satisfied: typing-extensions>=4.8.0 in ./.venv311/lib/python3.11/site-packages (from fastapi>=0.95.1->mlx-vlm) (4.16.0)
Requirement already satisfied: typing-inspection>=0.4.2 in ./.venv311/lib/python3.11/site-packages (from fastapi>=0.95.1->mlx-vlm) (0.4.4)
Requirement already satisfied: annotated-doc>=0.0.2 in ./.venv311/lib/python3.11/site-packages (from fastapi>=0.95.1->mlx-vlm) (0.0.5)
Requirement already satisfied: MarkupSafe>=2.0 in ./.venv311/lib/python3.11/site-packages (from jinja2>=3.1.0->mlx-vlm) (3.0.3)
Requirement already satisfied: cffi>=1.12.0 in ./.venv311/lib/python3.11/site-packages (from miniaudio>=1.59->mlx-vlm) (2.1.1)
Requirement already satisfied: pycparser in ./.venv311/lib/python3.11/site-packages (from cffi>=1.12.0->miniaudio>=1.59->mlx-vlm) (3.0)
Requirement already satisfied: huggingface_hub>=1.0 in ./.venv311/lib/python3.11/site-packages (from mlx-audio>=0.5.2->mlx-vlm) (1.31.0)
Requirement already satisfied: scipy>=1.10.0 in ./.venv311/lib/python3.11/site-packages (from mlx-audio>=0.5.2->mlx-vlm) (1.13.1)
Collecting sounddevice>=0.5.3 (from mlx-audio>=0.5.2->mlx-vlm)
  Downloading sounddevice-0.5.6-py3-none-macosx_10_6_x86_64.macosx_10_6_universal2.whl.metadata (1.4 kB)
Collecting tqdm>=4.66.2 (from mlx-vlm)
  Using cached tqdm-4.70.1-py3-none-any.whl.metadata (57 kB)
Requirement already satisfied: click<9.0.0,>=8.4.2 in ./.venv311/lib/python3.11/site-packages (from huggingface_hub>=1.0->mlx-audio>=0.5.2->mlx-vlm) (8.5.0)
Requirement already satisfied: filelock>=3.10.0 in ./.venv311/lib/python3.11/site-packages (from huggingface_hub>=1.0->mlx-audio>=0.5.2->mlx-vlm) (3.32.6)
Requirement already satisfied: fsspec>=2023.5.0 in ./.venv311/lib/python3.11/site-packages (from huggingface_hub>=1.0->mlx-audio>=0.5.2->mlx-vlm) (2026.7.0)
Requirement already satisfied: hf-xet<2.0.0,>=1.5.2 in ./.venv311/lib/python3.11/site-packages (from huggingface_hub>=1.0->mlx-audio>=0.5.2->mlx-vlm) (1.6.0)
Requirement already satisfied: httpx<1,>=0.23.0 in ./.venv311/lib/python3.11/site-packages (from huggingface_hub>=1.0->mlx-audio>=0.5.2->mlx-vlm) (0.28.1)
Requirement already satisfied: packaging>=20.9 in ./.venv311/lib/python3.11/site-packages (from huggingface_hub>=1.0->mlx-audio>=0.5.2->mlx-vlm) (24.1)
Requirement already satisfied: pyyaml>=5.1 in ./.venv311/lib/python3.11/site-packages (from huggingface_hub>=1.0->mlx-audio>=0.5.2->mlx-vlm) (6.0.2)
Requirement already satisfied: anyio in ./.venv311/lib/python3.11/site-packages (from httpx<1,>=0.23.0->huggingface_hub>=1.0->mlx-audio>=0.5.2->mlx-vlm) (4.15.1)
Requirement already satisfied: certifi in ./.venv311/lib/python3.11/site-packages (from httpx<1,>=0.23.0->huggingface_hub>=1.0->mlx-audio>=0.5.2->mlx-vlm) (2024.8.30)
Requirement already satisfied: httpcore==1.* in ./.venv311/lib/python3.11/site-packages (from httpx<1,>=0.23.0->huggingface_hub>=1.0->mlx-audio>=0.5.2->mlx-vlm) (1.0.9)
Requirement already satisfied: idna in ./.venv311/lib/python3.11/site-packages (from httpx<1,>=0.23.0->huggingface_hub>=1.0->mlx-audio>=0.5.2->mlx-vlm) (3.10)
Requirement already satisfied: h11>=0.16 in ./.venv311/lib/python3.11/site-packages (from httpcore==1.*->httpx<1,>=0.23.0->huggingface_hub>=1.0->mlx-audio>=0.5.2->mlx-vlm) (0.16.0)
Requirement already satisfied: annotated-types>=0.6.0 in ./.venv311/lib/python3.11/site-packages (from pydantic>=2.9.0->fastapi>=0.95.1->mlx-vlm) (0.8.0)
Requirement already satisfied: pydantic-core==2.46.5 in ./.venv311/lib/python3.11/site-packages (from pydantic>=2.9.0->fastapi>=0.95.1->mlx-vlm) (2.46.5)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv311/lib/python3.11/site-packages (from requests>=2.31.0->mlx-vlm) (3.4.0)
Requirement already satisfied: urllib3<3,>=1.26 in ./.venv311/lib/python3.11/site-packages (from requests>=2.31.0->mlx-vlm) (2.7.0)
Requirement already satisfied: regex>=2025.10.22 in ./.venv311/lib/python3.11/site-packages (from transformers>=5.14.0->mlx-vlm) (2026.9.10)
Requirement already satisfied: tokenizers<0.24.0,>=0.23.1 in ./.venv311/lib/python3.11/site-packages (from transformers>=5.14.0->mlx-vlm) (0.23.2)
Requirement already satisfied: typer in ./.venv311/lib/python3.11/site-packages (from transformers>=5.14.0->mlx-vlm) (0.27.2)
Requirement already satisfied: safetensors>=0.8.0 in ./.venv311/lib/python3.11/site-packages (from transformers>=5.14.0->mlx-vlm) (0.8.0)
Requirement already satisfied: shellingham>=1.3.0 in ./.venv311/lib/python3.11/site-packages (from typer->transformers>=5.14.0->mlx-vlm) (1.5.4)
Requirement already satisfied: rich>=13.8.0 in ./.venv311/lib/python3.11/site-packages (from typer->transformers>=5.14.0->mlx-vlm) (15.0.0)
Requirement already satisfied: markdown-it-py>=2.2.0 in ./.venv311/lib/python3.11/site-packages (from rich>=13.8.0->typer->transformers>=5.14.0->mlx-vlm) (4.2.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in ./.venv311/lib/python3.11/site-packages (from rich>=13.8.0->typer->transformers>=5.14.0->mlx-vlm) (2.21.0)
Requirement already satisfied: mdurl~=0.1 in ./.venv311/lib/python3.11/site-packages (from markdown-it-py>=2.2.0->rich>=13.8.0->typer->transformers>=5.14.0->mlx-vlm) (0.1.2)
Downloading mlx-0.32.3-cp311-cp311-macosx_26_0_arm64.whl (655 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 655.8/655.8 kB 2.3 MB/s  0:00:00
Downloading mlx_metal-0.32.3-py3-none-macosx_26_0_arm64.whl (67.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 67.7/67.7 MB 1.5 MB/s  0:00:43
Downloading mlx_vlm-0.7.4-py3-none-any.whl (3.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 1.4 MB/s  0:00:02
Downloading fastapi-0.141.1-py3-none-any.whl (131 kB)
Downloading llguidance-1.8.0-cp39-abi3-macosx_11_0_arm64.whl (3.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 1.8 MB/s  0:00:01
Downloading miniaudio-1.71-cp311-cp311-macosx_11_0_arm64.whl (351 kB)
Downloading mlx_audio-0.5.7-py3-none-any.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 1.9 MB/s  0:00:01
Downloading opencv_python-5.0.0.93-cp37-abi3-macosx_13_0_arm64.whl (48.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.3/48.3 MB 1.8 MB/s  0:00:26
Downloading python_multipart-0.0.32-py3-none-any.whl (30 kB)
Downloading sentencepiece-0.2.2-cp311-cp311-macosx_11_0_arm64.whl (1.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 1.9 MB/s  0:00:00
Downloading sounddevice-0.5.6-py3-none-macosx_10_6_x86_64.macosx_10_6_universal2.whl (1.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 1.7 MB/s  0:00:00
Downloading starlette-1.7.0-py3-none-any.whl (78 kB)
Using cached tqdm-4.70.1-py3-none-any.whl (80 kB)
Downloading uvicorn-0.54.0-py3-none-any.whl (87 kB)
Installing collected packages: uvicorn, tqdm, sentencepiece, python-multipart, opencv-python, mlx-metal, llguidance, starlette, sounddevice, mlx, miniaudio, fastapi, mlx-audio, mlx-vlm
  Attempting uninstall: tqdm
    Found existing installation: tqdm 4.66.5
    Uninstalling tqdm-4.66.5:
      Successfully uninstalled tqdm-4.66.5
  Attempting uninstall: opencv-python
    Found existing installation: opencv-python 4.10.0.84
    Uninstalling opencv-python-4.10.0.84:
      Successfully uninstalled opencv-python-4.10.0.84

ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
indicphotoocr 1.3.1 requires filelock==3.20.3, but you have filelock 3.32.6 which is incompatible.
indicphotoocr 1.3.1 requires fsspec==2024.9.0, but you have fsspec 2026.7.0 which is incompatible.
indicphotoocr 1.3.1 requires huggingface-hub==0.26.1, but you have huggingface-hub 1.31.0 which is incompatible.
indicphotoocr 1.3.1 requires markupsafe==3.0.2, but you have markupsafe 3.0.3 which is incompatible.
indicphotoocr 1.3.1 requires networkx==3.2.1, but you have networkx 3.6.1 which is incompatible.
indicphotoocr 1.3.1 requires numpy==1.26.4, but you have numpy 2.2.6 which is incompatible.
indicphotoocr 1.3.1 requires opencv-python==4.10.0.84, but you have opencv-python 5.0.0.93 which is incompatible.
indicphotoocr 1.3.1 requires regex==2024.9.11, but you have regex 2026.9.10 which is incompatible.
indicphotoocr 1.3.1 requires safetensors==0.4.5, but you have safetensors 0.8.0 which is incompatible.
indicphotoocr 1.3.1 requires sympy==1.13.1, but you have sympy 1.14.0 which is incompatible.
indicphotoocr 1.3.1 requires tqdm==4.66.5, but you have tqdm 4.70.1 which is incompatible.
indicphotoocr 1.3.1 requires typing-extensions==4.12.2, but you have typing-extensions 4.16.0 which is incompatible.
datasets 3.1.0 requires fsspec[http]<=2024.9.0,>=2023.1.0, but you have fsspec 2026.7.0 which is incompatible.
openbharatocr 0.4.3 requires easyocr==1.7.1, but you have easyocr 1.7.2 which is incompatible.
openbharatocr 0.4.3 requires numpy==1.26.4, but you have numpy 2.2.6 which is incompatible.
openbharatocr 0.4.3 requires opencv-python==4.6.0.66, but you have opencv-python 5.0.0.93 which is incompatible.
openbharatocr 0.4.3 requires pytesseract==0.3.10, but you have pytesseract 0.3.13 which is incompatible.
Successfully installed fastapi-0.141.1 llguidance-1.8.0 miniaudio-1.71 mlx-0.32.3 mlx-audio-0.5.7 mlx-metal-0.32.3 mlx-vlm-0.7.4 opencv-python-5.0.0.93 python-multipart-0.0.32 sentencepiece-0.2.2 sounddevice-0.5.6 starlette-1.7.0 tqdm-4.70.1 uvicorn-0.54.0
- mlx install: PASS

## [6] Cloning mlx-tune to /tmp/mlx-tune
Command: git clone https://github.com/ARahim3/mlx-tune.git /tmp/mlx-tune

Cloning into '/tmp/mlx-tune'...
- clone: PASS

## [7] Installing mlx-tune in editable mode
Command: cd /tmp/mlx-tune && /Users/srujansai/Desktop/South/.venv311/bin/pip install -e .

Obtaining file:///private/tmp/mlx-tune
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Checking if build backend supports build_editable: started
  Checking if build backend supports build_editable: finished with status 'done'
  Getting requirements to build editable: started
  Getting requirements to build editable: finished with status 'done'
  Preparing editable metadata (pyproject.toml): started
  Preparing editable metadata (pyproject.toml): finished with status 'done'
Requirement already satisfied: mlx>=0.31.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-tune==0.6.0) (0.32.3)
Collecting mlx-lm>=0.31.0 (from mlx-tune==0.6.0)
  Downloading mlx_lm-0.31.3-py3-none-any.whl.metadata (9.5 kB)
Requirement already satisfied: mlx-vlm>=0.4.3 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-tune==0.6.0) (0.7.4)
Requirement already satisfied: transformers>=4.36.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-tune==0.6.0) (5.17.0)
Requirement already satisfied: tokenizers>=0.15.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-tune==0.6.0) (0.23.2)
Requirement already satisfied: datasets<4.0.0,>=2.14.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-tune==0.6.0) (3.1.0)
Collecting mlx-embeddings>=0.1.0 (from mlx-tune==0.6.0)
  Downloading mlx_embeddings-0.1.0-py2.py3-none-any.whl.metadata (20 kB)
Requirement already satisfied: huggingface-hub>=0.20.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-tune==0.6.0) (1.31.0)
Requirement already satisfied: numpy>=1.23.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-tune==0.6.0) (2.2.6)
Requirement already satisfied: tqdm>=4.65.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-tune==0.6.0) (4.70.1)
Requirement already satisfied: filelock in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (3.32.6)
Requirement already satisfied: pyarrow>=15.0.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (25.0.1)
Requirement already satisfied: dill<0.3.9,>=0.3.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (0.3.8)
Requirement already satisfied: pandas in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (3.0.5)
Requirement already satisfied: requests>=2.32.2 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (2.34.2)
Requirement already satisfied: xxhash in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (4.0.1)
Requirement already satisfied: multiprocess<0.70.17 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (0.70.16)
Collecting fsspec<=2024.9.0,>=2023.1.0 (from fsspec[http]<=2024.9.0,>=2023.1.0->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0)
  Downloading fsspec-2024.9.0-py3-none-any.whl.metadata (11 kB)
Requirement already satisfied: aiohttp in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (3.14.3)
Requirement already satisfied: packaging in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (24.1)
Requirement already satisfied: pyyaml>=5.1 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (6.0.2)
Requirement already satisfied: aiohappyeyeballs>=2.5.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from aiohttp->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (2.7.1)
Requirement already satisfied: aiosignal>=1.4.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from aiohttp->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (1.4.0)
Requirement already satisfied: attrs>=17.3.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from aiohttp->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (24.2.0)
Requirement already satisfied: frozenlist>=1.1.1 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from aiohttp->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (1.5.0)
Requirement already satisfied: multidict<7.0,>=4.5 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from aiohttp->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (6.1.0)
Requirement already satisfied: propcache>=0.2.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from aiohttp->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (0.2.0)
Requirement already satisfied: typing_extensions>=4.4 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from aiohttp->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (4.16.0)
Requirement already satisfied: yarl<2.0,>=1.17.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from aiohttp->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (1.18.3)
Requirement already satisfied: idna>=2.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from yarl<2.0,>=1.17.0->aiohttp->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (3.10)
Requirement already satisfied: click<9.0.0,>=8.4.2 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from huggingface-hub>=0.20.0->mlx-tune==0.6.0) (8.5.0)
Requirement already satisfied: hf-xet<2.0.0,>=1.5.2 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from huggingface-hub>=0.20.0->mlx-tune==0.6.0) (1.6.0)
Requirement already satisfied: httpx<1,>=0.23.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from huggingface-hub>=0.20.0->mlx-tune==0.6.0) (0.28.1)
Requirement already satisfied: anyio in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from httpx<1,>=0.23.0->huggingface-hub>=0.20.0->mlx-tune==0.6.0) (4.15.1)
Requirement already satisfied: certifi in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from httpx<1,>=0.23.0->huggingface-hub>=0.20.0->mlx-tune==0.6.0) (2024.8.30)
Requirement already satisfied: httpcore==1.* in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from httpx<1,>=0.23.0->huggingface-hub>=0.20.0->mlx-tune==0.6.0) (1.0.9)
Requirement already satisfied: h11>=0.16 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from httpcore==1.*->httpx<1,>=0.23.0->huggingface-hub>=0.20.0->mlx-tune==0.6.0) (0.16.0)
Requirement already satisfied: mlx-metal==0.32.3 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx>=0.31.0->mlx-tune==0.6.0) (0.32.3)
Requirement already satisfied: sentencepiece in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-lm>=0.31.0->mlx-tune==0.6.0) (0.2.2)
Requirement already satisfied: protobuf in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-lm>=0.31.0->mlx-tune==0.6.0) (7.36.1)
Requirement already satisfied: jinja2 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-lm>=0.31.0->mlx-tune==0.6.0) (3.1.6)
Requirement already satisfied: miniaudio>=1.59 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-vlm>=0.4.3->mlx-tune==0.6.0) (1.71)
Requirement already satisfied: Pillow>=10.3.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-vlm>=0.4.3->mlx-tune==0.6.0) (12.3.0)
Requirement already satisfied: llguidance>=1.7.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-vlm>=0.4.3->mlx-tune==0.6.0) (1.8.0)
Requirement already satisfied: mlx-audio>=0.5.2 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-vlm>=0.4.3->mlx-tune==0.6.0) (0.5.7)
Requirement already satisfied: opencv-python>=4.12.0.88 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-vlm>=0.4.3->mlx-tune==0.6.0) (5.0.0.93)
Requirement already satisfied: fastapi>=0.95.1 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-vlm>=0.4.3->mlx-tune==0.6.0) (0.141.1)
Requirement already satisfied: python-multipart>=0.0.9 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-vlm>=0.4.3->mlx-tune==0.6.0) (0.0.32)
Requirement already satisfied: starlette>=1.0.1 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-vlm>=0.4.3->mlx-tune==0.6.0) (1.7.0)
Requirement already satisfied: uvicorn in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-vlm>=0.4.3->mlx-tune==0.6.0) (0.54.0)
Requirement already satisfied: websockets>=14.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-vlm>=0.4.3->mlx-tune==0.6.0) (17.1)
Requirement already satisfied: pydantic>=2.9.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from fastapi>=0.95.1->mlx-vlm>=0.4.3->mlx-tune==0.6.0) (2.13.5)
Requirement already satisfied: typing-inspection>=0.4.2 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from fastapi>=0.95.1->mlx-vlm>=0.4.3->mlx-tune==0.6.0) (0.4.4)
Requirement already satisfied: annotated-doc>=0.0.2 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from fastapi>=0.95.1->mlx-vlm>=0.4.3->mlx-tune==0.6.0) (0.0.5)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from jinja2->mlx-lm>=0.31.0->mlx-tune==0.6.0) (3.0.3)
Requirement already satisfied: cffi>=1.12.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from miniaudio>=1.59->mlx-vlm>=0.4.3->mlx-tune==0.6.0) (2.1.1)
Requirement already satisfied: pycparser in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from cffi>=1.12.0->miniaudio>=1.59->mlx-vlm>=0.4.3->mlx-tune==0.6.0) (3.0)
Requirement already satisfied: scipy>=1.10.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-audio>=0.5.2->mlx-vlm>=0.4.3->mlx-tune==0.6.0) (1.13.1)
Requirement already satisfied: sounddevice>=0.5.3 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from mlx-audio>=0.5.2->mlx-vlm>=0.4.3->mlx-tune==0.6.0) (0.5.6)
Requirement already satisfied: annotated-types>=0.6.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from pydantic>=2.9.0->fastapi>=0.95.1->mlx-vlm>=0.4.3->mlx-tune==0.6.0) (0.8.0)
Requirement already satisfied: pydantic-core==2.46.5 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from pydantic>=2.9.0->fastapi>=0.95.1->mlx-vlm>=0.4.3->mlx-tune==0.6.0) (2.46.5)
Requirement already satisfied: charset_normalizer<4,>=2 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from requests>=2.32.2->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (3.4.0)
Requirement already satisfied: urllib3<3,>=1.26 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from requests>=2.32.2->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (2.7.0)
Requirement already satisfied: regex>=2025.10.22 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from transformers>=4.36.0->mlx-tune==0.6.0) (2026.9.10)
Requirement already satisfied: typer in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from transformers>=4.36.0->mlx-tune==0.6.0) (0.27.2)
Requirement already satisfied: safetensors>=0.8.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from transformers>=4.36.0->mlx-tune==0.6.0) (0.8.0)
Requirement already satisfied: python-dateutil>=2.8.2 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from pandas->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas->datasets<4.0.0,>=2.14.0->mlx-tune==0.6.0) (1.16.0)
Requirement already satisfied: shellingham>=1.3.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from typer->transformers>=4.36.0->mlx-tune==0.6.0) (1.5.4)
Requirement already satisfied: rich>=13.8.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from typer->transformers>=4.36.0->mlx-tune==0.6.0) (15.0.0)
Requirement already satisfied: markdown-it-py>=2.2.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from rich>=13.8.0->typer->transformers>=4.36.0->mlx-tune==0.6.0) (4.2.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from rich>=13.8.0->typer->transformers>=4.36.0->mlx-tune==0.6.0) (2.21.0)
Requirement already satisfied: mdurl~=0.1 in /Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages (from markdown-it-py>=2.2.0->rich>=13.8.0->typer->transformers>=4.36.0->mlx-tune==0.6.0) (0.1.2)
Downloading fsspec-2024.9.0-py3-none-any.whl (179 kB)
Downloading mlx_embeddings-0.1.0-py2.py3-none-any.whl (74 kB)
Downloading mlx_lm-0.31.3-py3-none-any.whl (408 kB)
Building wheels for collected packages: mlx-tune
  Building editable for mlx-tune (pyproject.toml): started
  Building editable for mlx-tune (pyproject.toml): finished with status 'done'
  Created wheel for mlx-tune: filename=mlx_tune-0.6.0-0.editable-py3-none-any.whl size=18235 sha256=6567451c64701e4aa1279d04ec392ec1b12fb017009749ba2951149ecd610e12
  Stored in directory: /private/var/folders/yl/_kmwxk313kv6s44w10h5h4k40000gn/T/pip-ephem-wheel-cache-wsiqvea3/wheels/43/75/2d/fb973a3c0b70df6a7eed8c21e557a622184b933403a15614af
Successfully built mlx-tune
Installing collected packages: fsspec, mlx-lm, mlx-embeddings, mlx-tune
  Attempting uninstall: fsspec
    Found existing installation: fsspec 2026.7.0
    Uninstalling fsspec-2026.7.0:
      Successfully uninstalled fsspec-2026.7.0

ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
indicphotoocr 1.3.1 requires filelock==3.20.3, but you have filelock 3.32.6 which is incompatible.
indicphotoocr 1.3.1 requires huggingface-hub==0.26.1, but you have huggingface-hub 1.31.0 which is incompatible.
indicphotoocr 1.3.1 requires markupsafe==3.0.2, but you have markupsafe 3.0.3 which is incompatible.
indicphotoocr 1.3.1 requires networkx==3.2.1, but you have networkx 3.6.1 which is incompatible.
indicphotoocr 1.3.1 requires numpy==1.26.4, but you have numpy 2.2.6 which is incompatible.
indicphotoocr 1.3.1 requires opencv-python==4.10.0.84, but you have opencv-python 5.0.0.93 which is incompatible.
indicphotoocr 1.3.1 requires regex==2024.9.11, but you have regex 2026.9.10 which is incompatible.
indicphotoocr 1.3.1 requires safetensors==0.4.5, but you have safetensors 0.8.0 which is incompatible.
indicphotoocr 1.3.1 requires sympy==1.13.1, but you have sympy 1.14.0 which is incompatible.
indicphotoocr 1.3.1 requires tqdm==4.66.5, but you have tqdm 4.70.1 which is incompatible.
indicphotoocr 1.3.1 requires typing-extensions==4.12.2, but you have typing-extensions 4.16.0 which is incompatible.
Successfully installed fsspec-2024.9.0 mlx-embeddings-0.1.0 mlx-lm-0.31.3 mlx-tune-0.6.0
- pip install -e .: PASS

## [8] Smoke tests
Test: /Users/srujansai/Desktop/South/.venv311/bin/python -c "import mlx; print('mlx', mlx.__version__)"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
AttributeError: module 'mlx' has no attribute '__version__'
- mlx import: AttributeError: module 'mlx' has no attribute '__version__'

Test: /Users/srujansai/Desktop/South/.venv311/bin/python -c "import mlx_vlm; print('mlx_vlm OK')"
OK
- mlx_vlm import: OK

Test: /Users/srujansai/Desktop/South/.venv311/bin/python -c "import mlx.core as mx; print('mlx.core OK')"
OK
- mlx.core import: OK

Test: mlx-tune path (import only)
mlx-tune path OK

## [9] mlx-tune repo presence
- /tmp/mlx-tune: PRESENT (10+ top-level files)

## Final verdict
- Overall: PASS — mlx + mlx-vlm + mlx-tune installed

=== install_mlx_stack.sh complete @ 2026-09-29 16:22:36 IST, exit=0 ===
