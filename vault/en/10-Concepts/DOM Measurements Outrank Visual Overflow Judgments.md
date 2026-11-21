---
title: DOM Measurements Outrank Visual Overflow Judgments
tags:
  - dev/frontend
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/시각적-오버플로-판단보다-DOM-측정값이-우선한다
created: 2026-07-26
sources: []
---

## Summary

Don't conclude that a layout clipped in a screenshot is a CSS overflow bug — headless browsers often have a minimum window-width floor that distorts narrow-viewport screenshots, so the judgment call should come from a DOM measurement like `scrollWidth === clientWidth`.

## Details

- Some headless Chrome environments have a floor on window width (roughly ~500px) below which the requested viewport can't actually shrink. Even if you request a 375px mobile screenshot, the real render happens in a wider window, making the screen look clipped or misaligned.
- Misdiagnosing this distortion as "a bug causing horizontal scroll on mobile" leads you to break CSS chasing a bug that doesn't exist.
- The correct check: in the browser console/script, verify `document.documentElement.scrollWidth === document.documentElement.clientWidth`. If they're equal, there's no horizontal overflow — the screenshot artifact is a rendering-environment issue, however odd it looks.
- Generalization: a visual artifact (screenshot) is indirect evidence tangled up with rendering-environment constraints. The primary evidence for a layout judgment is the measurement the DOM itself reports.
- Build a failing measurement check even for visual bugs: a DOM baseline check before the fix flagged 3 cards with text-image overlap and 10 with covered photos, and after the fix the count of 0 was confirmed again on the production URL after deploy. UX diagnosis was done in numbers as well (a 360px sub-page hero pushed body text down to 524px; 39 places set 9-11px text). But for things numbers do not capture, such as image-compression quality, look at the screen separately.
- Same on Android: a color picker's selection ring did not show in screenshots, yet `uiautomator dump` reported checked=true. Since the state was fine, the problem narrowed to rendering (the background tint was painting over the ring), and moving the ring to the foreground fixed it.
- Automation can manufacture fake bugs: all three screenshots showed the detail screen, suggesting a back-navigation bug, but a coordinate tap meant to restore touch mode had reopened a card on the scrolled home screen (taps went by resource id from then on). A black screen was not a crash either — just a frame captured mid-transition.

## Sources
- Related: [[Verify Accessibility Contrast by Calculation Rather Than by Eye]]
