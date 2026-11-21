---
title: When a Build Works in the IDE but Fails in the Terminal, Check the Runtime First
tags:
  - tool/windows
  - dev/tooling
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/IDE에서-되는-빌드가-터미널에서-깨지면-런타임부터-본다
created: 2026-11-21
sources: []
---

## Summary

IDEs run on their own bundled runtime (JDK, Node, Python), while terminals and agent shells use the system runtime from PATH or `JAVA_HOME` — **when a build works in the IDE but breaks only in the terminal, suspect a runtime version mismatch before the code.**

## Details

- The symptom: when Claude Code ran `.\gradlew :app:assembleDebug :mobile:assembleDebug` in PowerShell, the build failed. The cause was the system default JVM 8 — inside Android Studio the bundled JDK (JBR) is used, so only IDE builds worked.
- The fix: point at the IDE's JBR with `$env:JAVA_HOME = 'C:\Program Files\Android\Android Studio\jbr'` and rebuild; both the watch app APK (34.4MB) and the phone companion APK (10.1MB) came out.
- Cleanup commands need it too: stopping the daemons afterwards with `gradlew --stop` also required setting `JAVA_HOME` again. The agent shell does not keep environment variables between commands, so set it on the same command line.
- Write it down or repeat it: right after the fix, the rule was saved as a project memory file (`gradle-needs-jbr-java-home`), so the next session does not start from the same failure.
- Diagnosis order: compare `java -version` (or `node -v`, `python --version`) in the terminal with the runtime path configured in the IDE. If they differ, pass the IDE's path through the environment variable and reproduce.
- Generalization: bundled versus system runtime is not an Android-only problem. It is the first suspect whenever something "works in the IDE but not in CI, the terminal, or an agent."

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Windows PowerShell Execution Policy Blocks npm Global CLIs]], [[Bridge Sessions With a Project Memory Directory]], [[Paths and Scripts That Pass Through Bash on Windows Get Silently Mangled]]
