---
title: When Agent-Driven Research Stalls, Measure the Handoff Structure First
tags:
  - dev/workflow
  - llm/agents
status: distilled
publish: true
lang: en
translation: 10-Concepts/에이전트-연구가-느리면-에이전트보다-인계-구조를-먼저-잰다
created: 2026-11-21
sources: []
---

## Summary

When agent-driven research stalls, swapping the agent does not help — **under the same process, any agent is just as slow**. First measure handoffs per idea, decision latency, document bloat, and time stuck on infrastructure, then cut handoffs with batch approval and timeboxes while keeping only the submission safety rails.

## Details

- Context: when progress stalled, the coding agent was swapped (Claude Code → Codex) and the score rose once, but after another seven-week plateau the work came back to the original agent. The newly brought-in agent's read-only handover review diagnosed the cause as the process, not the agent ("under the same rules, I would be just as slow").
- What to measure: each idea went through about 8 handoffs across three review stages, upload, and result logging. The workflow rules were revised four times in a month, the status doc grew to 1,356 lines and the log to 5,266, and a "decide within 48-72 hours" commitment turned into a 13-day gap.
- Over-strict contracts: the next candidate sat on hold for 13 days over one missing dependency (psutil). The official kit README already explained the install path, and a 20-line stand-in module used only when the import fails was enough — it was built and passed on the host on the first sprint day.
- Infrastructure swamps: weeks went into remote GPU infrastructure with zero model results. Set a timebox: if blocked for more than an hour, take the simplest workaround or drop it.
- The fix: approve several days of experiments in one batch, skip intermediate handoffs and stage reviews, and leave only uploads and the final choice to the user. Keep a single writer on the shared working folder (agents and subagents combined), hand over through file evidence rather than chat memory (match HEAD, the rules file's SHA256, and the dirty-file count), and keep the safety rails: official scorer pass, timing, baseline fallback. The reading cadence went from one every few days to three a day (partly from rechecking the daily quota).
- The real value of a swap is the full audit: right after the model switch, a read-only re-review found candidates that could not work in principle, a standard method never tested on real data, and four days of missing log entries.
- The limit: speed does not raise the score while candidate effects stay below the reading resolution (24 sprint uploads, zero gains). Cutting handoffs and making candidates bigger are separate problems.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Ask Only at Hard-to-Reverse Forks and Proceed on Disclosed Assumptions]], [[Split Parallel Subagents by File Ownership and Keep Builds in the Main Session]], [[Effects Smaller Than the Leaderboard Resolution Cannot Be Read]]
