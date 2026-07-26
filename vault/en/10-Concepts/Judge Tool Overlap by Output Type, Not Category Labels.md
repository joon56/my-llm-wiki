---
title: Judge Tool Overlap by Output Type, Not Category Labels
tags:
  - dev/tooling
  - product/research
status: distilled
publish: true
lang: en
translation: 10-Concepts/유사-도구의-역할-중복은-산출물-성격으로-판별한다
created: 2026-07-26
sources: []
---

## Summary

Category labels on tools ("research", "analytics") are ambiguous — judging "we already have one of these" by label alone gets it wrong. Distinguish roles by **what the tool actually outputs**: source evidence, processed judgment, or executable artifact.

## Details

- The trap: under the same "research tool" label — a tool that retrieves academic papers and a tool that generates market-research reports play **entirely different roles**. Going by label, you'd either reject a tool you need as "duplicate" or install two that do the same thing.
- The discriminating axis — what does it emit at the end:
  - **Source evidence** (papers, datasets, raw material) — ingredients for judgment
  - **Processed judgment** (strategy reports, summaries, recommendations) — someone else's digested conclusions
  - **Artifacts** (code, prototypes, designs) — executable results
- Same axis → duplication candidates; different axes → complements. When designing a stack, filling one slot per axis is the balanced shape.
- Extension: this is the general ambiguity of search keywords — when picking tools via words like "analytics", "automation", "AI assistant", check the demo output first.

## Sources

- (Korean source session is a local-only archive)
