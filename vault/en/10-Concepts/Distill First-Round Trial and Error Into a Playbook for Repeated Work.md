---
title: Distill First-Round Trial and Error Into a Playbook for Repeated Work
tags:
  - dev/workflow
  - tool/claude-code
  - llm/context
status: distilled
publish: true
lang: en
translation: 10-Concepts/반복-작업은-첫-회차-시행착오를-플레이북으로-증류한다
created: 2026-11-21
sources: []
---

## Summary

For work that repeats in the same format, **distill the user's corrections, the pitfalls and the verification procedure into a playbook and a fill-in-the-blanks start prompt** at the end of the first round — the second round then runs with the user called in only at checkpoints, and the first round's big rework is prevented from the start.

## Details

- What the first round (the first of a series of course assignments in the same format) produced: a six-stage procedure with three checkpoints (approve the plan / check the program in the IDE, about 3 minutes / final pre-submission review), a line budget and a list of "features built and then removed", comment-writing rules, rules for accurate report sentences, a submission checklist, and 14 first-round pitfalls. The playbook ran to 526 lines.
- The start prompt has only four blanks (topic, assignment document, textbook document, deadline), plus a precondition: do not start if a required input (the textbook PDF) is missing.
- First-round-only rules (a specific handoff-document path, "a single source file") were removed from the always-loaded CLAUDE.md first — left in place, they would have contradicted the playbook.
- Keep reusable assets in the project folder: some first-round verification scripts vanished with a session temp folder and had to be rewritten. The second round started by copying the build, coverage, clean-environment and mutation scripts plus 14 input sets and only renaming their targets.
- Reorder to remove rework: the first round proved textbook errors after the fact, changed code after the report was submitted, and patched the PDF by hand right before the deadline. The second round fixed the order: reproduce every textbook example with a reference model → checkpoint 1 → implement → parallel independent reviews → freeze the code (record hashes) → generate the report from the frozen code.
- Preferences that arrive mid-run (comment tone, header format) are written into the playbook on the spot, so the next round applies them from the start.
- Write the reason next to each rule: the playbook only said "Korean console output was removed in round 1", with no reason, so when round 2 got a request for Korean output there was nothing to judge it by — and the first round's encoding-independence principle quietly broke.
- Record what recurred, too: the scope debate and a blown line budget (1,239 implementation lines against about 1,000) came back. The difference was that round 2 raised the overrun as a decision at a checkpoint (round 1 never mentioned missing its target).

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Bridge Sessions With a Project Memory Directory]], [[Always-Loaded Instruction Files Can Conflict]], [[Procedures Need Their Reasons to Be Applied Correctly in the Field]]
