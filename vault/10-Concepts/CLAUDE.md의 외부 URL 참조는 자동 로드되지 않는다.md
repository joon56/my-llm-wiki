---
title: CLAUDE.md의 외부 URL 참조는 자동 로드되지 않는다
tags:
  - tool/claude-code
status: distilled
publish: true
created: 2026-07-26
sources:
  - "[[2026-07-16 command-messageandrej-karpathy-skillskarpathy-guidelinescomm (bbe5b12c)]]"
---

## 한 줄 요약

CLAUDE.md에 "이 URL을 참고하라"고 링크를 적어도 Claude Code가 세션마다 자동으로 가져오지 않는다 — 매번 적용되길 원하는 규칙이라면 내용을 파일 안에 직접 인라인해야 한다.

## 내용

- CLAUDE.md는 세션 시작 시 **파일에 적힌 텍스트만** 컨텍스트에 들어간다. URL은 글자 그대로의 문자열일 뿐, 자동 fetch되지 않음.
- URL 내용이 실제로 반영되려면 에이전트가 매번 WebFetch를 호출해야 하는데, 이는 보장되지 않고 토큰·시간도 소모됨.
- 선택 기준:
  - **항상 적용될 규칙** → 내용을 CLAUDE.md에 인라인 (길면 요약해서)
  - **가끔 필요한 참고자료** → URL로 두되 "필요할 때 fetch하라"는 지시를 명시
- 스킬(skill) 파일, 에이전트 지침 파일 전반에 같은 원칙 적용 — 지침 파일에서 외부 링크는 기본적으로 죽은 참조라고 가정하는 게 안전.

## 출처

- [[2026-07-16 command-messageandrej-karpathy-skillskarpathy-guidelinescomm (bbe5b12c)]]
