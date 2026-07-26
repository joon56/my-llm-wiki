#!/usr/bin/env python3
"""SessionEnd 훅: 끝난 세션을 볼트 90-Archive에 md로 아카이브.

stdin으로 훅 페이로드 JSON(transcript_path 포함)을 받는다.
어떤 경우에도 exit 0 — 세션 종료를 절대 블로킹하지 않는다(best-effort).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cc2obsidian import convert_one  # noqa: E402

DEFAULT_OUT = Path(__file__).resolve().parents[1] / "vault" / "90-Archive" / "claude-sessions"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    args = ap.parse_args()
    out_root = Path(args.out)
    try:
        payload = json.load(sys.stdin)
        tp = payload.get("transcript_path")
        if tp and Path(tp).is_file():
            convert_one(Path(tp), out_root, min_prompts=2)
    except Exception as e:  # noqa: BLE001 — 훅은 무조건 성공 종료
        try:
            out_root.mkdir(parents=True, exist_ok=True)
            with (out_root / "_hook-errors.log").open("a", encoding="utf-8") as f:
                f.write(f"{e!r}\n")
        except OSError:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
