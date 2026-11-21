---
title: Separate a Read-Only Question Session From the Working Session
tags:
  - tool/claude-code
  - dev/workflow
  - llm/prompting
status: distilled
publish: true
lang: en
translation: 10-Concepts/읽기-전용-질문-세션을-작업-세션과-분리한다
created: 2026-11-21
sources: []
---

## Summary

Alongside the working session that edits the repository, keep **a separate question session that only reads**, and fix its forbidden list, answer format, and handoff format in the first prompt — long decision-making Q&A then stays out of the working session's context, and only settled decisions cross over.

## Details

- Put the forbidden list in the first prompt: no file edits, commits, pushes, or code inside the repo; no hypothesis verdicts from real data; no printing of sensitive values (coordinates, device IDs). Name the four documents to read first and the extra ones per question type. If data must be inspected, use a throwaway script outside the repo, run with `python -I`.
- Fix the answer format: separate "what the documents say / what was computed from data / opinion" and cite the file and section (e.g. `SPEC §5.2`, `D-30`). Where there are options, give one recommendation with a reason and leave the decision to the user. Definitions fixed before seeing results are never proposed for change; only their impact and the options are explained.
- Separating these layers exposes gaps in the documents: answers like "the documents never say why this step exists" or "the reason for this condition is my interpretation, not documented" keep model opinion from passing as fact.
- Handoff format: on "summarize", produce a block to paste into the working session — (1) what was decided (decision IDs and answers), (2) new questions and to-dos, (3) candidates to move into the decision log or fact documents. Unknown values stay as blanks (`___`) for the user to fill, so the question session never invents them.
- The boundary held in practice: when the user said "let's start working", the question session handed over a summary instead of doing the work and sent the user back to the working session. Inspecting a file outside its scope was first proposed as "header and row count only, no values" and waited for permission.
- One handoff per destination: when work spans several places, write separate handoffs for the working session (code and docs) and for another app (team documents), and leave the user a list of only what they must do themselves.
- The field version of the same pattern: the working session wrote the pass/fail criteria, the file flow, and a "do not say in the field" list into a `.handoff/` document, and a dedicated field-check session read and followed it. Even after the context was compacted, the rules survived in the summary and the checks carried on.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Codify Constraints as Forbidden-Allowed Lists Before Work]], [[Bridge Sessions With a Project Memory Directory]], [[Split Parallel Subagents by File Ownership and Keep Builds in the Main Session]]
