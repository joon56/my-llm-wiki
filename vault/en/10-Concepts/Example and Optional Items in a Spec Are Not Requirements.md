---
title: Example and Optional Items in a Spec Are Not Requirements
tags:
  - dev/workflow
  - llm/agents
status: distilled
publish: true
lang: en
translation: 10-Concepts/명세의-예시·선택-항목은-요구사항이-아니다
created: 2026-11-21
sources: []
---

## Summary

LLM agents tend to implement every "e.g." and "optional" item in a spec or handoff document, plus defenses against errors that almost never happen, and the code balloons — **measure the excess by diffing output hashes against a minimal version that keeps only the core, and drop every feature you cannot justify against an evaluation criterion.**

## Details

- Case: the algorithm core was 297 lines of code (106 of them tables), yet the implementation file had 2,678 lines: four display options, a key argument, an output-target injection layer, 64 KiB streaming, thousands separators, and Linux/macOS branches never used in the target environment (Windows). Most came from the handoff document's "e.g." and "optional" items. The user pushed back twice with "why is this so long?"
- Diagnosis: build a minimal version (455 lines) with just the core and minimal I/O in a scratch folder, then compare output-file hashes and the results on 14 input sets for the same inputs. If they match, the other ~880 lines provably do not affect the result.
- Decide what stays by justifying each feature in a table keyed to the evaluation criteria (runs and matches the spec, components, size and speed, test coverage, design principles). Result: implementation 2,678 → 997 lines, executable 41,984 → 22,528 bytes, with identical output hashes, coverage and mutant detection.
- Length is a cost even without a line-count criterion: readers struggle to find the core, and size-based scoring suffers.
- Test-only hooks bloat the implementation too: the fault-injection macros were removed from the implementation. Instead, the test .c includes the standard headers first, swaps functions in with `#define malloc(n) test_malloc(n)`-style macros, includes the implementation .c, then `#undef`s them — the shipped implementation contains zero lines of test code.
- When scope decisions wobble, declare a one-sentence criterion first: "include anything whose removal leaves a capability missing; exclude a second way to produce the same output for the same input." Under it, generalizing the key length (about 15 lines) stayed in, and an alternative inverse cipher that performs the same decryption another way was dropped.
- Open the reference material you already have (grading rubric, assignment document) before asking about scope — claiming "the criteria are unknown" got corrected by the user, who pointed to the rubric in the folder. Carry the line budget and the "built then removed" feature list into the next job as up-front prohibitions.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Codify Constraints as Forbidden-Allowed Lists Before Work]], [[More Features Can Lose - Group Ablation and Complementarity]], [[Distill First-Round Trial and Error Into a Playbook for Repeated Work]]
