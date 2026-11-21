---
title: Passing Synthetic-Input Tests Is Not Real-World Readiness
tags:
  - dev/testing
  - dev/debugging
  - ml/evaluation
status: distilled
publish: true
lang: en
translation: 10-Concepts/합성-입력-테스트-통과는-실사용-준비-완료가-아니다
created: 2026-11-21
sources: []
---

## Summary

Synthetic inputs written by the author **only exercise the clean center of the distribution the author imagined** — before an irreversible field day or demo, meet the edge cases through a scaled-down rehearsal under real conditions and an independent review, and report synthetic and real-world verification separately.

## Details

- Case 1 (sensor experiment): analysis code that passed every end-to-end test built on synthetic signals failed one check after another in a solo real-world trial the day before the field session. Running flight was detected in 1 of 67 steps, jumps 0/3, sync hops 1/3, and brisk walking was classified as a leg-pendulum swing. A vertical acceleration of −0.8 g is below free fall (0 g) and therefore physically impossible for the body: it was the phone bouncing inside the waist pouch.
- Case 2 (video consultation app): an app that had passed 1,046 unit tests, 36 browser tests, and a one-hour continuous call — all with synthetic speech, saved video, and same-PC connections — showed four problems in its first demo with real people. Short real utterances were transcribed in another language, latency was about 600 ms through a free TURN relay (the tests had connected directly), a person truncated a long token link while copying it and got `Cannot GET /Join`, and one side produced zero transcript segments.
- The common cause is the input distribution: synthetic inputs cover only the center the author pictured — clearly enunciated sentences, complete URLs, one machine, a firmly mounted phone. The generator itself can be wrong as well: the "landscape" rotation matrix turned out to be a reflection (determinant −1).
- An independent review catches a different set of blind spots: a separate reviewer agent (about 25 minutes) found nine bugs the synthetic tests had missed — a crash converting blank cells to numbers that stayed hidden only because the log sheet was still empty, Korean labels all mapped to "mixed", an empty stage counted as "sync broken", pendulum cycles undercounted by one, and a crash on 2-3 s recordings. Each fix started with a reproducing test, and when random synthetic data would not reproduce a failure, the failing case's exact parameters (axis, damping, noise) were pinned into the test.
- A pass with the right count is more dangerous: in a second sync trial with less bounce, the old rule picked the second and third jumps plus a post-landing rebound (51 ms) and reported a normal-looking "3/3". Detection was switched to an event definition (push → below 0.2 g → landing impact), and the jump intervals are now printed so they can be cross-checked against the video.
- Reporting discipline limits the damage: every measurement table was labeled "all synthetic input" and a separate "not yet verified" list (real microphones, other networks, mobile browsers) was kept, and most demo failures came from that list. Promote user-perceived metrics to risks even when already measured: the relay round trip of about 570 ms had been measured, but only the median connection time was reported, so it first showed up as a problem in the demo.
- Rehearse under the real setup, before anything irreversible: a pre-check run with the actual pouch, headset, and screen off showed that 16-23 phone-insertion movements were counted as steps, putting the departure time at 9.2 s instead of 29.9 s, and the procedure was fixed before the main experiment. Bring real-world failures back into the synthetic regression set (e.g. a 48-item interjection test set), and output a blank plus a flag instead of a wrong number when a metric lacks support.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Give Independent Reviewer Agents the Source, Not Your Conclusions]], [[JS-Rendered Sites Are a Blind Spot for Static Fetch Verification]], [[Fire-and-Forget Hooks Fail Silently]]
