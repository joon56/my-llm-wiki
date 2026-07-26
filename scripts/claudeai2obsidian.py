#!/usr/bin/env python3
"""claudeai2obsidian.py — claude.ai 데이터 내보내기(conversations.json)를 Obsidian 노트로 변환.

데스크톱 앱/웹의 설정 → 개인정보 → 데이터 내보내기로 받은 zip(또는 그 안의
conversations.json)을 vault/90-Archive/claudeai/ 아래 세션 노트 형식으로 변환한다.

- export는 항상 전체 대화 누적본이므로, 이미 변환된 대화(UUID 기준)는 건너뛴다.
- 포맷은 비공식 — cc2obsidian.py와 같은 방어적 파싱(모르는 필드 무시).

사용:
    py scripts/claudeai2obsidian.py _dropbox/data-2026-07-26.zip --out vault/90-Archive/claudeai
    py scripts/claudeai2obsidian.py _dropbox/conversations.json --out vault/90-Archive/claudeai --dry-run
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from datetime import datetime
from pathlib import Path

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

INVALID_FILENAME = re.compile(r'[\\/:*?"<>|#\[\]^]')


def sanitize(name: str, limit: int = 60) -> str:
    name = INVALID_FILENAME.sub("", name)
    name = re.sub(r"\s+", " ", name).strip(" .")
    return name[:limit].strip() or "untitled"


def to_date(ts: str | None) -> str:
    if not ts:
        return "unknown"
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone().strftime("%Y-%m-%d")
    except ValueError:
        return str(ts)[:10]


def yaml_escape(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def load_conversations(src: Path) -> list[dict]:
    """zip 또는 json에서 대화 목록 로드."""
    if src.suffix.lower() == ".zip":
        with zipfile.ZipFile(src) as z:
            names = [n for n in z.namelist() if n.endswith("conversations.json")]
            if not names:
                raise FileNotFoundError(f"{src.name} 안에 conversations.json 이 없습니다")
            data = json.loads(z.read(names[0]).decode("utf-8"))
    else:
        data = json.loads(src.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("conversations.json 최상위가 리스트가 아닙니다 (포맷 변경?)")
    return [c for c in data if isinstance(c, dict)]


def existing_uuids(out_root: Path) -> set[str]:
    """이미 변환된 노트의 session_id 수집 (중복 변환 방지)."""
    seen: set[str] = set()
    if not out_root.is_dir():
        return seen
    for p in out_root.rglob("*.md"):
        try:
            head = p.read_text(encoding="utf-8", errors="replace")[:600]
        except OSError:
            continue
        m = re.search(r"^session_id: (\S+)", head, re.M)
        if m:
            seen.add(m.group(1))
    return seen


def render_note(conv: dict, max_chars: int) -> str | None:
    uuid = str(conv.get("uuid", ""))
    title = (conv.get("name") or "").strip() or uuid[:8]
    created = to_date(conv.get("created_at"))
    msgs = [m for m in conv.get("chat_messages", []) if isinstance(m, dict)]
    n_human = sum(1 for m in msgs if m.get("sender") == "human")

    fm = [
        "---",
        f"title: {yaml_escape(re.sub(r'\\s+', ' ', title)[:80])}",
        "source: claude-ai",
        f"session_id: {uuid}",
        f"date: {created}",
        f"turns: {len(msgs)}",
        f"prompts: {n_human}",
        "status: raw",
        "tags:",
        "  - claude-ai/session",
        "---",
        "",
        f"# {title}",
        "",
        "> [!info] claude.ai 대화 원본입니다. 배운 것은 개념 노트로 옮기고, 여기엔 링크만 거세요.",
        "",
        "**정제 메모**",
        "- 핵심 교훈:: ",
        "- 관련 노트:: ",
        "",
        "---",
        "",
        "",
    ]

    body: list[str] = []
    used = 0
    truncated = False
    for m in msgs:
        text = (m.get("text") or "").strip()
        if not text:
            continue
        head = "## 🙋 나" if m.get("sender") == "human" else "### 🤖 Claude"
        piece = f"{head}\n\n{text}\n\n"
        if max_chars and used + len(piece) > max_chars:
            truncated = True
            break
        body.append(piece)
        used += len(piece)

    if not body:
        return None
    if truncated:
        body.append(f"\n> [!warning] 길이 제한({max_chars:,}자)으로 이후 내용이 잘렸습니다.\n")
    return "\n".join(fm) + "".join(body)


def convert(src: Path, out_root: Path, *, min_prompts: int = 2,
            max_chars: int = 40000, dry_run: bool = False) -> tuple[int, int]:
    """변환 실행. (변환 수, 건너뜀 수) 반환."""
    convs = load_conversations(src)
    seen = existing_uuids(out_root)
    written = skipped = 0

    for conv in convs:
        uuid = str(conv.get("uuid", ""))
        msgs = conv.get("chat_messages") or []
        n_human = sum(1 for m in msgs if isinstance(m, dict) and m.get("sender") == "human")
        if not uuid or uuid in seen or n_human < min_prompts:
            skipped += 1
            continue
        note = render_note(conv, max_chars)
        if note is None:
            skipped += 1
            continue
        title = (conv.get("name") or "").strip() or uuid[:8]
        fname = f"{to_date(conv.get('created_at'))} {sanitize(title)} ({uuid[:8]}).md"
        target = out_root / fname
        if dry_run:
            print(f"  → {fname}  [{len(msgs)} msgs]")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(note, encoding="utf-8")
        written += 1

    return written, skipped


def main() -> int:
    ap = argparse.ArgumentParser(description="claude.ai export → Obsidian 노트 변환")
    ap.add_argument("src", help="export zip 또는 conversations.json 경로")
    ap.add_argument("--out", default="vault/90-Archive/claudeai", help="출력 폴더")
    ap.add_argument("--min-prompts", type=int, default=2, help="발화 N개 미만 대화 제외 (기본 2)")
    ap.add_argument("--max-chars", type=int, default=40000, help="노트 최대 길이 (0=무제한)")
    ap.add_argument("--dry-run", action="store_true", help="쓰지 않고 목록만")
    args = ap.parse_args()

    src = Path(args.src)
    if not src.is_file():
        print(f"❌ 파일 없음: {src}", file=sys.stderr)
        return 1

    written, skipped = convert(src, Path(args.out), min_prompts=args.min_prompts,
                               max_chars=args.max_chars, dry_run=args.dry_run)
    print(f"\n✅ {written}개 변환, {skipped}개 건너뜀(중복/짧음)"
          + (" (dry-run)" if args.dry_run else f" → {args.out}"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
