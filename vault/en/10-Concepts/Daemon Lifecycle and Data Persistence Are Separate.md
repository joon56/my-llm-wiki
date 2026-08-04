---
title: Daemon Lifecycle and Data Persistence Are Separate
tags:
  - dev/tooling
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/데몬-생명주기와-데이터-영속성은-분리된다
created: 2026-08-04
sources: []
---

## Summary

In any daemon-backed tool, process state and data state are independent axes — `stop` kills only the process while data stays on disk, and status-check commands must never mutate anything.

## Details

- agentmemory's `stop` terminates only the background process. Stored memories remain on disk under `~/.agentmemory/`, so restarting brings everything back intact.
- `status` is a pure query — even when the daemon is down, it reports and never starts it for you. Verify per tool that "check commands don't mutate".
- Background daemons stay alive until reboot unless explicitly killed — "it will shut itself down when the session ends" is a wrong assumption.
- Generalized mental model: for any daemon-backed tool, always separate two questions — (1) is the process running? (2) where does the data live?
- Practical consequence: to actually remove data, use the data directory or a deletion API, not `stop`; conversely, to just free resources temporarily, `stop` alone is enough and loses nothing.

## Sources

- 
