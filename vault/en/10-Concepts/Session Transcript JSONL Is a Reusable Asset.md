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

- Claude Code records every session as a JSONL file under `~/.claude/projects/<project-dir>/` — prompts, responses, and tool calls all land there in structured form. Not permanently, though: at startup it deletes transcripts whose last activity is older than `cleanupPeriodDays` (default 30 days).
- Bulk import: agentmemory's `import-jsonl` absorbed 14 sessions / 2063 observations in one pass, turning them into searchable long-term memory.
- Cross-project recall: hybrid search (BM25 + vector + graph) pulled a past prompt written in a different project into the current one.
- Wiki distillation: the same JSONL files feed this wiki's `90-Archive/` to `10-Concepts/` distillation pipeline.
- Mindset shift: treating transcripts as a structured dataset rather than "old conversation history" opens multiple reuse paths at once.
- Caveat: the raw JSONL expires, but copies made before then (archive notes, memory imports, backups) persist. Still treat anything pasted into chat (tokens, personal data) as permanently recorded, and keep sensitive values out of the conversation in the first place.
- Retention caused real loss: on 2026-11-21 only 17 transcript files were left, the oldest last active on 10-26. Sessions from roughly 10-05 to 10-21, which a broken archive hook had never captured, were gone for good ([[Fire-and-Forget Hooks Fail Silently]]). For secondary use, collect within the retention window or raise `cleanupPeriodDays` — this setup now uses 90.
- Don't trust the role field when converting transcripts for reading: answers collected through AskUserQuestion live inside tool_result, so extracting only "user messages" drops the decisions entirely. Conversely, background-task notifications (task-notification) and context-compaction summaries ("This session is being continued…") are recorded with role user and get misread as things the user said (this wiki's converted logs showed them as user turns too) — filter them out before extraction or statistics.
- It also works as a recovery store for quota-limited tool results: Figma MCP reads were capped at about 20 a month (view seat), so instead of calling again, a script pulled the design code out of tool_result entries in the JSONL (including results too large to inline, which had been spilled to separate files) and saved each screen by its `data-node-id`. That recovered 13 screens and 55 icons without the model re-typing large responses, and asset URLs that expire after 7 days were downloaded immediately.

## Sources

- 
