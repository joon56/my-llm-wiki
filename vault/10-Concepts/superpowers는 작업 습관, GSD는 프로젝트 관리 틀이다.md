---
title: superpowers는 작업 습관, GSD는 프로젝트 관리 틀이다
tags:
  - tool/claude-code
  - dev/workflow
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/superpowers-Is-a-Work-Habit,-GSD-Is-a-Project-Framework
created: 2026-10-05
sources:
  - "[[2026-09-05 최근에 설치한 get shit done 스킬과 기존의 superpowers 스킬이 겹치는 부분이 있다고 말했 (83d63dca)]]"
---

## 한 줄 요약

둘 다 '계획 → 실행 → 검증'을 강제하는 프로세스 스킬이지만, **superpowers는 작업 하나 단위의 무상태 규율**이고 **GSD는 `.planning/`에 상태를 남기는 다중 세션 프로젝트 관리 시스템**이다 — 기능이 겹치는 게 아니라 층위가 다르다.

## 내용

- 겹치는 짝: brainstorming ↔ `/gsd-discuss-phase`·`/gsd-spec-phase` / writing-plans ↔ `/gsd-plan-phase` / executing-plans·subagent-driven-development ↔ `/gsd-execute-phase`·`/gsd-quick` / systematic-debugging ↔ `/gsd-debug` / verification-before-completion ↔ `/gsd-verify-work` / code-review ↔ `/gsd-code-review`.
- 상태: superpowers는 세션이 끝나면 사라진다. GSD는 ROADMAP·STATE·PLAN·VERIFICATION 파일을 남겨 `/clear` 후에도 `/gsd-resume-work`로 이어 간다.
- 단위와 발동: superpowers는 작업 하나, 매 대화 시작마다 자동 발동("1%라도 해당되면 반드시 써라"). GSD는 프로젝트 → 마일스톤 → 페이즈 → 플랜 계층, 명시적 `/gsd-*` 명령으로만.
- 비용: GSD는 planner·executor·verifier 등 전용 서브에이전트가 수십 개라 토큰 비용이 훨씬 크다. GSD에만 있는 것: 커밋 자동화, PR 생성, 마일스톤 아카이브. superpowers에만 있는 것: TDD, git worktrees, 스킬 작성.
- 선택: 단일 기능·버그·실험 하나 → superpowers. 0에서 시작해 수 주 걸리고 세션이 여러 번 끊기는 프로젝트, 기존 코드베이스 인수 → GSD.
- 금지: 이미 자체 진실 원천(실험 로그, status 문서, 제출 기록)이 있는 저장소에 GSD `.planning/`을 얹으면 진실 원천이 둘이 된다.
- 함께 쓸 때: GSD가 "무엇을 언제", superpowers가 "어떻게"를 맡는다. GSD 실행 중엔 writing-plans를 중복하지 않되, debugging·verification·TDD는 그대로 유효하다.

## 출처

- [[2026-09-05 최근에 설치한 get shit done 스킬과 기존의 superpowers 스킬이 겹치는 부분이 있다고 말했 (83d63dca)]]
- 관련: [[유사 도구의 역할 중복은 산출물 성격으로 판별한다]], [[단일 원본에서 파생물을 생성하는 데이터 아키텍처]], [[스킬 선택 경쟁은 에러 없는 확률 게임이다]]
