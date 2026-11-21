---
title: Paths and Scripts That Pass Through Bash on Windows Get Silently Mangled
tags:
  - tool/windows
  - tool/claude-code
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/Windows에서-bash를-거치는-경로·스크립트는-조용히-변형된다
created: 2026-11-21
sources: []
---

## Summary

On Windows, Claude Code runs hook commands and Bash-tool commands through Git Bash, so **unquoted backslash paths, heredoc scripts, and CRLF patches come out the other side as different strings** — and in a hook whose output no one watches, the result is a stop that leaves no trace. Write paths with forward slashes and quotes, and run scripts from files.

## Details

- Lead case (hook): a SessionEnd hook in `~/.claude/settings.json` was written as `C:\Users\<user>\...\python.exe C:\...\archive_session.py` with unquoted backslashes. Bash treated each `\` as an escape, so the command became `C:Users<user>AppData...python.exe: command not found` (exit 127).
- No trace was left: the script never started, so its own try/except error log was never written. The session-archive pipeline sat stopped for about two months (newest archive 10-02, noticed 11-21), and together with Claude Code's default 30-day transcript cleanup, sessions from roughly 10-05 to 10-21 were lost for good.
- Diagnosis: run the hook's exact command string through `bash -c '<command>'` with a sample JSON on stdin, and exit 127 reproduces. Running the same script directly works — the command string is broken, not the script.
- Fix and watch: rewrite the paths with forward slashes and quotes (`"C:/Users/<user>/.../python.exe" "C:/.../archive_session.py"`). Then, on every periodic run, compare the newest archived date with today so a stalled pipeline is noticed within days.
- Same family, heredoc backslashes: in a script passed to the Bash tool through a heredoc, backslashes were halved and a regex broke. This matches bash's handling of an unquoted delimiter (`<<EOF`), which turns `\\` into `\`.
- Same family, parsing and line endings: inline heredoc scripts containing quotes and special characters failed to parse twice, and in a repo whose working tree is CRLF (`core.autocrlf=true`) patch scripts broke line endings twice. Rules: new files can be written with LF because git normalizes them; patch existing CRLF files from Python with `open(..., newline='')` and explicit `\r\n`; never carry `\r\n` through a heredoc.
- Common fix: for anything that crosses bash, write paths with forward slashes and quotes, and write scripts and patches to a file with a file-writing tool before running them. Skipping the shell's quoting rules removes all three symptoms at once — the same lesson as the cp949 pitfalls: route text around shell boundaries through files.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Debug Plugin Hooks by Running Them Manually From the Cache]], [[Fire-and-Forget Hooks Fail Silently]], [[Windows cp949 Encoding Pitfalls]]
