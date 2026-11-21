---
title: Make the LLM Flag Every Sentence Written Beyond the Source Material
tags:
  - llm/prompting
  - dev/workflow
  - dev/docs
status: distilled
publish: true
lang: en
translation: 10-Concepts/LLM이-원자료-밖에서-쓴-문장은-따로-신고하게-한다
created: 2026-11-21
sources: []
---

## Summary

When an LLM builds presentation material from official sources, **have it flag, item by item, every inference, piece of general knowledge or unverified claim that is not in the sources, and render only what a human approved at the text stage** — that catches stale assumptions before they get baked into convincing slides.

## Details

- Two user instructions set the frame: "don't decide arbitrarily — resolve it by asking me," and "tell me this content before you put it into the HTML; we'll verify it, then add it."
- Ask the blocking questions first: questions were split into "must confirm now" (date and length, which edition of the reference document, scope of terms) and "can decide later" (format, practice tool, how to handle an error in a reference), with "answer just 1–4 and I'll start." The user answered in four lines and work started immediately.
- List out-of-source sentences: the draft report carried a separate list of "parts I wrote that are not in the official document" — a "where is this used" column per course, career examples split by track when the source gave them only for the whole department, and a tool-usage claim backed only by vendor customer stories.
- Per-item [verify] tags: each line of the recommendation list marked what was uncertain (whether it would resonate with the audience, a site's Korean support, an app's menu location, whether a public dataset still existed, whether an unconfirmed event could be mentioned). At this gate the user removed a motivator that no longer matched reality (coding-test prep) and approved the rest.
- Hand over what could not be checked, together with how to check it: project import not tested in a real IDE, an error-message table written from memory, a dataset detail page that timed out. Each came with a human check such as "during rehearsal, make one mistake on purpose and confirm the message matches."
- Errors in references count too: a Java syntax explanation in a reference blog that does not exist in the language ("`*var` returns the hashcode") was reported with a question about dropping it.
- Why: a rendered slide states sourced facts and inferences with the same confidence. The distinction survives only if the generator marks it at the text stage.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Let the LLM Pick Evidence IDs and Let Code Fill Quotes and Numbers]], [[Ask Only at Hard-to-Reverse Forks and Proceed on Disclosed Assumptions]], [[Never Trust PDF Table Extraction Without Cross-Checking the Prose]]
