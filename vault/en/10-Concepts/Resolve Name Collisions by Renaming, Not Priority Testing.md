---
title: Resolve Name Collisions by Renaming, Not Priority Testing
tags:
  - tool/claude-code
  - dev/tooling
status: distilled
publish: true
lang: en
translation: 10-Concepts/이름-충돌은-우선순위-파악-대신-rename으로-푼다
created: 2026-08-04
sources: []
---

## Summary

When the same command name exists in multiple sources, do not experiment to learn "which one wins" — rename one of them so the ambiguity cannot occur at all.

## Details

- `/code-review` existed three ways at once: one built-in plus two installed packs, with no clear answer as to which would run.
- Why priority testing is impractical: verifying requires a restart, and slash-command input happens on the user's side, so the agent cannot run the verification loop by itself.
- Fix: renamed one pack's skill to `two-axis-review` — with distinct names, no priority rule can ever produce ambiguity.
- A rename must touch three places together: (1) the skill folder name, (2) the `name:` field in frontmatter, (3) every reference to the old name.
- Side effect: `npx skills update` resurrects the file under its original name — the rename has to be re-applied after each update, so put it on the update checklist.
- General principle: when discovering the resolution rule costs more than removing the collision, skip the investigation and change the structure.

## Sources

- 
