---
title: 문서에 없는 기능은 설치된 소스를 grep해서 찾는다
tags:
  - tool/claude-code
  - dev/debugging
  - llm/agents
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Grep-Installed-Sources-for-Undocumented-APIs
created: 2026-08-04
sources:
  - "[[2026-07-14 agentmemory라는 skill 사용법 알려줘 (f2bdfc8c)]]"
  - "[[2026-11-06 ide_opened_fileThe user opened the file cUsersUSERDesktop모프 (bff996c4)]]"
---

## 한 줄 요약

로컬에 설치된 도구는 공식 문서가 아니라 설치된 코드 자체가 최종 문서다 — 문서에 없는 기능이 필요하면 `node_modules`의 소스를 grep해서 실제 엔드포인트를 찾아 쓰면 된다.

## 내용

- agentmemory에서 특정 세션의 기억을 지워야 했는데, 문서와 스킬 어디에도 세션 단위 삭제 방법이 없었음.
- 설치된 패키지 소스(`node_modules` 하위)를 grep으로 뒤져서 `POST /agentmemory/forget` 엔드포인트가 `{sessionId}`를 받는다는 것을 코드에서 직접 확인.
- 찾은 엔드포인트를 REST로 직접 호출해서 문서에 없는 세션 삭제를 완료 — 별도 CLI 명령이나 MCP 도구 없이 해결.
- 원칙: 로컬에 설치된 도구의 라우트 정의, 핸들러 시그니처는 코드에 그대로 있으므로, 문서 부재 = 기능 부재가 아니다.
- 탐색 순서: (1) 공식 문서/스킬 확인 → (2) 설치 경로에서 라우트·명령어 문자열 grep → (3) 시그니처 확인 후 직접 호출.
- 웹 서비스 API와 달리 로컬 도구는 소스가 손에 있으므로 이 방법이 항상 가능하고, 버전 불일치 걱정도 없음(지금 실행 중인 바로 그 코드를 읽는 것이므로).
- 두 번째 사례: Firebase CLI의 비대화형 로그인 링크가 몇 분 만에 "Unable to verify client"로 만료됐다. 설치된 firebase-tools 소스를 읽어 두 경로를 찾아 썼다 — `firebase login <인증코드>`가 설정 파일에 저장된 대기 세션(code verifier)을 이어받는 경로, 그리고 `lib/auth`의 `loginGoogle(true)`·`recordCredentials()`를 node로 직접 호출해 이 PC 브라우저 → localhost 콜백으로 코드 붙여넣기 없이 끝내는 경로. 찾은 재로그인 절차는 메모리에 기록했다.

## 출처

- [[2026-07-14 agentmemory라는 skill 사용법 알려줘 (f2bdfc8c)]]
- [[2026-11-06 ide_opened_fileThe user opened the file cUsersUSERDesktop모프 (bff996c4)]]
- 관련: [[세션 트랜스크립트 JSONL은 2차 활용 자원이다]]
