---
title: superpowers Is a Work Habit, GSD Is a Project Framework
tags:
  - tool/claude-code
  - dev/workflow
status: distilled
publish: true
lang: en
translation: 10-Concepts/superpowers는-작업-습관,-GSD는-프로젝트-관리-틀이다
created: 2026-10-05
sources: []
---

## Summary

Both are process skills that enforce plan -> execute -> verify, but **superpowers is stateless, per-task discipline** while **GSD is a multi-session project-management system that keeps state in `.planning/`** — they are not overlapping features but different layers.

## Details

- Matching pairs: brainstorming <-> `/gsd-discuss-phase`, `/gsd-spec-phase` / writing-plans <-> `/gsd-plan-phase` / executing-plans, subagent-driven-development <-> `/gsd-execute-phase`, `/gsd-quick` / systematic-debugging <-> `/gsd-debug` / verification-before-completion <-> `/gsd-verify-work` / code-review <-> `/gsd-code-review`.
- State: superpowers vanishes when the session ends. GSD leaves ROADMAP, STATE, PLAN and VERIFICATION files, so `/gsd-resume-work` picks up even after `/clear`.
- Unit and triggering: superpowers works per task and fires automatically at the start of every conversation ("if there is even a 1% chance, use the skill"). GSD works in a project -> milestone -> phase -> plan hierarchy, only through explicit `/gsd-*` commands.
- Cost: GSD runs dozens of dedicated subagents (planner, executor, verifier...), so token cost is far higher. GSD only: commit automation, PR creation, milestone archives. superpowers only: TDD, git worktrees, skill writing.
- Choose: a single feature, bug or experiment -> superpowers. A project starting from zero that spans weeks and many broken-up sessions, or taking over an existing codebase -> GSD.
- Don't: put GSD's `.planning/` on a repo that already has its own source of truth (experiment logs, status docs, submission records) — you end up with two sources of truth.
- Together: GSD owns "what and when", superpowers owns "how". During a GSD run, skip writing-plans, but debugging, verification and TDD still apply.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Judge Tool Overlap by Output Type, Not Category Labels]], [[Data Architecture That Generates Derivatives From a Single Source of Truth]], [[Skill Selection Competition Is a Silent Probability Game]]
