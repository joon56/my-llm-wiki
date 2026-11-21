---
title: Classify Disk Cleanup by Regenerability, Not Folder Names
tags:
  - tool/windows
  - dev/tooling
status: distilled
publish: true
lang: en
translation: 10-Concepts/디스크-정리는-이름이-아니라-재생성-가능성으로-분류한다
created: 2026-11-21
sources: []
---

## Summary

Do not clean up disk space in order of size. **Sort candidates by "what comes back and what is gone for good if I delete it" into three tiers — caches (regenerate automatically), reinstallable or regenerable, and unrecoverable — and never delete based on a folder's name alone.**

## Details

- Measured (22.8 GB free of 237.5 GB on C:): the big items were the hibernation file (`hiberfil.sys`) at 12.8 GB, the conda package cache at 12.0 GB, Android emulator system images at 7.2 GB, GPU shader caches at 5.6 GB, a browser's on-device AI model at 4.0 GB, the browser cache at 3.5 GB, emulator virtual devices (AVDs) at 2.9 GB, and the npm cache at 2.0 GB. Recoverable space was estimated at 45-50 GB; deleting only the items the user picked actually freed 33 GB.
- Tier 1 — caches that regenerate: deleting them loses no functionality; the next run is just a little slower. Shader and browser caches, `npm cache clean --force`, `conda clean --all`, and emulator quickboot snapshots (phone 2.6 GB, watch 2.0 GB) belong here.
- Tier-1 gains are temporary: snapshots are saved again every time the emulator shuts down, so an AVD folder trimmed to 0.76 GB was back at 2.9 GB about four weeks later (presumably re-saved snapshots). It only stops when you change how it is generated — the `-no-snapshot-save` option or turning quickboot off; space filling back up is the subject of [[Space Freed by Deleting Comes Back - Relocate Where It Accumulates]].
- Tier 2 — reinstallable or regenerable, at a cost: the hibernation file is turned off with an admin `powercfg /h off` and restored with `/h on`. Deleting an AVD's userdata is just a factory reset that is recreated on the next cold boot (only installed apps, settings, and pairing records are lost), and an AVD definition is recreated in a few clicks in the device manager. Only deleting the system image means the emulator cannot launch again until you re-download it.
- Choose within tier 2 by planned use: the phone AVD that would not be used again was deleted outright (about 3.2 GB), while the watch AVD needed for a demo was kept (its userdata was only 680 MB, so deleting it saves little and only adds the cost of reinstalling apps). Installed apps (games, security, finance, and so on) go into a separate "your call" group, since only the user knows whether they are still used.
- Tier 3 — unrecoverable: an AppData folder named after a game publisher turned out to hold save files, not the app, so its deletion was put on hold and re-confirmed. Folders named after apps or companies can be user data — open them before deleting.
- Leave alone, or touch only with dedicated tools: do not touch `Windows\Installer` (4.3 GB), and shrink WinSxS (26.8 GB) only with `Dism /Online /Cleanup-Image /StartComponentCleanup` (2-5 GB). If folder totals and actual usage disagree by ~15 GB, suspect areas outside your permissions first, such as system restore points (visible only via an admin `vssadmin list shadowstorage /for=C:`).
- Before and after: before deleting, check admin rights, running processes (close the browser before clearing its cache), and dependencies. A warning that "games on another drive may no longer run" came only after a game launcher had already been removed, so ask about dependencies before removal; afterwards, confirm that the uninstall registry entries and leftover AppData folders are gone.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Space Freed by Deleting Comes Back - Relocate Where It Accumulates]], [[Daemon Lifecycle and Data Persistence Are Separate]], [[Verify Backup Creation Immediately After Running a Destructive Script]]
