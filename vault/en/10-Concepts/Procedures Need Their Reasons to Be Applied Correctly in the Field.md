---
title: Procedures Need Their Reasons to Be Applied Correctly in the Field
tags:
  - work/communication
  - dev/docs
status: distilled
publish: true
lang: en
translation: 10-Concepts/절차에-이유를-적어야-현장에서-맞게-응용된다
created: 2026-11-21
sources: []
---

## Summary

When a procedure or an answer says only *what* and leaves out *why*, **people generalize the steps wrongly and keep asking the same question** — give the purpose first, then an analogy or a picture, and the details last.

## Details

- The case: an experiment protocol said only "photograph the start and end of the timed segment", with no reason. The person carrying it out asked four times in a row — "what are the photos for?" → "so I photograph the start and end of the route?" (wrong) → "I don't understand what 'timed segment' means" → "but I'd have to take the phone out during the recording to take a photo?" (clashing with the no-handling-during-recording rule).
- Once the purpose was stated, the details fell out by themselves: the photos exist so that every trial stops at the same spot, and so that someone can later match the spot to the map. That implies "once, today, while not recording, two photos, stored outside the repo."
- Explain terms as definition → why → numeric example → how to measure: "song transition gap" was first used as a bare term and drew a follow-up question. The re-explanation: "the silence from one song's end to the next one's start. It is not in the sensor data, so song boundaries are computed, and 2 s per gap pushes the fourth song 6 s late. Time it at home with a stopwatch."
- Analogies and pictures beat definitions: one sentence — "the timed segment is a highway average-speed check (known length ÷ transit time)" — and a sketch `start ── [segment start ═ 200 m ═ segment end] ── finish` landed before any long explanation did.
- Answers built on document IDs lose the big picture: after a run of replies citing decision and check numbers, the request came: "I don't understand the whole thing — draw it like a map." A one-page HTML map of each experiment's purpose, hypotheses, measurements, and theory links followed, with chips separating measured / computed / documented / opinion / not yet known.
- The same correction in another project: a team-facing status explanation of an app was called "too technical" and was rewritten as one-line definition → what it measures → what changed this time → principles → status → what teammates can do now.
- Field versions change form too: short lines that paste into a phone's notes app, in the order things happen (before leaving → recordings ①②③ → after returning), with one rule on top ("never take the phone out while recording").

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Speed Up Design Consensus With Mockups Instead of Verbal Descriptions]], [[Blank-Slate Questions Invite Silence - Ask With Options]], [[Anchor Beginner Explanations in What They Can Try Now, Not Future Payoff]]
