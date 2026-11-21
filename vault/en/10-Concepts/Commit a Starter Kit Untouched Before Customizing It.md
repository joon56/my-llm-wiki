---
title: Commit a Starter Kit Untouched Before Customizing It
tags:
  - tool/git
  - dev/workflow
  - dev/docs
status: distilled
publish: true
lang: en
translation: 10-Concepts/상류-패치를-받을-스타터는-원본-그대로-첫-커밋한다
created: 2026-11-21
sources: []
---

## Summary

When you receive a starter kit whose provider will send patches later, **commit it untouched before changing anything, so `git apply --3way` has the base blobs it needs**, and keep the IDs you add locally out of the numbering range the upstream will continue.

## Details

- The payoff: because the starter had been committed exactly as received before any edits, an upstream patch (v1→v3) that arrived two days later could be applied with `git apply --3way`. Many documents had already been edited, yet the patch did not fail wholesale; it only left conflict markers.
- Why it works: a 3-way merge needs the original blobs named on the patch's `index <old>..<new>` lines to exist in the local object database. Without the pristine commit, the only route is `--reject` and applying `.rej` files by hand.
- Order of operations: extract with `unzip -n` (never overwrite existing files; first check that the archive paths are plain relative paths) → dry-run with `git apply --check` → stage local changes instead of committing them → apply. `--3way` implies `--index`, so the working tree and the index must match.
- Fix the conflict rule in advance: keep every value, row, and note the local side filled in (measured facts, decision records, config numbers, current status) and add only the upstream's new rows and keys. Report each place you deliberately diverged from the kit (four this time) with its reason, so the next patch does not hit the same conflict.
- Numbering collisions: local decision records had been appended right after the upstream's numbers (D-27 to D-42), and the upstream kit then defined that same range itself, so the local items were renumbered from D-43, touching 127 references across documents, config comments, and code comments, and three overlapping items were merged. Start local additions with a separate prefix or a generously offset range from day one.
- Renumbering leaves a tail: commit messages keep pointing at the old numbers forever, so keep an old→new mapping table in the change log. In Korean text the particle after a number depends on how the number is pronounced, so renumbering can leave grammatical errors (e.g. "D-54으로"); check particles after renumbering.
- Make cleanup conditional on verification: version header, zero conflict markers, continuous numbering with no duplicates or dangling references, config loads, CSV headers match the docs, code diffs touch only comments, and a privacy scan. When one test still failed, the "delete once everything checks out" condition was not met, so the patch and zip were kept, and the commit came only after the user reviewed the staged diff.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Seed Migrations Separate Content Updates From User State]], [[Client-Persisted IDs Are Immutable Contracts]]
