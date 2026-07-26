---
title: Prompt Overload Makes Small LLMs Narrate Instead of Calling Tools
tags:
  - llm/prompting
  - llm/local
status: distilled
publish: true
lang: en
translation: 10-Concepts/프롬프트-과부하는-툴-호출-대신-텍스트-나레이션을-유발한다
created: 2026-07-26
sources: []
---

## Summary

Overloading a small model with detailed step-by-step few-shot examples backfires: instead of actually calling tools, the model **imitates the examples in prose** — describing what it would do and ending the turn (narration-not-action). Short, imperative instructions work better.

## Details

- Symptom: after a verbose "step 1, call tool X; step 2, ..." example, the model outputs "First, I will call tool X. Then..." — a textual re-enactment — instead of emitting the tool-call JSON.
- Cause: small models lean heavily on surface patterns in the prompt. If the example reads like a *description of actions*, generating more description becomes the highest-probability continuation.
- Fix: cut the examples, use **short imperative commands** — "Don't explain. Call the tool now.", "Output tool calls only." If you must show an example, show the literal call format, not a narrative about it.
- Implication: "more detailed prompt" is not monotonically better — there's a point where detail becomes load, and for small models that point arrives very early.

## Sources

- Related: [[Small LLM Tool Chaining Is Solved by Agent Separation, Not Prompting]]
