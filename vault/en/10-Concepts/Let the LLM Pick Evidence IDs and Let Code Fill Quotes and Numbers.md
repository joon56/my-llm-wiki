---
title: Let the LLM Pick Evidence IDs and Let Code Fill Quotes and Numbers
tags:
  - llm/pipeline
  - llm/prompting
status: distilled
publish: true
lang: en
translation: 10-Concepts/LLM은-근거-ID만-고르고-인용·숫자는-코드가-채운다
created: 2026-11-21
sources: []
---

## Summary

A rule that a note line passes only if it matches a source quote word for word turned consultation notes into sentence classification and earned the verdict "not specific enough". **Let the LLM write the prose but choose evidence only by alias; code fills in quotes, timestamps, and speakers, and code checks numbers and names.**

## Details

- Starting point: in the old design, each note line had to match a source quote exactly. No model swap can produce narrative notes under that rule — the output becomes a classifier that decides which utterance goes in which slot, which was the structural cause of the demo feedback "not specific enough".
- Structure: transcript segments and scene photos get aliases (`s01`, `m01`), and the LLM returns only sentences plus evidence aliases under a JSON schema. Code fills quotes, timestamps, and speakers from the aliases, so the model has no room to rewrite a quote.
- Code checks: block numbers absent from the evidence (compared with units), names, banned expressions, speaker-rule violations, and sentences whose bigram overlap with their evidence is below 0.3. Only failed sentences are re-asked once with the reason attached (partial repair); a second failure drops the sentence with a warning, and missing information is written as "unconfirmed".
- Safety flags are rules OR LLM: the LLM can raise a risk flag but can never lower one.
- Long inputs and style: split into 1,500-character chunks with 200 characters of overlap, then merge by evidence and same-fact matching. Sentences are written in record style rather than copied speech, one fact per item ("About thirty seconds." → "Once barking starts, it lasts about thirty seconds").
- Results (synthetic dialogues): across 11 dialogues, 97.7% fact recall, 100% task capture, and 0 unsupported numbers; on a 33-minute consultation, facts 78 → 97.5%, tasks 62.5 → 87.5%, processing time 24.6 → 18.3 min. The gains mix the effects of several changes.
- Humans confirm what remains: scene observation once described a dog lying down as "sitting". Code checks guarantee the link to evidence, not the accuracy of the observation, so the expert confirmation step stays.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Make the LLM Flag Every Sentence Written Beyond the Source Material]], [[Never Trust PDF Table Extraction Without Cross-Checking the Prose]], [[Forcing the Output Removes the Path to an Empty Answer]]
