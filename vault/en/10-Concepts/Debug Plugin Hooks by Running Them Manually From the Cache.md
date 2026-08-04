---
title: Debug Plugin Hooks by Running Them Manually From the Cache
tags:
  - tool/claude-code
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/플러그인-훅은-캐시-디렉토리에서-수동-실행해-진단한다
created: 2026-08-04
sources: []
---

## Summary

When a plugin hook seems to error, run the hook script manually from the installed copy under `~/.claude/plugins/cache/` and check its exit code — that is what separates real failures from cosmetic messages.

## Details

- Diagnosis path: go to `~/.claude/plugins/cache/<marketplace>/<plugin>/<hash>/`, read `hooks.json` to see which script is attached to which event.
- Then execute the hook script directly in a terminal and check the exit code — 0 means the hook itself is fine; non-zero means a genuine failure.
- In this case, the suspected "error" turned out to be a statusline-not-configured nag message, not a hook failure — manual execution settled it immediately.
- Guessing from the in-session error message alone lumps informational nags, warnings, and real failures into one undifferentiated "error"; manual execution is the only reliable way to separate them.
- Detail worth remembering: the `<hash>` directory in the cache is the version that actually runs, so read the cached copy, not the upstream repo, to match current behavior.

## Sources

- 
