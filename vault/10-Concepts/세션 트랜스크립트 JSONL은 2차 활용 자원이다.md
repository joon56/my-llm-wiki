---
title: 세션 트랜스크립트 JSONL은 2차 활용 자원이다
tags:
  - tool/claude-code
  - llm/agents
  - dev/tooling
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Session-Transcript-JSONL-Is-a-Reusable-Asset
created: 2026-08-04
sources:
  - "[[2026-07-14 agentmemory라는 skill 사용법 알려줘 (f2bdfc8c)]]"
  - "[[2026-11-06 ide_opened_fileThe user opened the file cUsersUSERDesktop모프 (bff996c4)]]"
---

## 한 줄 요약

Claude Code가 `~/.claude/projects/` 아래에 남기는 세션 JSONL은 단순 로그가 아니라 대량 임포트·크로스 프로젝트 검색·위키 증류가 가능한 원자재다.

## 내용

- Claude Code는 모든 세션을 `~/.claude/projects/<project-dir>/` 아래 JSONL 파일로 기록함 — 프롬프트, 응답, 도구 호출이 전부 구조화되어 남음. 단, 영구 보존은 아님: 시작할 때 마지막 활동이 `cleanupPeriodDays`(기본 30일)보다 오래된 트랜스크립트를 삭제함.
- 대량 임포트: agentmemory의 `import-jsonl`로 세션 14개 / 관찰 2063건을 한 번에 흡수해 검색 가능한 장기 기억으로 전환.
- 크로스 프로젝트 검색: 하이브리드 리콜(BM25 + 벡터 + 그래프)로 다른 프로젝트에서 썼던 과거 프롬프트를 현재 프로젝트에서 끌어올 수 있었음.
- 위키 증류: 같은 JSONL이 이 위키의 `90-Archive/` → `10-Concepts/` 증류 파이프라인의 입력이기도 함.
- 관점 전환: 트랜스크립트를 "지나간 대화 기록"이 아니라 "구조화된 데이터셋"으로 취급하면 재활용 경로가 여러 개 열림.
- 주의: 원본 JSONL은 기간이 지나면 지워지지만, 그 전에 만든 사본(아카이브 노트, 메모리 임포트, 백업)은 남음. 채팅에 붙여넣은 것(토큰, 개인정보 포함)은 여전히 영구 기록으로 취급하고, 민감한 값은 애초에 붙여넣지 않는 게 안전.
- 보존 기간은 실제 손실로 이어졌다: 2026-11-21에 남은 트랜스크립트는 17개뿐이었고, 가장 오래된 것의 마지막 활동은 10-26이었다. 아카이브 훅이 고장 나 수집하지 못한 약 10-05~10-21 세션은 영구 소실됐다([[fire-and-forget 훅은 침묵 실패한다]]). 2차 활용하려면 보존 기간 안에 수집하거나 `cleanupPeriodDays`를 늘린다 — 이 환경은 90으로 올렸다.
- 읽기용으로 변환할 때 role 필드를 그대로 믿지 않는다: AskUserQuestion으로 받은 사용자 답변은 tool_result 안에 있어서, '사용자 메시지'만 뽑으면 결정 근거가 통째로 빠진다. 반대로 백그라운드 작업 완료 알림(task-notification)과 컨텍스트 압축 요약("This session is being continued…")은 user 역할로 기록돼 사용자 발화로 잘못 분류된다(이 위키의 변환 로그에도 사용자 발화로 찍혀 있었다) — 추출·통계 전에 걸러야 한다.
- 호출 한도가 있는 도구 응답의 회수 창고로도 쓴다: Figma MCP 읽기가 월 약 20회(보기 좌석)라 다시 부를 수 없어서, JSONL의 tool_result(너무 커서 별도 파일로 빠진 결과 포함)에서 디자인 코드를 스크립트로 뽑아 `data-node-id`로 화면을 식별해 저장했다. 모델이 큰 응답을 다시 옮겨 적지 않고 화면 13개·아이콘 55개를 확보했고, 7일 뒤 만료되는 에셋 URL은 즉시 내려받았다.

## 출처

- [[2026-07-14 agentmemory라는 skill 사용법 알려줘 (f2bdfc8c)]]
- [[2026-11-06 ide_opened_fileThe user opened the file cUsersUSERDesktop모프 (bff996c4)]]
- 관련: [[문서에 없는 기능은 설치된 소스를 grep해서 찾는다]]
