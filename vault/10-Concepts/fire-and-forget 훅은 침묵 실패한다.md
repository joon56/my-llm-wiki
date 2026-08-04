---
title: fire-and-forget 훅은 침묵 실패한다
tags:
  - tool/claude-code
  - dev/debugging
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Fire-and-Forget-Hooks-Fail-Silently
created: 2026-08-04
sources:
  - "[[2026-07-14 agentmemory라는 skill 사용법 알려줘 (f2bdfc8c)]]"
---

## 한 줄 요약

`fetch(url).catch(() => {})` 패턴으로 이벤트를 쏘는 fire-and-forget 훅은 수신자가 죽어 있으면 **모든 이벤트를 소리 없이 버린다** — 세션 0개 기록, 에러 0개 표시.

## 내용

- 실제 사례: agentmemory 훅들이 이벤트를 `fetch(url).catch(() => {})`로 POST하고 있었는데, 데몬이 내려가 있는 동안 모든 이벤트가 조용히 버려졌다. 기록된 세션 0개, 그런데 화면에 뜬 에러도 0개.
- 이때 실제로 쓰인 진단 체인(기록해 둘 가치가 있음): 포트 확인 → MCP는 응답하지만 데이터가 비어 있음 → 훅 소스 코드 읽기 → 해당 프로세스가 연결부(shim)일 뿐임을 발견 → 데몬 시작 로그 확인 → 바이너리 부재 확정.
- fire-and-forget의 트레이드오프: 이벤트 전송이 실패해도 에이전트 작업을 절대 막지 않는다는 장점이 있지만, 그 대가로 실패 신호가 완전히 사라진다.
- 따라서 fire-and-forget 파이프라인에는 **외부 헬스 신호가 반드시 별도로 필요**하다 — 예: 데몬 포트 체크, 주기적인 "최근 N분간 수집 건수 > 0" 확인.
- 일반화: `.catch(() => {})`가 들어간 코드는 "실패해도 괜찮은가"가 아니라 "실패를 어디서 알아챌 것인가"를 먼저 답해야 한다.

## 출처

- [[2026-07-14 agentmemory라는 skill 사용법 알려줘 (f2bdfc8c)]]
- 관련: [[자기 로그를 다루는 도구의 재귀 오염 함정]]
