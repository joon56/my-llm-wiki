#!/usr/bin/env python3
"""
cc2obsidian.py — Claude Code 세션 로그(JSONL)를 Obsidian 노트(.md)로 변환합니다.

Claude Code는 세션을 ~/.claude/projects/<project>/<session-id>.jsonl 에 저장합니다.
공식 문서 기준으로 이 JSONL의 "내부 포맷은 버전마다 바뀔 수 있으므로",
이 스크립트는 방어적으로 파싱합니다(모르는 필드는 무시). 깨지면 --debug 로 확인하세요.

사용 예:
    python3 cc2obsidian.py --out ~/vault/90-Archive/claude-sessions --dry-run
    python3 cc2obsidian.py --out ~/vault/90-Archive/claude-sessions --since 2026-01-01
    python3 cc2obsidian.py --out ~/vault/90-Archive/claude-sessions --project my-app --index
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------------
# 파싱 유틸
# ---------------------------------------------------------------------------

INVALID_FILENAME = re.compile(r'[\\/:*?"<>|#\[\]^]')


def sanitize(name: str, limit: int = 60) -> str:
    """Obsidian 파일명으로 안전한 문자열로 정리."""
    name = INVALID_FILENAME.sub("", name)
    name = re.sub(r"\s+", " ", name).strip(" .")
    return name[:limit].strip() or "untitled"


def iter_entries(path: Path, debug: bool = False):
    """JSONL 한 줄씩 dict로. 깨진 줄은 건너뜀."""
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                if debug:
                    print(f"  [skip] {path.name}:{i} {e}", file=sys.stderr)
                continue
            if isinstance(obj, dict):
                yield obj


def blocks_of(entry: dict) -> list:
    """message.content 를 항상 리스트로 정규화."""
    msg = entry.get("message")
    if not isinstance(msg, dict):
        return []
    content = msg.get("content")
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    if isinstance(content, list):
        return [b for b in content if isinstance(b, dict)]
    return []


def render_tool_use(block: dict) -> str:
    """도구 호출을 한 줄 요약으로. 전체 입력은 노이즈라 잘라냄."""
    name = block.get("name", "tool")
    inp = block.get("input") or {}
    hint = ""
    if isinstance(inp, dict):
        for key in ("command", "file_path", "path", "pattern", "query", "description"):
            if key in inp and isinstance(inp[key], str):
                hint = inp[key].replace("\n", " ")[:120]
                break
    return f"- 🔧 `{name}`" + (f" — `{hint}`" if hint else "")


def parse_session(path: Path, debug: bool = False) -> dict | None:
    """세션 파일 하나를 구조화된 dict로."""
    turns: list[dict] = []
    summary = None
    session_id = path.stem
    cwd = None
    first_ts = last_ts = None
    tool_names: set[str] = set()

    for entry in iter_entries(path, debug):
        etype = entry.get("type")

        if etype == "summary" and isinstance(entry.get("summary"), str):
            summary = entry["summary"].strip()
            continue

        # 서브에이전트/내부 메타 항목은 본문에서 제외
        if entry.get("isSidechain") or entry.get("isMeta"):
            continue
        if etype not in ("user", "assistant"):
            continue

        cwd = entry.get("cwd") or cwd
        ts = entry.get("timestamp")
        if isinstance(ts, str):
            first_ts = first_ts or ts
            last_ts = ts

        texts: list[str] = []
        tools: list[str] = []
        only_tool_result = True

        for b in blocks_of(entry):
            btype = b.get("type")
            if btype == "text":
                t = (b.get("text") or "").strip()
                if t:
                    texts.append(t)
                    only_tool_result = False
            elif btype == "thinking":
                only_tool_result = False  # 사고 내용은 저장하지 않음
            elif btype == "tool_use":
                tools.append(render_tool_use(b))
                tool_names.add(str(b.get("name", "")))
                only_tool_result = False
            elif btype == "tool_result":
                pass  # 도구 결과 원문은 너무 길어서 제외

        # 도구 결과만 담긴 user 턴은 실제 발화가 아니므로 스킵
        if etype == "user" and only_tool_result and not texts:
            continue
        if not texts and not tools:
            continue

        turns.append({"role": etype, "texts": texts, "tools": tools, "ts": ts})

    if not turns:
        return None

    prompts = [t for t in turns if t["role"] == "user"]
    title = summary or (prompts[0]["texts"][0] if prompts and prompts[0]["texts"] else session_id)
    title = re.sub(r"\s+", " ", title.strip())[:80]

    return {
        "session_id": session_id,
        "title": title,
        "summary": summary,
        "cwd": cwd,
        "project": Path(cwd).name if cwd else path.parent.name,
        "first_ts": first_ts,
        "last_ts": last_ts,
        "turns": turns,
        "n_user": len(prompts),
        "n_turns": len(turns),
        "tools": sorted(t for t in tool_names if t),
        "size": path.stat().st_size,
        "source_path": str(path),
    }


# ---------------------------------------------------------------------------
# 노트 생성
# ---------------------------------------------------------------------------

def to_date(ts: str | None) -> str:
    if not ts:
        return "unknown"
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone().strftime("%Y-%m-%d")
    except ValueError:
        return ts[:10]


def yaml_escape(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def render_note(sess: dict, max_chars: int) -> str:
    date = to_date(sess["first_ts"])
    project = sess["project"] or "unknown"

    fm = [
        "---",
        f"title: {yaml_escape(sess['title'])}",
        "source: claude-code",
        f"session_id: {sess['session_id']}",
        f"project: {yaml_escape(project)}",
        f"cwd: {yaml_escape(sess['cwd'] or '')}",
        f"date: {date}",
        f"turns: {sess['n_turns']}",
        f"prompts: {sess['n_user']}",
        f"tools: [{', '.join(sess['tools'])}]",
        "status: raw",  # raw → triaged → distilled 로 직접 승격
        "tags:",
        "  - claude-code/session",
        f"  - project/{re.sub(r'[^a-zA-Z0-9_-]', '-', project).lower()}",
        "---",
        "",
        f"# {sess['title']}",
        "",
        "> [!info] 원본 세션 로그입니다. 여기서 배운 것은 별도 노트로 옮기고, 이 노트에서는 링크만 거세요.",
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

    for turn in sess["turns"]:
        head = "## 🙋 나" if turn["role"] == "user" else "### 🤖 Claude"
        chunk = [head, ""]
        for t in turn["texts"]:
            chunk.append(t)
            chunk.append("")
        if turn["tools"]:
            chunk.extend(turn["tools"])
            chunk.append("")
        piece = "\n".join(chunk)

        if max_chars and used + len(piece) > max_chars:
            truncated = True
            break
        body.append(piece)
        used += len(piece)

    if truncated:
        body.append(f"\n> [!warning] 길이 제한({max_chars:,}자)으로 이후 내용이 잘렸습니다. "
                    f"원본: `{sess['source_path']}`\n")

    return "\n".join(fm) + "\n".join(body) + "\n"


def note_target(sess: dict, out_root: Path) -> Path:
    """세션 dict → 노트 파일 경로 (프로젝트 하위폴더/날짜 제목 (id8).md)"""
    date = to_date(sess["first_ts"])
    fname = f"{date} {sanitize(sess['title'])} ({sess['session_id'][:8]}).md"
    return Path(out_root) / sanitize(sess["project"] or "unknown", 40) / fname


def is_curated(note: Path) -> bool:
    """Existing note whose status moved past raw (triaged/distilled) — never overwrite it."""
    if not note.is_file():
        return False
    head = note.read_text(encoding="utf-8").split("\n---", 1)[0]
    return any(line.startswith("status:") and line.split(":", 1)[1].strip() != "raw"
               for line in head.splitlines())


def convert_one(jsonl_path: Path, out_root: Path,
                max_chars: int = 40000, min_prompts: int = 1) -> Path | None:
    """단일 세션 변환. 훅(archive_session.py)에서 사용. 조건 미달 또는 정제된 노트면 None."""
    sess = parse_session(Path(jsonl_path))
    if not sess or sess["n_user"] < min_prompts:
        return None
    target = note_target(sess, Path(out_root))
    if is_curated(target):
        return None
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_note(sess, max_chars), encoding="utf-8")
    return target


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Claude Code 세션 → Obsidian 노트 변환")
    ap.add_argument("--src", default=str(Path.home() / ".claude" / "projects"),
                    help="Claude Code projects 디렉터리 (기본: ~/.claude/projects)")
    ap.add_argument("--out", required=True, help="노트를 저장할 Obsidian 볼트 내 폴더")
    ap.add_argument("--since", help="YYYY-MM-DD 이후 세션만")
    ap.add_argument("--project", help="프로젝트 이름 부분 일치 필터")
    ap.add_argument("--min-prompts", type=int, default=2,
                    help="사용자 발화가 N개 미만인 세션은 제외 (기본 2)")
    ap.add_argument("--max-chars", type=int, default=40000,
                    help="노트 하나의 본문 최대 길이 (0=무제한, 기본 40000)")
    ap.add_argument("--index", action="store_true", help="MOC 인덱스 노트도 생성")
    ap.add_argument("--dry-run", action="store_true", help="쓰지 않고 목록만 출력")
    ap.add_argument("--debug", action="store_true")
    args = ap.parse_args()

    src = Path(args.src).expanduser()
    if not src.is_dir():
        print(f"❌ 소스 디렉터리를 찾을 수 없습니다: {src}", file=sys.stderr)
        print("   CLAUDE_CONFIG_DIR 를 바꿨다면 --src 로 지정하세요.", file=sys.stderr)
        return 1

    out = Path(args.out).expanduser()

    # 최상위 .jsonl 만 (하위 <session-id>/subagents/ 는 제외)
    files = sorted(p for p in src.glob("*/*.jsonl") if p.is_file())
    if not files:
        print(f"⚠️  {src} 에서 .jsonl 파일을 찾지 못했습니다.", file=sys.stderr)
        return 1

    print(f"📂 세션 파일 {len(files)}개 발견")

    written, skipped = [], 0
    for path in files:
        try:
            sess = parse_session(path, args.debug)
        except Exception as e:  # noqa: BLE001 — 한 파일 때문에 전체가 죽지 않게
            print(f"  [error] {path.name}: {e}", file=sys.stderr)
            skipped += 1
            continue

        if not sess:
            skipped += 1
            continue
        if sess["n_user"] < args.min_prompts:
            skipped += 1
            continue
        if args.project and args.project.lower() not in (sess["project"] or "").lower():
            skipped += 1
            continue
        if args.since and to_date(sess["first_ts"]) < args.since:
            skipped += 1
            continue

        target = note_target(sess, out)
        if is_curated(target):
            skipped += 1
            continue

        if args.dry_run:
            print(f"  → {target.relative_to(out)}  [{sess['n_turns']} turns]")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(render_note(sess, args.max_chars), encoding="utf-8")
        written.append((sess, target))

    print(f"\n✅ {len(written)}개 변환, {skipped}개 건너뜀"
          + (" (dry-run: 실제로 쓰지 않음)" if args.dry_run else f" → {out}"))

    if args.index and written and not args.dry_run:
        lines = [
            "---",
            "title: Claude Code 세션 아카이브",
            "tags:",
            "  - moc",
            "  - claude-code/session",
            "---",
            "",
            "# Claude Code 세션 아카이브",
            "",
            f"자동 생성: {datetime.now(timezone.utc).astimezone():%Y-%m-%d %H:%M}  ·  총 {len(written)}건",
            "",
            "```dataview",
            "TABLE date, project, turns, status",
            'FROM #claude-code/session',
            "WHERE status = \"raw\"",
            "SORT date DESC",
            "```",
            "",
            "## 프로젝트별",
            "",
        ]
        by_project: dict[str, list] = {}
        for sess, target in written:
            by_project.setdefault(sess["project"] or "unknown", []).append((sess, target))
        for project in sorted(by_project):
            lines.append(f"### {project}")
            lines.append("")
            for sess, target in sorted(by_project[project],
                                       key=lambda x: to_date(x[0]["first_ts"]), reverse=True):
                lines.append(f"- `{to_date(sess['first_ts'])}` [[{target.stem}]]")
            lines.append("")
        (out / "00 Claude Code 세션 인덱스.md").write_text("\n".join(lines), encoding="utf-8")
        print("🗂  인덱스 노트 생성 완료")

    return 0


if __name__ == "__main__":
    sys.exit(main())
