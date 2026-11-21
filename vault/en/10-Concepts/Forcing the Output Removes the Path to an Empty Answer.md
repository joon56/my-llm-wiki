---
title: Forcing the Output Removes the Path to an Empty Answer
tags:
  - llm/prompting
  - llm/local
  - ml/evaluation
status: distilled
publish: true
lang: en
translation: 10-Concepts/출력을-강제하면-빈-답을-낼-길이-사라진다
created: 2026-11-21
sources: []
---

## Summary

Pinning the start of a speech model's output to Korean stopped transcripts from coming out in the wrong language, but it also took away the model's option to say "no speech", so it invented sentences from silence and breathing. **Use forced output only as a fallback, and filter inputs that should produce no answer outside the model.**

## Details

- Symptom: in the first real-user demo, the speech recognizer (Qwen3-ASR 1.7B on llama-server) transcribed short interjections as `嗯。`, `哦。`, and `Yeah.`. The request carried no language, so the model guessed one per segment; in that mode 16 of 48 interjections came out as Chinese characters or kana.
- First fix: an assistant prefill (`language Korean<asr_text>`) pinned the output to Korean, and foreign-language output dropped to 0/48. Only the three problem utterances were compared before and after.
- Side effect (found six days later while comparing another model): silence produced a made-up sentence ("For his wife, he...") and breathing or brief noise produced "Yes." — on all four silence/noise samples. A stray "Yes." in a consultation record can read as consent. Pinning the start of the output also removes "empty output" as an option.
- Second fix (two-step query): let the model pick the language first; keep Korean as-is, leave "no speech" blank, and re-ask with Korean forced only when another language comes out. Foreign output stayed at 0/48, hallucinations fell from 4/4 to 0/4, and accuracy was unchanged. The cost was 258 → 325 ms on average per segment, with re-asks on 1 in 3 interjections and on no normal sentences.
- Put the real fix outside the model (the user's correction): if production will switch to an external speech API, model-specific prompt tuning will soon be thrown away. Filtering silence and noise in front of the model (a browser VAD, e.g. Silero VAD at about 2 MB) survives any model or API swap and cuts cost for APIs billed by audio length.
- Give the filter its own pass criteria first: a short "yes" signals consent and must never be dropped, so the bar is "lose 0 of 48 interjections, block all silence and noise". The old filter checked loudness only, so even a faint sound around -50 dBFS went to the model once it lasted 0.3 s.
- Generalize: after any fix that forces the output format, language, or prefix, regression-test not only the original failures but also inputs whose correct answer is empty (silence, blank input, irrelevant input). A JSON schema or forced choice with no "not applicable" slot carries the same risk.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Finalize Model Choice by Measuring on Your Own Data and GPU, Not Public Benchmarks]], [[Small LLM Tool Chaining Is Solved by Agent Separation, Not Prompting]], [[Passing Synthetic-Input Tests Is Not Real-World Readiness]]
