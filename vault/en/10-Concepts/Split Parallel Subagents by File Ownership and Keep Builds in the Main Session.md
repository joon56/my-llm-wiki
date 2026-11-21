---
title: Split Parallel Subagents by File Ownership and Keep Builds in the Main Session
tags:
  - llm/agents
  - tool/claude-code
  - dev/workflow
status: distilled
publish: true
lang: en
translation: 10-Concepts/병렬-서브에이전트는-파일-소유권으로-나누고-빌드는-메인이-독점한다
created: 2026-11-21
sources: []
---

## Summary

When you hand screen implementation to several subagents in parallel, **the main session first freezes the shared files and stub signatures, then gives each worker a contract: edit only your own files, never run the build, and report (don't fix) problems in shared files** — integration then lands in one pass.

## Details

- What the main session fixed before delegating: the data layer, all string resources (written in one go to avoid parallel conflicts), shared helpers and layouts, and three screens that demonstrate the patterns. The remaining screens were "compiles-only" stubs with their public signatures in place, and the three workers started only after the baseline build and tests passed.
- Worker contract: no edits outside your owned-file list; keep the stubs' public APIs and class signatures; new strings only in your own prefixed file (Korean and English together); if a shared helper is missing, write it privately in your own file and report it; never run the build tool. Landscape layouts must match the portrait ids and view types exactly (ViewBinding requires it).
- Self-checks without building: the workers used scripts to verify XML well-formedness, that every resource and id reference exists, that all 215 translations were present with matching format arguments, and that portrait and landscape layout ids matched (26 and 37). Anything they were not sure would compile went into a separate section of their report.
- Outcome: each worker took about 8-11 minutes and roughly 0.42-0.45M tokens. Without waiting for the last worker, the main session compiled the two finished workers' code first and got zero errors; after merging, the full build and all 37 tests passed. Meanwhile the main session set up the backend and booted the emulator.
- Shared-file problems came back as reports, not edits: two workers independently flagged that the library's default `buttonCompat` style would override `android:button=@null` and redraw radio circles on chips, and the main session fixed it once in the shared style. A warning that tabs included in the same screen would mix their saved state on rotation if their ids collided also arrived as a report.
- Delegated research used the same contract style: read-only, results only in a designated file, a URL for every non-obvious claim, and say so when unsure. Two research workers ran alongside implementation and surfaced constraints before any code was written — "storage keys cannot contain Korean -> use UUID keys", "AI calls require App Check".

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Split Web Research Into Verifier and Discovery Agents]], [[Codify Constraints as Forbidden-Allowed Lists Before Work]]
