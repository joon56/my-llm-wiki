---
title: LLM MOC
tags:
  - moc
publish: true
lang: en
translation: 50-MOC/LLM-MOC
created: 2026-07-26
---

# LLM MOC

Entry points by topic. As concept notes accumulate, they get sorted and linked here.

## RAG

## Prompting

- [[Prompt Caching]]
- [[Prompt Overload Makes Small LLMs Narrate Instead of Calling Tools]]

## Local LLMs & Agents

- [[Small LLM Tool Chaining Is Solved by Agent Separation, Not Prompting]]

## Fine-tuning

## ML & Data Analysis

- [[More Features Can Lose - Group Ablation and Complementarity]]
- [[Bridge Joins Connect Tables Without Shared Keys]]
- [[Block Temporal Leakage With a Feature Cutoff Rule]]
- [[The Train-Validation Metric Gap Signals Overfitting]]
- [[Transformers on Small Data Memorize Noise]]
- [[Compare Small-Data Neural Nets With Multi-Seed Averages]]
- [[Reverse-Engineer Undocumented Datasets With Statistics]]

## Dev — Security

- [[Authorization Must Not Trust Client Input]]
- [[Refresh Token Rotation Is Vulnerable to Concurrent Calls]]
- [[Secrets Pasted Into Chat Persist in Session Logs]]
- [[Pre-Publication PII and License Sweep Checklist]]
- [[Remove PDF PII With True Redaction, Not Overlays]]

## Dev — Database

- [[Wrap SQL Scripts in a Transaction to Surface the First Error]]
- [[Store Timezone-Offset Data as TIMESTAMPTZ]]

## Dev — Debugging & Verification

- [[JS-Rendered Sites Are a Blind Spot for Static Fetch Verification]]
- [[Verify Background Process Termination by Checking the Port]]
- [[Verify Backup Creation Immediately After Running a Destructive Script]]
- [[DOM Measurements Outrank Visual Overflow Judgments]]
- [[Verify Accessibility Contrast by Calculation Rather Than by Eye]]
- [[Visually Review Generated Charts by Reading the Image]]
- [[Offline HTML Copies May Lack Required Meta Tags]]

## Dev — Architecture

- [[Data Architecture That Generates Derivatives From a Single Source of Truth]]
- [[Client-Persisted IDs Are Immutable Contracts]]
- [[Seed Migrations Separate Content Updates From User State]]
- [[Verify Version Drift Between Planning Docs and Final Deliverables]]
- [[A Single HTML File With Base64 Assets Is Deployment Without a Server]]
- [[Notebooks Are Artifacts - the Source Is a Generator Script]]

## Design & UX

- [[Why High-Contrast Brutalist UI Does Not Suit Long-Form Content]]
- [[Speed Up Design Consensus With Mockups Instead of Verbal Descriptions]]

## Research & Writing

- [[Never Trust PDF Table Extraction Without Cross-Checking the Prose]]
- [[Joint Test Significance Is Not the Same as Individual Coefficient Significance]]
- [[Photo Conventions for Academic and Big Tech Career Documents Abroad]]
- [[Port Psychometric Instruments by Behavioral Proxies, Not Item Translation]]

## Product & MVP

- [[Each MVP Round Tests One Core Risk Hypothesis]]
- [[Infer Unmeasurable Phenomena from Combined Indirect Signals]]
- [[Judge Tool Overlap by Output Type, Not Category Labels]]

## Tools

- [[gitignore Does Not Stop Already-Tracked Files]]
- [[External URL References in CLAUDE.md Are Not Auto-Loaded]]
- [[claude.ai and Claude Code Have Separate Skill and Plugin Systems]]
- [[Windows PowerShell Execution Policy Blocks npm Global CLIs]]
- [[Create and Push a GitHub Repo With Only a PAT]]
- [[Windows cp949 Encoding Pitfalls]]
- [[Grep Installed Sources for Undocumented APIs]]
- [[Handle Third-Party Installs via Dry-Run and Install-State]]
- [[Resolve Name Collisions by Renaming, Not Priority Testing]]
- [[Compare Tool Profiles by Install-Plan Diff, Not Module Names]]
- [[Daemon Lifecycle and Data Persistence Are Separate]]

## Claude Code

- [[Plugin Slash Commands Are Namespaced]]
- [[plugin uninstall Ignores the Marketplace Qualifier]]
- [[Skill Risk Scales With Auto-Invocable Count]]
- [[Skill Selection Competition Is a Silent Probability Game]]
- [[Skills Are Probabilistic, Hooks Are Deterministic]]
- [[Always-Loaded Instruction Files Can Conflict]]
- [[Skills Come From Two Sources - Personal Folder and Plugin Cache]]
- [[Installing a Plugin Does Not Start Its Server]]
- [[Fire-and-Forget Hooks Fail Silently]]
- [[Debug Plugin Hooks by Running Them Manually From the Cache]]
- [[Session Transcript JSONL Is a Reusable Asset]]
- [[Bridge Sessions With a Project Memory Directory]]
- [[Parallelize ML Experiments With Background Execution]]
- [[Same-URL Artifact Redeployment Enables Incremental Approval]]
- [[Codify Constraints as Forbidden-Allowed Lists Before Work]]

## Automation & Pipelines

- [[Split Web Research Into Verifier and Discovery Agents]]
- [[Passed Deadlines Get Extended - Schedule Facts Need Re-Verification]]
- [[Secret Scans Must Fail the Pipeline, Not Just Warn]]
- [[The Recursive Contamination Trap of Tools That Consume Their Own Logs]]
- [[A Pipeline That Turns YouTube Videos Into LLM-Readable Material]]
- [[Multi-Source Documentation by Per-Source Study and Diff Merge]]
- [[Read Large PDFs Token-Efficiently With a PyMuPDF Fallback]]
