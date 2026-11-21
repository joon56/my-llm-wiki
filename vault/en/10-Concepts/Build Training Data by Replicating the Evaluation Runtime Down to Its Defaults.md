---
title: Build Training Data by Replicating the Evaluation Runtime Down to Its Defaults
tags:
  - llm/pipeline
  - ml/data
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/학습-데이터는-평가-런타임을-기본값까지-복제해-만든다
created: 2026-11-21
sources: []
---

## Summary

An offline data-generation path (vLLM etc.) and the evaluation runtime (HF transformers etc.) **drift apart without raising errors — in tokenizers, sampling defaults, optional kernel packages, padding and budget units**. Diff the specs item by item and round-trip-check every text path before the training data gets contaminated.

## Details

- Trigger: the user asked "don't the model specs matter too?", which prompted an item-by-item comparison of checkpoint hashes, precision, context length and sampling settings against the evaluation environment. That comparison revealed that a generation job already running was consuming corrupted input.
- Tokenizer: transformers 5.x's default loader stripped every space from a DeepSeek-R1 distilled model's text, in both the evaluation-side and generation-side versions. The submission code's shared loader had an encode→decode round-trip check, but the separate data-generation script did not — the guard against a known trap existed on only one path. Passing token-id prompts built by the verified tokenizer to vLLM fixed it at a cost of about 10 minutes.
- Scope workarounds to the affected model: disabling tokenizer initialization globally broke generation for another model (Qwen3.5), whose multimodal processor requires the tokenizer. Restricting the exception to the one model fixed it.
- Sampling defaults: labels were generated with T=1.0, top_k 40, top_p 0.95, but one model's (Olmo) default generation config uses T=0.6. Leaving defaults in place silently samples from a different distribution, so the label-generation settings were pinned explicitly.
- Optional packages: without the `kernels` package, transformers dequantized gpt-oss's MXFP4 weights and ran out of memory; with a version outside the accepted range (0.15.x) the package was ignored and it ran out of memory again. Matching the version listed in the evaluation Docker image tag let the model load in its compressed format.
- Padding: when extracting hidden states in batches, left padding shifts token positions and the linear-attention recurrent state, corrupting the values. Only samples of the same problem — which share a prefix length — were batched together, with no padding.
- Feature definitions need the same conditions: the token cap was stored in the artifact so training and inference read the same value, and long training traces were cut again to the deployment cap (re-censoring) before computing features. A feature that cannot be reproduced under the deployment cap (forced-answer agreement) was dropped from model selection.
- Principle: list the evaluation environment's versions, defaults and optional dependencies, diff them line by line against the generation path, and put a round-trip check on every path text passes through. These mismatches never raise errors; they only change the training data quietly.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Block Temporal Leakage With a Feature Cutoff Rule]], [[Measure the Evaluation Server Budget With a Fixed-Prediction Dummy Submission]], [[Ranking Quality and the Decision Threshold Fail Separately]]
