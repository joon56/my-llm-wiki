---
title: 서드파티 설치는 dry-run과 install-state 기준으로 다룬다
tags:
  - dev/tooling
  - tool/claude-code
  - dev/security
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Handle-Third-Party-Installs-via-Dry-Run-and-Install-State
created: 2026-08-04
sources:
  - "[[2026-07-15 claude-code-skills-guide.md 읽고, 지금 설치 안 된 taste-skill Matt P (4a82016f)]]"
---

## 한 줄 요약

서드파티 팩은 설치 전 `--dry-run`으로 계획을 검사하고, 제거할 때는 기록된 install-state를 유일한 진실로 삼는다 — 경로도 패키지명도 추측하지 않는다.

## 내용

- 618개 파일짜리 스킬 팩을 설치하기 전에 `--dry-run`으로 설치 계획을 먼저 출력해서 검토: 네임스페이스가 격리되는가? `settings.json`을 건드리지 않는가?
- dry-run에서 확인할 핵심 두 가지: (1) 파일이 어디에 쓰이는지(기존 파일 덮어쓰기 여부), (2) 전역 설정 파일 변경 여부.
- 제거는 설치 시 기록된 install-state(이 경우 603개 항목)를 기준으로 수행 — "아마 이 폴더에 깔렸겠지"라고 경로를 추측해서 지우면 남의 파일을 지우거나 잔재를 남김.
- 추측한 패키지명으로 명령을 실행하지 말 것: 실제 bin 이름은 해당 저장소의 `package.json`에서 확인한 뒤에만 실행. 오타 스쿼팅 패키지를 실행하는 사고를 원천 차단.
- 요약된 절차: repo의 package.json으로 bin 검증 → `--dry-run`으로 계획 검토 → 설치 → 제거 시 install-state만 신뢰.

## 출처

- [[2026-07-15 claude-code-skills-guide.md 읽고, 지금 설치 안 된 taste-skill Matt P (4a82016f)]]
- 관련: [[이름 충돌은 우선순위 파악 대신 rename으로 푼다]]
