---
title: Notebooks Are Artifacts - the Source Is a Generator Script
tags:
  - tool/jupyter
  - dev/workflow
  - ml/training
status: distilled
publish: true
lang: en
translation: 10-Concepts/노트북은-산출물이고-소스는-생성기-스크립트다
created: 2026-08-04
sources: []
---

## Summary

Never hand-edit an .ipynb — treat a generator script as the single source of truth: `make_notebook.py` builds the notebook with nbformat, `jupyter nbconvert --execute` runs it, and nbformat parses the output cells to verify results, so notebook, code, and outputs can never drift apart.

## Details

- An ipynb is a blob of JSON, which makes direct editing risky (cell IDs, execution counts, output metadata) and easily produces a "lying notebook" whose outputs no longer match its code.
- The pipeline: `make_notebook.py` builds the notebook programmatically with nbformat → `jupyter nbconvert --to notebook --execute --inplace` runs it end to end → nbformat parses the output cells to check results (accuracy, loss curves, etc.).
- Every change request (e.g. adjusting the number of epochs) is handled by editing the script, then regenerating and re-executing. The notebook is never patched in place.
- This keeps all three — notebook file, source code, and execution outputs — pointing at the same version at all times; drift becomes structurally impossible.
- Because verification is automated too, "the results changed after running" is caught by the script before a human ever opens the notebook.
- When the adopted approach changes, sync the explanation document in the same unit of work — regenerating only the notebook while neglecting the doc just moves the drift into the documentation.

## Sources
-
