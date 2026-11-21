---
title: Moving a Folder Breaks State Keyed by Its Path
tags:
  - tool/windows
  - dev/tooling
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/폴더를-옮기면-경로를-키로-쓰는-상태가-끊긴다
created: 2026-11-21
sources: []
---

## Summary

Moving a project or tool folder to another drive **silently breaks every piece of state keyed by its path** — virtualenvs, hard-coded paths, agent session history. List them first, then move in make-before-break order: copy -> compare -> switch over -> verify it works -> delete the original.

## Details

- Path-keyed state to inventory before moving: Python venvs (absolute paths are baked in, so they will not run after a move — recreate them at the new location), hard-coded paths in scripts, notebooks, docker files, and IDE settings (grep for `C:\Users\<user>`), SDK paths recorded in IDE and tool settings, and absolute paths written inside memory notes.
- Agent history is path-keyed too: Claude Code keeps session history and memory under `~/.claude/projects/<encoded path>`, so a moved folder is treated as a new project and its memory and `--resume` history disappear. Copy the old directory to the new path's name to reconnect them.
- File locks: shut down the IDE, the Gradle daemon, adb, node, and agents first — an idle Gradle daemon and the adb server really were holding SDK files. A folder the current session is using cannot be moved mid-session.
- Order (make-before-break): copy -> compare file counts and bytes -> switch the settings over (back up the settings files first) -> verify it works at the new location -> delete the original (confirming once more right before). Never delete the original before verification is done.
- An actual SDK move: after robocopy, file counts of 39,820 and 19,785 matched (robocopy exit code 1 means "files were copied", not failure). The C: originals were deleted (3.2 GB freed) only after editing two IDE settings files, setting user environment variables, and confirming that the SDK at the new location recognized its 8 packages. IDEs and editors must be restarted to pick up new environment variables.
- Transferring access follows the same principle: when handing over ownership of a cloud project, "verify the new owner's real access before removing the old account" was fixed as the order. CLI login, a database read, a dry-run security-rules deploy, and the IAM role were all checked, followed by an app-login regression check.
- Environment conditions: use ASCII target paths (Korean characters in a path break the Android build tool AAPT2). If free space is near zero, clear Temp before moving — even when the copy goes to another drive, the editor and agents keep writing to C:, so writes can fail midway.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Verify Backup Creation Immediately After Running a Destructive Script]], [[Bridge Sessions With a Project Memory Directory]], [[Space Freed by Deleting Comes Back - Relocate Where It Accumulates]]
