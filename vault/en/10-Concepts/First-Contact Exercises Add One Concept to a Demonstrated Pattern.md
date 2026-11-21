---
title: First-Contact Exercises Add One Concept to a Demonstrated Pattern
tags:
  - work/teaching
  - dev/workflow
status: distilled
publish: true
lang: en
translation: 10-Concepts/처음-배운-개념의-실습은-시연한-패턴에-하나만-더-얹는다
created: 2026-11-21
sources: []
---

## Summary

If learners must fill in blank code for concepts they met that same day, **the moment one person gets stuck, every later step collapses** — so the facilitator demonstrates the base form, learners repeat the same pattern on a different target while adding exactly one concept, every intermediate state runs, and there is a checkpoint where stragglers can rejoin.

## Details

- The draft's failure mode: beginners were to fill all four TODOs themselves (constructor → object → inheritance → polymorphism) in a 23-minute exercise. The user pointed out that writing code for concepts not yet taught would be too hard — anyone stuck on TODO 1 never starts the rest.
- Change the goal from "write it yourself" to "follow, tweak, see the result": blanks at word level instead of line level (the `extends`, `super` and `@Override` slots), new classes made by copying an example file and changing three spots, and two-stage hints (an analogy, then near-final code).
- Pairing (the user's idea): TODOs come in pairs where the second is "the first one's pattern plus one extension." Switching the target from the hero side to the monster side repeats the same pattern, so the halves balance naturally (about 6 and 12 lines), and the second TODO's hint is just "same pattern as TODO 1." Each pair adds exactly one new concept (overloading, then polymorphism).
- The facilitator demonstrates the base form: TODOs 1 and 3 are typed live on screen, and learners do only TODOs 2 and 4, reusing a pattern they just watched.
- Tune the outcome so it shows why the concept is needed: the first draft had the warrior lose to the dragon alone and win once a mage was built through inheritance; the final version cut the dragon's HP from 250 to 180 so the warrior and mage win by a hair. The closing line is "we didn't touch a single line of battle code, yet only the dragon attacks differently" (polymorphism).
- Every intermediate state runs: running with the blanks untouched exits cleanly ("characters created: 0"), and word-level blanks that would break compilation sit inside comments to be "filled in, then uncommented." Learners who fall behind import a mid-point project (TODOs 1–2 done) and rejoin at the next demo.
- Distribution and script are part of the design: ship the code as a zipped IDE project that opens with a single Import (pasting into a new project means also warning about beginner traps such as the generated module-info file). The script covers what to say, what to show, the expected output, the hint to put up after a few minutes, a helper's "error message → cause → fix" table, and what to cut if time runs over.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Anchor Beginner Explanations in What They Can Try Now, Not Future Payoff]], [[Blank-Slate Questions Invite Silence - Ask With Options]]
