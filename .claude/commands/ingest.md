---
description: _dropbox의 claude.ai export를 아카이브로 변환하고 반입함을 비운다
---

`_dropbox/`에 있는 claude.ai 데이터 내보내기 파일을 변환하라.

절차:
1. `_dropbox/`에서 `*.zip`과 `*.json` 파일을 찾는다 (README.md 제외). 없으면 "반입함이 비어 있음"을 보고하고 종료.
2. 각 파일에 대해 먼저 dry-run: `py scripts/claudeai2obsidian.py <파일> --out vault/90-Archive/claudeai --dry-run` — 변환 대상 개수를 사용자에게 보고.
3. 실제 변환 실행 (dry-run 플래그 제거). 에러가 나면 해당 파일은 삭제하지 말고 에러를 그대로 보고.
4. `py scripts/secret_scan.py vault` 실행 — HIGH 발견 시 보고하고 중단 (아카이브는 로컬 전용이지만 습관 유지).
5. **성공적으로 변환된 원본 파일만** `_dropbox/`에서 삭제한다 (README.md는 유지).
6. 결과 요약: 변환 N개 / 중복 건너뜀 M개 / 반입함 상태. `/distill`로 정제 가능함을 안내.

제약: `_dropbox/` 밖의 파일을 삭제하지 않는다. 변환 실패한 파일은 보존한다.
