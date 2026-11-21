---
title: Finalize Model Choice by Measuring on Your Own Data and GPU, Not Public Benchmarks
tags:
  - ml/evaluation
  - llm/local
status: distilled
publish: true
lang: en
translation: 10-Concepts/모델-선정은-공개-벤치마크가-아니라-내-데이터·내-GPU-실측으로-확정한다
created: 2026-11-21
sources: []
---

## Summary

The top candidates picked from public numbers — for both speech recognition and summarization — lost when measured in the target language on the GPU that would actually run them. **Use public benchmarks only to shortlist; finalize with a domain test set and switch criteria written down before measuring.**

## Details

- Real case: choosing local models for a remote consultation app, public numbers pointed to Cohere Transcribe for speech (English average WER 5.42 vs 7.44 for Whisper large-v3) and Qwen3.8-27B Q4 (~18 GB) for summarization. Public leaderboards had no Korean numbers, so the pick was marked "confirm by measurement", and on an RTX 3070 8 GB both lost.
- Change the language and the ranking changes: Korean public-speech CER came out Qwen3-ASR 1.7B 3.81%, Whisper turbo 4.10%, Cohere 8.05%. English WER rankings do not carry over to other languages.
- VRAM fit decides speed: the 27B Q4 spilled past 8 GB into system RAM and took 6-10 minutes per dialogue, while the adopted Gemma 4 12B reached 100% fact recall at about 100 seconds per dialogue. A smaller 9B invented content, and one candidate could not even be measured because the inference engine (llama.cpp) did not support it — neither fact appears on a public leaderboard.
- Measure the failures that average error rates hide: Whisper variants produced "Thank you." from silence, "Amen" from noise, and "Thank you for watching." from breathing, and errors clustered on domain keywords (the Korean words for "barks" and "mat" turned into similar-sounding unrelated words). So the metrics gained "characters outside the target language" and "hallucinations on silence/noise", and the test set became 24 interjections × 2 conditions (clean, phone-like noise), 30 domain sentences, and 200 public speech clips.
- Write switch criteria before measuring: for a new candidate (Whisper turbo Q5) the rule was declared up front — fewer interjection errors and foreign-language outputs than the incumbent, public/domain CER no more than 0.5 pp worse, no more hallucinations; miss any one and the incumbent stays. Interjection CER of 24.6% vs 68.3% and domain CER of 1.2% vs 4.2% settled it without debate (Q5's only advantage was GPU memory, 4.2 → 1.8 GB).
- Pin what you download: 18 models and binaries (55 GB), including third-party GGUF conversions, are listed in a manifest with size and SHA-256. A different file under the same name cannot silently change the results.
- Tag results with their conditions: state "synthetic / read-aloud speech", and report even a single acceptance-criterion miss (term recall one item lower out of 95) instead of hiding it, leaving it as a target for re-verification on real speech.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[A Leaderboard Submission Is a Pre-Registered Experiment]], [[Forcing the Output Removes the Path to an Empty Answer]], [[Passing Synthetic-Input Tests Is Not Real-World Readiness]]
