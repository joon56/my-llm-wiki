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
- [[Forcing the Output Removes the Path to an Empty Answer]]

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

## ML Experiment Methodology

- [[A Leaderboard Submission Is a Pre-Registered Experiment]]
- [[Switch Components Off on Purpose to Map Real-Data Loss]]
- [[Measure the Oracle Ceiling Before Implementing]]
- [[Swapping the Model Class Beats Adding Knobs]]
- [[Ask About Ambiguous Rules as a Pre-Approval Question]]
- [[Effects Smaller Than the Leaderboard Resolution Cannot Be Read]]
- [[Budget Remote Runtime by Resource-Type Multipliers and the Worst-Case Path]]
- [[Select Improvements the Leaderboard Cannot Read With an In-Submission Holdout]]
- [[Ranking Quality and the Decision Threshold Fail Separately]]
- [[Build Training Data by Replicating the Evaluation Runtime Down to Its Defaults]]
- [[Measure the Evaluation Server Budget With a Fixed-Prediction Dummy Submission]]
- [[Finalize Model Choice by Measuring on Your Own Data and GPU, Not Public Benchmarks]]
- [[GPU-Hours Set Cloud GPU Cost - Let the Prepaid Balance Stop Unattended Runs]]

## Research & Measurement

- [[Freeze the Analysis With a Tag, Then Compute Results Once]]
- [[Filling Unrecorded Conditions With Planned Values Fails Silently]]
- [[A Validation Reference Must Come From a Source Independent of What It Checks]]
- [[Judge an Error Against the Slack the Analysis Already Absorbs]]
- [[Augmented Trials Add No Information - Simulation Is for Testing Code]]
- [[Ratio Effect Metrics Shrink on Their Own as the Denominator Grows]]
- [[Messenger Transfers Change Video FPS - Verify Frames Against a Filmed Clock]]
- [[Check Field Data Per Trial Before Leaving the Site]]
- [[Mark Sensor Recordings With Body Actions, Not Device Handling]]

## Dev — Security

- [[Authorization Must Not Trust Client Input]]
- [[Refresh Token Rotation Is Vulnerable to Concurrent Calls]]
- [[Secrets Pasted Into Chat Persist in Session Logs]]
- [[Pre-Publication PII and License Sweep Checklist]]
- [[Remove PDF PII With True Redaction, Not Overlays]]
- [[Unfiltered Queries That Lean on RLS Leak on Admin Accounts]]

## Dev — Database

- [[Wrap SQL Scripts in a Transaction to Surface the First Error]]
- [[Store Timezone-Offset Data as TIMESTAMPTZ]]
- [[Sorting by a Sum Aggregate Lets Duplicate Rows Inflate Rankings]]
- [[Verify RLS and Triggers on a Real Engine Even Without DB Access]]

## Dev — Debugging & Verification

- [[JS-Rendered Sites Are a Blind Spot for Static Fetch Verification]]
- [[Verify Background Process Termination by Checking the Port]]
- [[Verify Backup Creation Immediately After Running a Destructive Script]]
- [[DOM Measurements Outrank Visual Overflow Judgments]]
- [[Verify Accessibility Contrast by Calculation Rather Than by Eye]]
- [[Visually Review Generated Charts by Reading the Image]]
- [[Offline HTML Copies May Lack Required Meta Tags]]
- [[Verify Textbook and Spec Tables With Structural Invariants and a Reference Model]]
- [[Coverage Proves Execution, Mutation Proves Checking]]
- [[Verify Paste Portability With a Clean Project and Encoding Matrix]]
- [[Passing Synthetic-Input Tests Is Not Real-World Readiness]]
- [[A Successful Push Does Not Prove Auth and Deployment Are Fine]]
- [[Tie Server Writes to User-Intent Events, Not Value Changes]]
- [[In a Cache-First Listener, Absence Is Unconfirmed Until the Server Answers]]

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

## Collaboration & Meetings

- [[Blank-Slate Questions Invite Silence - Ask With Options]]
- [[Meetings Are for Choosing, Not for Generating Ideas]]

## Teaching & Communication

- [[First-Contact Exercises Add One Concept to a Demonstrated Pattern]]
- [[Anchor Beginner Explanations in What They Can Try Now, Not Future Payoff]]
- [[Procedures Need Their Reasons to Be Applied Correctly in the Field]]

## Research & Writing

- [[Never Trust PDF Table Extraction Without Cross-Checking the Prose]]
- [[Joint Test Significance Is Not the Same as Individual Coefficient Significance]]
- [[Photo Conventions for Academic and Big Tech Career Documents Abroad]]
- [[Port Psychometric Instruments by Behavioral Proxies, Not Item Translation]]

## Product & MVP

- [[Each MVP Round Tests One Core Risk Hypothesis]]
- [[Infer Unmeasurable Phenomena from Combined Indirect Signals]]
- [[Judge Tool Overlap by Output Type, Not Category Labels]]
- [[Review Capacity-Based Matching Plans for Failure States and Demand Dilution First]]
- [[Record Deliberate Omissions and Their Reasons Next to the Code]]

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
- [[Paths and Scripts That Pass Through Bash on Windows Get Silently Mangled]]
- [[Classify Disk Cleanup by Regenerability, Not Folder Names]]
- [[Space Freed by Deleting Comes Back - Relocate Where It Accumulates]]
- [[Moving a Folder Breaks State Keyed by Its Path]]
- [[When a Build Works in the IDE but Fails in the Terminal, Check the Runtime First]]
- [[Commit a Starter Kit Untouched Before Customizing It]]

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
- [[superpowers Is a Work Habit, GSD Is a Project Framework]]

## Working With Agents

- [[Split Parallel Subagents by File Ownership and Keep Builds in the Main Session]]
- [[Ask Only at Hard-to-Reverse Forks and Proceed on Disclosed Assumptions]]
- [[Remembered Environment State Is a Hypothesis - Measure Before Acting]]
- [[Distill First-Round Trial and Error Into a Playbook for Repeated Work]]
- [[Give Independent Reviewer Agents the Source, Not Your Conclusions]]
- [[Example and Optional Items in a Spec Are Not Requirements]]
- [[Separate a Read-Only Question Session From the Working Session]]
- [[Generate Change Reports From the Diff, Not From Memory]]
- [[Make the LLM Flag Every Sentence Written Beyond the Source Material]]
- [[When Agent-Driven Research Stalls, Measure the Handoff Structure First]]
- [[Verify Round-Trip Identity Before Extracting Text for Human Edits]]

## Automation & Pipelines

- [[Split Web Research Into Verifier and Discovery Agents]]
- [[Passed Deadlines Get Extended - Schedule Facts Need Re-Verification]]
- [[Secret Scans Must Fail the Pipeline, Not Just Warn]]
- [[The Recursive Contamination Trap of Tools That Consume Their Own Logs]]
- [[A Pipeline That Turns YouTube Videos Into LLM-Readable Material]]
- [[Multi-Source Documentation by Per-Source Study and Diff Merge]]
- [[Read Large PDFs Token-Efficiently With a PyMuPDF Fallback]]
- [[Let the LLM Pick Evidence IDs and Let Code Fill Quotes and Numbers]]
- [[Decide Whether Work Was Done by Back-Referencing Outputs, Not Status Flags]]
