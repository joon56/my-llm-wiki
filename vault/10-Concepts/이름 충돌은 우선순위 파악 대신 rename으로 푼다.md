---
title: 이름 충돌은 우선순위 파악 대신 rename으로 푼다
tags:
  - tool/claude-code
  - dev/tooling
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Resolve-Name-Collisions-by-Renaming-Not-Priority-Testing
created: 2026-08-04
sources:
  - "[[2026-07-15 claude-code-skills-guide.md 읽고, 지금 설치 안 된 taste-skill Matt P (4a82016f)]]"
---

## 한 줄 요약

같은 이름의 명령이 여러 소스에 존재할 때 "어느 것이 이기는지" 실험하는 대신 하나를 rename해서 모호함 자체를 없애는 게 정답이다.

## 내용

- `/code-review`가 세 곳에 동시에 존재했음: 빌트인 1개 + 설치된 팩 2개. 어느 것이 실행될지 불명확한 상태.
- 우선순위 테스트가 비실용적인 이유: 확인하려면 재시작이 필요하고, 슬래시 명령 입력은 사용자 쪽에서 일어나므로 에이전트가 스스로 검증 루프를 돌 수 없음.
- 해법: 팩 하나의 스킬을 `two-axis-review`로 rename — 이름이 다르면 우선순위 규칙이 무엇이든 모호함이 발생할 수 없음.
- rename 시 세 군데를 함께 바꿔야 함: (1) 스킬 폴더 이름, (2) frontmatter의 `name:` 필드, (3) 해당 이름을 참조하는 모든 곳.
- 부작용: `npx skills update`가 원본 이름으로 파일을 되살림 — 업데이트를 돌린 뒤에는 rename을 다시 적용해야 함. 업데이트 루틴에 체크 항목으로 넣어둘 것.
- 일반 원칙: 결정 규칙을 알아내는 비용 > 충돌 자체를 제거하는 비용이면, 규칙 탐구를 버리고 구조를 바꾼다.

## 출처

- [[2026-07-15 claude-code-skills-guide.md 읽고, 지금 설치 안 된 taste-skill Matt P (4a82016f)]]
- 관련: [[서드파티 설치는 dry-run과 install-state 기준으로 다룬다]]
