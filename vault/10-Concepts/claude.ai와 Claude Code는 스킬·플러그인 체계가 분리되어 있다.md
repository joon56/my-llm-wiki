---
title: claude.ai와 Claude Code는 스킬·플러그인 체계가 분리되어 있다
tags:
  - tool/claude-code
  - tool/claude-ai
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/claude.ai-and-Claude-Code-Have-Separate-Skill-and-Plugin-Systems
created: 2026-07-26
sources:
  - "[[2026-07-15 로컬 Claude 코드 스킬 로드하기 (894f7060)]]"
  - "[[2026-07-03 Claude에서 caveman skill 사용하기 (cf5f7202)]]"
  - "[[2026-11-06 ide_opened_fileThe user opened the file cUsersUSERDesktop모프 (bff996c4)]]"
---

## 한 줄 요약

claude.ai(웹/데스크톱)와 로컬 Claude Code는 **완전히 분리된 샌드박스**다 — 한쪽에 설치한 스킬·플러그인은 다른 쪽에 자동 반영되지 않고, 설치 방법 자체가 다르며, 이식 가능 여부는 플러그인의 구성요소에 좌우된다.

## 내용

- **설치 체계가 별개**: Claude Code는 marketplace/`~/.claude` 기반 플러그인, claude.ai는 zip 업로드 방식 Skills. 같은 기능을 양쪽에서 쓰려면 각각 설치해야 함.
- **이식 가능 조건**: claude.ai Skills는 순수 `SKILL.md` 지침 텍스트만 지원 —
  - 이식 가능: 지침·체크리스트·문서형 스킬
  - 이식 불가: hooks(이벤트 훅), 로컬 MCP 서버, 서브에이전트, 로컬 스크립트에 의존하는 플러그인
- **로드 타이밍 함정**: Claude Code 플러그인/훅은 **세션 재시작 시점에만** 로드됨. 설치 직후 커맨드가 "unknown command"면 고장이 아니라 재시작 안 한 것 — 재시작부터 확인.
- 일반화: 같은 브랜드 제품군이라도 실행 환경이 다르면 확장 기능은 격리된 별개 시스템이라고 가정하는 게 안전.
- 예외: claude.ai 커넥터(MCP)는 Claude Code에 'claude.ai <이름>' 서버로 들어온다. 단 세션 도중에 연결하면 실행 중인 세션은 연결 전 도구 목록을 유지한다 — 새 터미널에서는 Connected인데 현재 세션은 호출하지 못했고, `/mcp`에서 해당 서버를 Reconnect하자 풀렸다(2회 재현).

## 출처

- [[2026-07-15 로컬 Claude 코드 스킬 로드하기 (894f7060)]]
- [[2026-07-03 Claude에서 caveman skill 사용하기 (cf5f7202)]]
- [[2026-11-06 ide_opened_fileThe user opened the file cUsersUSERDesktop모프 (bff996c4)]]
