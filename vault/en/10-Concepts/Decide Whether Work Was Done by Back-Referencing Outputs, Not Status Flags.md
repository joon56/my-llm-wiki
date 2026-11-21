---
title: Decide Whether Work Was Done by Back-Referencing Outputs, Not Status Flags
tags:
  - llm/pipeline
  - dev/workflow
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/처리-여부는-상태-플래그가-아니라-산출물-역참조로-판정한다
created: 2026-11-21
sources: []
---

## Summary

In a multi-step pipeline, if only the "mark done" step is skipped, **the status field lies and the next run reprocesses the same input** — before reprocessing, back-search the outputs for the input's ID to see whether it was actually handled, and only then ask the user to choose.

## Details

- The case: in this wiki's distillation routine, 10 of 15 `status: raw` source logs were read closely and classified, and the user picked 4 titles for new notes — only then was duplication suspected. All 10 had already been cited as sources of concept notes in an earlier run; only the source status update and the backlinks had been skipped.
- Diagnosis: grep the concept-note folder for each session ID (8 characters) to map which source is cited by which note. Cited sources became distilled with backlinks, sources without lessons became triaged, and out-of-scope ones stayed raw. New notes: zero.
- The cost: every title the user picked was already covered by an existing note — one user decision and a close reading of 10 sources wasted.
- Judgments drift between runs: a session that an earlier run had used as the source for 7 concept notes was first classified as "no lesson" this time. Back-referencing existing outputs has to come before re-judging.
- The root structure: writing outputs (notes) and updating the ledger (source status, backlinks) are separate steps, so if a session ends after the first, the status stays wrong. The ledger lived in a local archive that git does not track, so history could not reveal it either.
- Principle: a status flag is a cache, not the truth. Decide "already processed?" from evidence on the output side (back-searching the input ID, presence of the output file), and mark completion in the same step that writes the output — ideally in the same commit.
- Order of checks: before producing candidates, (1) back-search the input IDs and (2) check for conceptual duplicates among existing outputs; ask the user only after that.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[The Recursive Contamination Trap of Tools That Consume Their Own Logs]], [[Fire-and-Forget Hooks Fail Silently]], [[Generate Change Reports From the Diff, Not From Memory]]
