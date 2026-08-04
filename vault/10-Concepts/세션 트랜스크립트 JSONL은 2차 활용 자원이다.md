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
---

## 한 줄 요약

Claude Code가 `~/.claude/projects/` 아래에 남기는 세션 JSONL은 단순 로그가 아니라 대량 임포트·크로스 프로젝트 검색·위키 증류가 가능한 원자재다.

## 내용

- Claude Code는 모든 세션을 `~/.claude/projects/<project-dir>/` 아래 JSONL 파일로 보존함 — 프롬프트, 응답, 도구 호출이 전부 구조화되어 남음.
- 대량 임포트: agentmemory의 `import-jsonl`로 세션 14개 / 관찰 2063건을 한 번에 흡수해 검색 가능한 장기 기억으로 전환.
- 크로스 프로젝트 검색: 하이브리드 리콜(BM25 + 벡터 + 그래프)로 다른 프로젝트에서 썼던 과거 프롬프트를 현재 프로젝트에서 끌어올 수 있었음.
- 위키 증류: 같은 JSONL이 이 위키의 `90-Archive/` → `10-Concepts/` 증류 파이프라인의 입력이기도 함.
- 관점 전환: 트랜스크립트를 "지나간 대화 기록"이 아니라 "구조화된 데이터셋"으로 취급하면 재활용 경로가 여러 개 열림.
- 주의: 채팅에 붙여넣은 모든 것(토큰, 개인정보 포함)이 JSONL에 영구히 남는다는 뜻이기도 하므로, 민감한 값은 애초에 붙여넣지 않는 게 안전.

## 출처

- [[2026-07-14 agentmemory라는 skill 사용법 알려줘 (f2bdfc8c)]]
- 관련: [[문서에 없는 기능은 설치된 소스를 grep해서 찾는다]]
