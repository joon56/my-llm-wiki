---
title: Grep Installed Sources for Undocumented APIs
tags:
  - tool/claude-code
  - dev/debugging
  - llm/agents
status: distilled
publish: true
lang: en
translation: 10-Concepts/문서에-없는-기능은-설치된-소스를-grep해서-찾는다
created: 2026-08-04
sources: []
---

## Summary

For a locally installed tool, the installed code itself is the authoritative documentation — when the docs lack a feature you need, grep the package source in `node_modules` and call what you find.

## Details

- Needed to delete a specific session's memories in agentmemory, but neither the docs nor the skills mentioned any per-session deletion.
- Grepped the installed package source (under `node_modules`) and found a `POST /agentmemory/forget` endpoint that accepts `{sessionId}` — confirmed directly in the code.
- Called that endpoint via plain REST and the undocumented session deletion worked, with no dedicated CLI command or MCP tool involved.
- Principle: route definitions and handler signatures of a locally installed tool sit right there in the code, so "not documented" does not mean "not possible".
- Search order: (1) check official docs/skills, (2) grep the install path for route and command strings, (3) verify the signature, then call it directly.
- Unlike remote web APIs, local tools ship their source, so this always works and there is no version mismatch — you are reading the exact code that is running.
- A second case: the Firebase CLI's non-interactive login link expired within minutes with "Unable to verify client". Reading the installed firebase-tools source turned up two workable paths — `firebase login <auth code>` resuming the pending session (code verifier) saved in its config file, and calling `loginGoogle(true)` and `recordCredentials()` from `lib/auth` directly with node, which completes via this PC's browser and a localhost callback with no code pasting. The re-login procedure went into memory.

## Sources

- 
