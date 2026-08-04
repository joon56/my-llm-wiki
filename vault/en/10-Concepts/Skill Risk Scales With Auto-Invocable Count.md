---
title: Skill Risk Scales With Auto-Invocable Count
tags:
  - tool/claude-code
  - llm/agents
  - llm/context
status: distilled
publish: true
lang: en
translation: 10-Concepts/스킬-위험-지표는-자동-발동-가능-개수다
created: 2026-08-04
sources: []
---

## Summary

The real risk metric is not how many skills are installed but **how many of them the model can invoke on its own (auto-invocable)** — misfire risk lives only in that subset.

## Details

- Measured case: of 119 installed SKILL.md files, 96 were auto-invocable. Misfire risk (a skill firing in the wrong situation) exists only for those 96; the rest are fully manual until the user calls them via slash command.
- Setting `disable-model-invocation: true` in a skill's frontmatter makes it slash-command-only — the model can never trigger it by itself, so misfire risk drops to zero.
- "How many skills did I install" is therefore the wrong question; count how many are auto-invocable. To reduce risk you often don't need to delete a skill — disabling auto-invocation is enough.
- Hidden cost: skill descriptions are not lazy-loaded — **they are all loaded into context every session**. Each auto-invocable skill carries a permanent per-session token cost; with 96 of them, 96 descriptions occupy context at all times.
- In short, auto-invocable skills cost you on two axes — (1) misfire probability and (2) always-on token overhead — so rarely used skills are best demoted to slash-only.

## Sources
- 
