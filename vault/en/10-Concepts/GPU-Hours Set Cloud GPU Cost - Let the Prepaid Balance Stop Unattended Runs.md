---
title: GPU-Hours Set Cloud GPU Cost - Let the Prepaid Balance Stop Unattended Runs
tags:
  - infra/cloud
  - ml/training
  - dev/workflow
status: distilled
publish: true
lang: en
translation: 10-Concepts/클라우드-GPU-비용은-GPU-시간이-정한다-—-무인-구간은-잔액으로-끈다
created: 2026-11-21
sources: []
---

## Summary

Cloud GPU cost is **essentially fixed by the remaining work (GPU-hours) × the rate, so adding pods makes a job faster, not cheaper**. When nobody is awake, cost is decided by who turns the machines off — design the prepaid balance as the kill switch and pull results often so an abrupt stop loses nothing.

## Details

- Cost formula: cost = GPU count × hours on × rate. With about 20 GPU-hours of work left, one 4-GPU pod (5 h × \$8) and two of them (2.5–3 h × \$16) both come to about \$40; the second pod only adds about \$3 for setup and weight downloads. Answering "wouldn't another pod be cheaper?" with this arithmetic let the user pick two pods for speed.
- User correction: when Claude suggested topping up overnight, the user pointed out, "I need to sleep — if I top up, nobody can stop the pods and the money burns." The jobs would finish in the early morning, after which two idle pods would drain \$16 an hour, and the agent could not stop them because reading the key needed to stop a pod was blocked as sensitive.
- Design: treat the prepaid balance as both spending cap and automatic kill switch. Size it to run out right after the work finishes and pull results to the local machine every 10–20 minutes until then; when every pod stopped on an empty balance, no data was lost.
- Any step that needs a human breaks in an unattended window: the plan "the user stops the old pods right after the data is pulled" never ran because the user was asleep. Pods share one balance, so new money feeds idle pods — the remaining work was moved onto the running pods so the balance would run out just as the work ended.
- Save granularity: a job that only saves when a whole batch finishes loses everything when the budget cuts out. Before the balance ran out, a full generation run that was one-third done was stopped and replaced by a core subset split across 4 GPUs that saved every 12 problems.
- When the budget is short, cut by value per GPU-minute: kill jobs already shown to carry no signal first and protect the work that matters most for evaluation. Shrinking an expensive model's run to the core problems saved about \$20, and since multi-GPU pods bill idle GPUs too, tail work goes to a single-GPU pod.
- Stop and Terminate differ: Stop halts the pod but keeps the volume; Terminate deletes the volume too. Never terminate before confirming that the results have been pulled.
- Decision aid: putting the quality cost of not topping up (about 1–2 points) next to the luck-driven swing of a small test set (±7–9 points) makes it easy to judge whether the extra spend is worth it.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Daemon Lifecycle and Data Persistence Are Separate]], [[Parallelize ML Experiments With Background Execution]]
