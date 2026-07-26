#!/usr/bin/env python3
"""볼트 비밀정보 스캔. HIGH 발견 시 exit 1 (CI 게이트 겸용).

사용:  python scripts/secret_scan.py vault [다른경로...]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

PATTERNS: list[tuple[str, str, re.Pattern]] = [
    ("HIGH", "anthropic-key", re.compile(r"sk-ant-[A-Za-z0-9_-]{10,}")),
    ("HIGH", "openai-key", re.compile(r"sk-[A-Za-z0-9]{20}T3BlbkFJ[A-Za-z0-9]{20}")),
    ("HIGH", "aws-access-key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("HIGH", "github-token", re.compile(r"gh[pousr]_[A-Za-z0-9]{36,}")),
    ("HIGH", "private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("MEDIUM", "bearer-token", re.compile(r"Bearer\s+[A-Za-z0-9._\-]{20,}")),
    ("MEDIUM", "generic-secret",
     re.compile(r"(?i)(?:api[_-]?key|secret|password|token)\s*[:=]\s*[\"'][^\"']{12,}[\"']")),
]

SCAN_EXT = {".md", ".txt", ".json", ".yaml", ".yml"}
SKIP_DIRS = {".git", ".obsidian", "node_modules", "__pycache__"}


def _mask(s: str) -> str:
    return s[:8] + "…"


def scan_paths(paths: list[Path]) -> list[tuple[str, str, Path, int, str]]:
    findings = []
    for root in paths:
        files = [root] if root.is_file() else sorted(
            p for p in root.rglob("*")
            if p.is_file() and p.suffix.lower() in SCAN_EXT
            and not (SKIP_DIRS & set(p.parts))
        )
        for f in files:
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for i, line in enumerate(text.splitlines(), 1):
                for sev, rule, rx in PATTERNS:
                    m = rx.search(line)
                    if m:
                        findings.append((sev, rule, f, i, _mask(m.group(0))))
    return findings


def main() -> int:
    targets = [Path(a) for a in sys.argv[1:]] or [Path("vault")]
    findings = scan_paths(targets)
    high = [f for f in findings if f[0] == "HIGH"]
    for sev, rule, f, line, masked in findings:
        print(f"[{sev}] {rule}  {f}:{line}  {masked}")
    print(f"\n스캔 완료: HIGH {len(high)}건, MEDIUM {len(findings) - len(high)}건")
    if high:
        print("HIGH 발견 — 해당 키를 폐기(rotate)하고 노트에서 제거하세요. 배포 차단됨.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
