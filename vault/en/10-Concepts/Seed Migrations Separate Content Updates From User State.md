---
title: Seed Migrations Separate Content Updates From User State
tags:
  - dev/architecture
status: distilled
publish: true
lang: en
translation: 10-Concepts/시드-마이그레이션은-콘텐츠-갱신과-사용자-상태를-분리한다
created: 2026-08-14
sources: []
---

## Summary

In a serverless localStorage app, updating seed data safely requires a **seed version plus a chain of per-version migrate functions** that merge "author-owned content" separately from "user-created state" — swapping the seed wholesale resets the user's progress.

## Details

- Structure: the seed carries `version: N`; the app runs `if (v < 6) migrateV6(s); if (v < 7) migrateV7(s);`. Each migrate copies **only the fields that changed in that version** from the seed into the user's stored state.
- Separation rules:
  - Author-owned fields (titles, dates, descriptions, links): overwrite with the seed value.
  - User-owned fields (completion checks, status, personal memos): never touch.
  - Mixed fields (notes the author pre-fills but the user may edit): **guard before overwriting** — e.g. replace only if the new phrasing isn't already present.
- Migrations run cumulatively, so each function must be idempotent and safe starting from any older state. Look items up by id and skip silently when missing (the user may have deleted them).
- In domains where content corrections are frequent (tracking external schedules, for example), this pattern turns "fix the seed, bump the version" into a safe routine.

## Sources

- Related: [[Client-Persisted IDs Are Immutable Contracts]], [[Data Architecture That Generates Derivatives From a Single Source of Truth]]
