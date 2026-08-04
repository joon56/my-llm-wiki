---
title: Transformers on Small Data Memorize Noise
tags:
  - ml/overfitting
  - ml/data
status: distilled
publish: true
lang: en
translation: 10-Concepts/소데이터에-Transformer를-쓰면-노이즈를-암기한다
created: 2026-08-04
sources: []
---

## Summary

At around 2.5K samples, a Transformer's attention capacity goes into memorization rather than generalization — the diagnosed failures were input-construction problems, not architecture problems, and the fix belongs to the inputs.

## Details

- Context: two failure modes were diagnosed while using a Transformer-style model for NHIS hospitalization prediction (2,532 patients).
- Failure 1 — fake sequences: feeding an unordered bag of diagnosis codes as a sequence, with positional embeddings on top, makes the model memorize an "order" that does not exist. The listing order of codes is meaningless, yet position becomes a learnable signal.
- Failure 2 — preprocessing leakage: fitting the vocab and StandardScaler on the full dataset before the train/val split leaks validation information into training. Fit on train only; transform both.
- Common principle: with ~2.5K samples, attention's representational capacity flows into memorizing noise instead of learning signal. The smaller the data, the larger the share of spurious patterns available to memorize.
- Prescription: fix the inputs, not the architecture — represent unordered data without order (aggregates, bags) and run preprocessing through a leakage-free pipeline.
- Generalization: much of "the model is acting weird" is not a model problem but a mismatch between the input representation and the data's actual structure.

## Sources

- Related: [[The Train-Validation Metric Gap Signals Overfitting]]
