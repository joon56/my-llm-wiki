---
title: Small LLM Tool Chaining Is Solved by Agent Separation, Not Prompting
tags:
  - llm/local
  - llm/agents
status: distilled
publish: true
lang: en
translation: 10-Concepts/소형-LLM-툴-체이닝은-프롬프트보다-에이전트-분리로-해결하라
created: 2026-07-26
sources: []
---

## Summary

Small local LLMs (3B-class) cannot be made reliable at multi-step tool chaining — feeding one tool's output into the next — no matter how carefully you engineer the prompt. The **structural fix** works: split the work into single-purpose agents so each agent holds only one or two tools.

## Details

- Real case: asking an Ollama 3B model to chain "multiply tool → feed result into add tool" kept failing — dropping intermediate results or skipping tools — even after repeated prompt refinement.
- The cause is **model capacity, not prompt quality** — choosing among tools, holding intermediate state, and planning order all at once exceeds a small model's reasoning budget. Prompt tweaks shift probabilities slightly; they never produce reliability.
- What worked: split into single-purpose agents — one agent that only multiplies, one that only adds — with orchestration (ordering) handled by code. Each agent sees 1–2 tools, so the choice space collapses and call stability jumps.
- General principle: the smaller the model, **the more intelligence you move into structure (code), leaving the model only narrow decisions**. Don't port the "one generalist agent with 10 tools" pattern from frontier models down to small ones.

## Sources

- Related: [[Prompt Overload Makes Small LLMs Narrate Instead of Calling Tools]]
