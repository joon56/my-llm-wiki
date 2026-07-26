# 이 볼트에 대하여

Obsidian 기반 개인 LLM 위키. 모든 파일은 마크다운. Quartz 4로 공개 발행됨.

## 규칙
- 링크는 `[[노트 제목]]` 위키링크만 사용. 마크다운 링크 금지.
- 모든 새 노트는 YAML 프로퍼티 필수: title, tags, status, created
- status 값: raw | triaged | distilled
- **publish: true 인 노트만 웹에 발행됨. 기본값은 미발행.** 발행 플래그는 사용자만 결정.
- 노트 제목은 명제나 개념으로. 날짜/로그 형식 제목 금지.
- 한 노트 = 한 개념. 길어지면 쪼개고 링크로 연결.
- `90-Archive/` 는 자동 생성물. 수정 금지. 읽기만. 발행 절대 금지.
- 태그는 계층형: `llm/rag`, `llm/finetuning`, `tool/claude-code`
- 새 노트는 `_templates/` 형식을 따름.

## 자주 쓰는 작업
- 정제(/distill): 90-Archive 로그 → 10-Concepts 개념 노트로 승격
- MOC 갱신: 50-MOC/*.md 의 링크 목록 최신화
