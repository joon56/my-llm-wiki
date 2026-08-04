---
title: Plugin Slash Commands Are Namespaced
tags:
  - tool/claude-code
  - dev/workflow
status: distilled
publish: true
lang: en
translation: 10-Concepts/플러그인-슬래시-커맨드에는-네임스페이스가-붙는다
created: 2026-08-04
sources: []
---

## Summary

The real name of a plugin-provided slash command is the **fully namespaced `/plugin:command` form** — typing it without the namespace yields an unknown-command error.

## Details

- Plugin commands are always registered under a `plugin:command` namespace. Example: the caveman plugin's command is `/caveman:caveman`, not `/caveman`.
- Typing bare `/caveman` produces an "unknown command" error — the plugin isn't missing, you only typed half the name.
- The namespace rule prevents collisions when different plugins ship same-named commands, at the cost of longer typing every time.
- For a short alias, wrap it with a user command file under `~/.claude/commands/`. Example: create `~/.claude/commands/cm.md` that internally invokes the namespaced command, and it runs as `/cm`.
- User commands (`~/.claude/commands/*.md`) become slash commands under their bare filename with no namespace, which makes them a good shortcut layer for frequently used plugin commands.

## Sources
- 
