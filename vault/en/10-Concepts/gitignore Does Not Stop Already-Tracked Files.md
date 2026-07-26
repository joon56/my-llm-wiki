---
title: gitignore Does Not Stop Already-Tracked Files
tags:
  - tool/git
status: distilled
publish: true
lang: en
translation: 10-Concepts/gitignore는-이미-추적된-파일을-막지-못한다
created: 2026-07-26
sources: []
---

## Summary

`.gitignore` only applies to files that are not yet tracked — a file that's already committed keeps being tracked and pushed even after you add it to `.gitignore`, so it needs to be explicitly untracked with `git rm -r --cached`.

## Details

- What gitignore actually does: "exclude untracked files from staging candidates." Files already in the index are not affected.
- A common failure pattern: a cache file gets committed, then added to `.gitignore` — but its changes keep getting pushed anyway. The common misdiagnosis: "gitignore isn't working."
- The fix: `git rm -r --cached <path>` (keeps the local file, only untracks it), then commit. Gitignore takes effect from that point on.
- **Warning: it still lives in commit history.** If secrets or PII got committed, untracking alone isn't enough — you also need history rewriting (filter-repo) and to rotate any exposed keys.
- Preventive habit: when setting up `.gitignore` in a repo for the first time, audit already-tracked files with `git ls-files` first. Especially for public repos, check history for caches, personal data, or real names before pushing.

## Sources
-
