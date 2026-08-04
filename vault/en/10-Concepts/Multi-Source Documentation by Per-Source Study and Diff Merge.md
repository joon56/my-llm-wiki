---
title: Multi-Source Documentation by Per-Source Study and Diff Merge
tags:
  - research/writing
  - llm/pipeline
status: distilled
publish: true
lang: en
translation: 10-Concepts/멀티소스-문서화는-소스별-학습-후-차분-병합으로-한다
created: 2026-08-04
sources: []
---

## Summary

When building one guide from multiple sources (3 videos + a 76-page official PDF), do not blend them at once — study each source separately, extract an explicit diff, and merge it; this prevents both duplication and silent omission.

## Details

- Procedure: (1) study and summarize each source independently → (2) explicitly write out "what exists ONLY in the PDF" as a diff list → (3) merge that diff into the unified document.
- Real diff examples: the search operators reference and the AI keyword recommender existed only in the 76-page PDF, not in any video — items that would have been silently dropped without the diff list.
- Why not blend everything at once: overlapping content gets included multiple times, or conversely, each pass assumes "another source covered that" and it ends up nowhere — a silent omission.
- The key is making the diff an explicit written artifact, not a mental comparison — it becomes a merge checklist.
- The pattern scales with more sources: pick one baseline source, then add only each additional source's diff against that baseline.

## Sources

- 
