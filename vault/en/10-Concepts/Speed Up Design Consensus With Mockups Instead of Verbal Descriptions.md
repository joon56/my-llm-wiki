---
title: Speed Up Design Consensus With Mockups Instead of Verbal Descriptions
tags:
  - dev/workflow
  - design/process
status: distilled
publish: true
lang: en
translation: 10-Concepts/말로-설명하는-대신-시안을-띄워-디자인-합의-속도-높이기
created: 2026-07-26
sources: []
---

## Summary

Don't make people choose a design direction from a verbal description — render 2-4 small mockups side by side and let them pick from those. Consensus forms faster, and interaction signals like clicks and hesitation reveal preferences even before an explicit answer does.

## Details

- Describing "dark navy with electric blue accents" versus "paper texture with serif type" in words leaves everyone picturing something different — that's why "this isn't what I meant" shows up after the pick.
- Practical method (actually used to decide this wiki's theme):
  1. Render the same content (an identical wiki page) as a mini mockup for each candidate direction, shown side by side
  2. Limit choices to 2-4 options, each with a one-line trade-off stated
  3. Once a direction is picked, compare intensity variants within it (pure vs. soft) — go from big direction to detail, in that order
- Side effect: if clicks get logged, preference shows up before the explicit answer — repeatedly clicking one mockup is effectively a decision already made. You can reframe the question ("why does C split opinion?") to get to certainty faster.
- Condition: mockup fidelity only needs to match the question — color and typography decisions don't need a polished prototype; an inline-styled mini mockup is enough.
- After a mockup is picked, the next step is an "improvement switchboard" prototype: eight improvements toggle on and off one by one for before/after comparison, and clicking "use this combination" on the preferred set records the choice. The top dropdown menu and three color schemes were also made clickable instead of described.
- Feel beats the recommendation: A was recommended out of three, but after trying them the user picked B as "easier to recognize at a glance". Give a recommendation with its reasons, but take the decision after the person has touched the options.
- The prototype becomes the spec: it covered the whole flow from sign-up through closing, matching, and the next round, 37 scenarios were checked automatically, and the 8 design rules settled there (numbered so they could be amended by number) became the implementation baseline.

## Sources
- Related: [[Why High-Contrast Brutalist UI Does Not Suit Long-Form Content]]
