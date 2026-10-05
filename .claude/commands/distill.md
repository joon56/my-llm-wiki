---
description: 주간 정제 — raw 세션 노트를 분류하고 개념 노트로 승격
---

vault/90-Archive/ 전체(claude-sessions/ 및 claudeai/)에서 status가 raw인 노트 중 최근 10개를 읽고 정제하라.

절차 (순서 엄수):
0. 누락 세션 자동 수집 (SessionEnd 훅이 침묵 실패해도 아카이브가 끊기지 않도록): `vault/90-Archive/claude-sessions/` 안 노트들의 가장 최근 `date:`를 기준일로 잡고 `py -X utf8 scripts/cc2obsidian.py --out vault/90-Archive/claude-sessions --since <기준일>`을 실행한다. triaged/distilled 노트는 변환기가 덮어쓰지 않고, raw 노트는 최신 내용으로 갱신된다. 새로 생긴 노트 개수를 보고한다 — 기준일 이후 세션이 있었는데 새 노트가 생겼다면 SessionEnd 훅이 실패 중이라는 뜻이니 함께 알린다.
1. 해당 노트 10개를 읽는다.
2. "재사용 가능한 교훈 유/무" 분류표만 먼저 제시한다 (한 줄 근거 포함). 이 단계에서 파일 생성 금지.
3. 교훈 없음 → 해당 노트의 프로퍼티만 `status: triaged`로 변경.
4. 교훈 있음 → 개념 노트 제목 후보를 3개씩 제안하고 사용자의 선택을 기다린다. 제목은 반드시 사용자가 확정한다.
5. 확정된 것만 `vault/10-Concepts/`에 `_templates/개념 노트.md` 형식으로 생성. `publish`는 항상 false로 두고 발행 여부는 사용자가 결정.
6. 원본 노트를 `status: distilled`로 바꾸고 `출처::` 역링크를 남긴다.
7. 사용자가 발행(`publish: true`)을 승인한 노트는 **영어판도 함께 생성한다**: `vault/en/` 미러 경로에 영어 파일명으로 번역본을 만들고, 양쪽 frontmatter에 `lang` + `translation`(상대 슬러그) 짝을 연결한다. 영어판도 `publish: true`. `vault/en/50-MOC/LLM MOC (EN).md`에도 링크를 추가한다. 한국어 MOC 갱신도 잊지 말 것.

제약: 한 번에 개념 노트 5개 초과 생성 금지. vault/CLAUDE.md 규칙 준수.
