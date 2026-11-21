---
title: 프로필 비교는 모듈명이 아니라 install plan diff로 한다
tags:
  - dev/tooling
  - tool/claude-code
  - llm/agents
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Compare-Tool-Profiles-by-Install-Plan-Diff,-Not-Module-Names
created: 2026-08-04
sources:
  - "[[2026-07-15 claude-code-skills-guide.md 읽고, 지금 설치 안 된 taste-skill Matt P (4a82016f)]]"
---

## 한 줄 요약

minimal vs developer 같은 프로필 선택은 모듈 이름을 읽고 감으로 하는 게 아니라, 두 프로필의 실제 install plan(파일 목록)을 diff해서 결정한다.

## 내용

- minimal과 developer 프로필을 각각 `--dry-run`으로 뽑은 실제 설치 계획끼리 비교해서 판단.
- diff 결과 1: minimal은 developer의 엄밀한 부분집합(strict subset)이었음 — "minimal을 고르면 뭔가 빠질까?"라는 걱정을 데이터로 해소.
- diff 결과 2: 오발동이 잦던 문제 모듈들은 이미 minimal에도 포함되어 있었음 — developer를 피한다고 오발동이 사라지는 게 아니었음.
- diff 결과 3: developer 전용 추가분은 Perl/F#/ArkTS 등 쓰지 않는 스택 커버리지였음 — 이 환경에서는 순수한 토큰 비용일 뿐.
- 교훈: "developer"라는 이름은 아무 정보도 주지 않는다. 이름은 마케팅이고, 파일 목록이 사실이다.
- 재사용 가능한 패턴: 프로필/에디션/티어 중 하나를 골라야 할 때마다 각각의 산출물 목록을 뽑아 diff → 차집합이 나에게 가치가 있는지만 판단.

## 출처

- [[2026-07-15 claude-code-skills-guide.md 읽고, 지금 설치 안 된 taste-skill Matt P (4a82016f)]]
- 관련: [[서드파티 설치는 dry-run과 install-state 기준으로 다룬다]]
