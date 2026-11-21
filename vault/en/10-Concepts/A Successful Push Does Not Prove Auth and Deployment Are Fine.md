---
title: A Successful Push Does Not Prove Auth and Deployment Are Fine
tags:
  - tool/git
  - tool/windows
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/푸시-성공은-인증·배포가-정상이라는-증거가-아니다
created: 2026-11-21
sources: []
---

## Summary

Two calls — "the push worked, so git is fine" and "the live site is just cached" — were both wrong: duplicate credentials were triggering account-picker popups, and the Pages deployment was stuck in the queue. **Check transport, authentication, the deploy queue, and the live site as separate layers.**

## Details

- What happened: after pushing updated data for a static site, the agent judged from the push output alone that git was fine and said the stale live site was waiting on deployment and cache. Only after the user pointed out again that the account prompts kept failing were auth and deployment state queried directly — and both calls turned out wrong.
- Cause 1 (auth): Windows Credential Manager held the same account twice, as `git:https://<user>@github.com` and `git:https://github.com`, so Git Credential Manager asked the user to pick an account on every authentication (trace log: `Multiple accounts available - prompting user to select one`). The push itself succeeds, so command output never shows the problem.
- Fix 1: with the user's approval, delete the duplicate with `cmdkey /delete:"LegacyGeneric:target=git:https://<user>@github.com"`, then retest read and push with `GIT_TERMINAL_PROMPT=0` and `GCM_INTERACTIVE=never`. That mode fails immediately instead of opening a window, so the agent can see auth problems itself.
- Cause 2 (deploy): the commit was on the remote, but the Pages deployment had been `queued` for about 21 minutes while the GitHub status page showed Pages and Actions as healthy — the whole service can be green while your one deployment is stuck. Empty output from `gh run list` meant "unknown", and attaching "cache" to it was where the misdiagnosis began.
- Fix 2: re-trigger the deployment with an empty commit, then poll in the background, with a cap of about 13 minutes, until the live page shows the new date string. It went live, but it is unclear whether the re-trigger or the queue clearing did it; the next round's deployment finished in 25 seconds.
- Deployment is done when production shows the new version's marker (the data-update date, a new JS hash, a new string inside the bundle), not when the push exits 0.
- Principle: when the cause is unknown, say "unconfirmed" and query that layer instead of offering a plausible story. Never rebut a symptom the user sees (popups) with a success signal on your side (exit 0).

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Verify Background Process Termination by Checking the Port]], [[Create and Push a GitHub Repo With Only a PAT]], [[Remembered Environment State Is a Hypothesis - Measure Before Acting]]
