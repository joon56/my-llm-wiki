---
title: Session Transcript JSONL Is a Reusable Asset
tags:
  - tool/claude-code
  - llm/agents
  - dev/tooling
status: distilled
publish: true
lang: en
translation: 10-Concepts/세션-트랜스크립트-JSONL은-2차-활용-자원이다
created: 2026-08-04
sources: []
---

## Summary

The session JSONL files Claude Code keeps under `~/.claude/projects/` are not mere logs but raw material that supports bulk import, cross-project search, and wiki distillation.

## Details

- Claude Code preserves every session as a JSONL file under `~/.claude/projects/<project-dir>/` — prompts, responses, and tool calls all land there in structured form.
- Bulk import: agentmemory's `import-jsonl` absorbed 14 sessions / 2063 observations in one pass, turning them into searchable long-term memory.
- Cross-project recall: hybrid search (BM25 + vector + graph) pulled a past prompt written in a different project into the current one.
- Wiki distillation: the same JSONL files feed this wiki's `90-Archive/` to `10-Concepts/` distillation pipeline.
- Mindset shift: treating transcripts as a structured dataset rather than "old conversation history" opens multiple reuse paths at once.
- Caveat: this also means anything ever pasted into chat (tokens, personal data) persists in the JSONL forever — keep sensitive values out of the conversation in the first place.

## Sources

- 
