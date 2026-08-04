---
title: Skills Are Probabilistic, Hooks Are Deterministic
tags:
  - tool/claude-code
  - llm/agents
  - dev/workflow
status: distilled
publish: true
lang: en
translation: 10-Concepts/스킬은-확률적으로,-훅은-결정론적으로-강제된다
created: 2026-08-04
sources: []
---

## Summary

Skills only work if the model *chooses* to invoke them, while hooks run unconditionally whenever their event fires — so **rules that must always hold belong in hooks, not skills**.

## Details

- A skill works by the model reading its description and deciding whether to use it now — no matter how well written, a skill the model doesn't pick might as well not exist for that session.
- A hook runs every single time its registered event occurs. Examples: a block-no-verify hook that blocks `--no-verify` commits, a cost-tracker hook that records session cost.
- Decision rule: guidance that can occasionally be skipped goes in a skill; rules that must never be violated (blocking dangerous commands, secret scanning, cost logging) go in hooks.
- Trap: a hook script sitting on disk does nothing by itself — it only runs if it is wired into the `hooks` key of settings.json. In the audited setup, **132 dead hook scripts** were found installed but never wired up.
- Audit method: compare the number of hook script files on disk against the number of entries in settings.json `hooks` — that exposes hooks you believe are installed but that have never executed once.

## Sources
- 
