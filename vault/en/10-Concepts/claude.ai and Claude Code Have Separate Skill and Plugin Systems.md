---
title: claude.ai and Claude Code Have Separate Skill and Plugin Systems
tags:
  - tool/claude-code
  - tool/claude-ai
status: distilled
publish: true
lang: en
translation: 10-Concepts/claude.ai와-Claude-Code는-스킬·플러그인-체계가-분리되어-있다
created: 2026-07-26
sources: []
---

## Summary

claude.ai (web/desktop) and local Claude Code are **fully isolated sandboxes** — nothing installed in one carries over to the other, the installation mechanisms differ, and whether a plugin can be ported at all depends on what it's made of.

## Details

- **Separate install systems**: Claude Code uses marketplace/`~/.claude`-based plugins; claude.ai uses zip-upload Skills. The same capability must be installed in each environment separately.
- **Portability conditions**: claude.ai Skills support pure `SKILL.md` instruction text only —
  - Portable: instruction/checklist/document-style skills
  - Not portable: anything depending on hooks (event triggers), local MCP servers, subagents, or local scripts
- **Load-timing trap**: Claude Code plugins/hooks load **only at session start**. If a freshly installed command shows "unknown command", it's not broken — you haven't restarted the session. Check that first.
- Generalization: even within one product family, assume extensions are isolated per execution environment until proven otherwise.
- Exception: claude.ai connectors (MCP) do show up in Claude Code, as servers named "claude.ai <name>". But if you connect one mid-session, the running session keeps its pre-connection tool list — a new terminal showed it as Connected while the current session could not call it, and reconnecting that server from `/mcp` fixed it (reproduced twice).

## Sources

- (Korean source sessions are local-only archives)
