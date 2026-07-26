---
title: Windows PowerShell 실행 정책이 npm 전역 CLI를 차단한다
tags:
  - tool/windows
  - tool/npm
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Windows-PowerShell-Execution-Policy-Blocks-npm-Global-CLIs
created: 2026-07-26
sources:
  - "[[2026-07-03 Claude에서 caveman skill 사용하기 (cf5f7202)]]"
---

## 한 줄 요약

npm 전역 설치한 CLI가 PowerShell에서 "이 시스템에서 스크립트를 실행할 수 없습니다"로 죽는 건 CLI 문제가 아니라 **PowerShell 기본 실행 정책(Restricted)이 npm의 `.ps1` 래퍼를 차단**하는 것 — `Set-ExecutionPolicy RemoteSigned` 또는 `.cmd` 직접 호출로 해결한다.

## 내용

- 구조: npm은 전역 CLI마다 세 가지 래퍼를 만든다 — `foo`(bash용), `foo.cmd`(cmd용), `foo.ps1`(PowerShell용). PowerShell에서 `foo`를 치면 `.ps1`이 우선 실행되는데, 기본 정책이 서명 없는 스크립트를 차단.
- 해법 1 (권장): 현재 사용자 범위로 정책 완화 —
  ```powershell
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
  로컬 스크립트는 허용, 인터넷에서 받은 서명 없는 스크립트만 차단. 관리자 권한 불필요.
- 해법 2 (일회성): `.cmd` 확장자로 직접 호출 — `foo.cmd ...`. 정책을 안 건드리고 우회.
- 진단 팁: `Get-ExecutionPolicy -List`로 스코프별 정책 확인. 에러 메시지에 `.ps1` 경로가 보이면 100% 이 문제.

## 출처

- [[2026-07-03 Claude에서 caveman skill 사용하기 (cf5f7202)]]
- 관련: [[파괴적 스크립트는 백업 생성 여부를 즉시 검증해야 한다]] (Windows 도구 체인 함정)
