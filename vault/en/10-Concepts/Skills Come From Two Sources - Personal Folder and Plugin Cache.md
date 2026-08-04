---
title: Skills Come From Two Sources - Personal Folder and Plugin Cache
tags:
  - tool/claude-code
  - dev/workflow
status: distilled
publish: true
lang: en
translation: 10-Concepts/스킬의-출처는-개인-폴더와-플러그인-캐시-두-곳이다
created: 2026-08-04
sources: []
---

## Summary

Skills come from **two paths — the personal folder (`~/.claude/skills/`) and the plugin cache** — and knowing which source a skill lives in tells you where to edit or remove it.

## Details

- Personal skills live at `~/.claude/skills/<name>/SKILL.md`. These are ones you wrote or copied in yourself: edits take effect directly, and deleting the folder removes the skill.
- Plugin skills materialize at `~/.claude/plugins/cache/<marketplace>/<plugin>/<hash>/skills/<name>/SKILL.md`. They are a byproduct of plugin installation — editing the cached file gets overwritten on update, and removal goes through `claude plugin uninstall`, not file deletion.
- Measured case: an audit found roughly 30 skills that were **all plugin-derived**, with a personal count of zero — everything the user thought of as "my skills" actually lived in the plugin cache.
- To scaffold a skill of your own, start with `claude plugin init <name>`.
- Practical rule: before editing or deleting a skill, check the actual path of its SKILL.md — a path under `skills/` means edit the file; a path under `plugins/cache/` means manage it at the plugin level.

## Sources
- 
