---
title: Space Freed by Deleting Comes Back - Relocate Where It Accumulates
tags:
  - tool/windows
  - dev/tooling
status: distilled
publish: true
lang: en
translation: 10-Concepts/지워서-얻은-용량은-돌아온다-—-쌓이는-위치를-옮긴다
created: 2026-11-21
sources: []
---

## Summary

Space recovered by deleting caches and temp files comes back within weeks. **To stop the recurrence, measure the growth sources (work-folder tmp, caches, agent outputs) and move where they are created off the system drive with persistent settings.**

## Details

- Timeline: cleaning caches, Temp, and conda raised free space on C: from 12.7 GB to 29.7 GB. Eleven days later it was about 15.8 GB; moving the SDK, the Gradle cache, and the AVDs to another drive brought it to 19.0 GB, but seven days after that it was 0.8 GB — the 17 GB won by deleting did not last three weeks.
- What came back (measured): Temp went from 3.3 GB deleted to 6 GB, the npm cache from 2.5 GB deleted to 2.25 GB, the editor's extension-installer cache from 0.59 GB to 1.2 GB, and the GPU shader cache from about 2 GB back to 1.3 GB.
- The biggest growth source was not a cache: one work folder's tmp (experiment virtualenvs and pip caches) was 22.6 GB, and temp files left by tests in another agent session's scratchpad were 2.3 GB. Re-running the same cleanup list never reveals growth sources like these.
- Control group: the SDK, Gradle cache, and AVDs that were relocated via environment variables (`ANDROID_HOME`, `GRADLE_USER_HOME`, `ANDROID_AVD_HOME`) did not pile up on C: again. The npm cache, moved only with a one-off flag (`npm install --cache ...`), piled up again at its default path.
- The fix is relocation: use persistent settings such as `npm config set cache <path on another drive> --location=user`, and move large tool folders (editor extensions, other tools' runtime caches) and link them back with a junction. Move large projects to an ASCII path on the work drive, and reserve deletion for Temp.
- Measurement order: sort the user profile's top-level folders by size, then break the top entries into sub-units such as tmp, .git, and .venv. Decide delete / relocate / keep for each and build a table ordered by impact.
- What is safe to delete is decided by regenerability ([[Classify Disk Cleanup by Regenerability, Not Folder Names]]). The rule to add here is to avoid what is in use right now: skip and list whatever running processes hold (`npm-cache\_npx` used by MCP servers, an open browser's cache), and in Temp areas used by concurrently running agent sessions, delete only large files untouched for three days or more.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Classify Disk Cleanup by Regenerability, Not Folder Names]], [[Moving a Folder Breaks State Keyed by Its Path]], [[Remembered Environment State Is a Hypothesis - Measure Before Acting]]
