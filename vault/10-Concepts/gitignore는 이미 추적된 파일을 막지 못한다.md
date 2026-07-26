---
title: gitignore는 이미 추적된 파일을 막지 못한다
tags:
  - tool/git
status: distilled
publish: false
created: 2026-07-26
sources:
  - "[[2026-07-15 ide_opened_fileThe user opened the file chealthcareCLAUDE.md (e0e1d313)]]"
---

## 한 줄 요약

`.gitignore`는 "아직 추적되지 않은" 파일에만 적용된다 — 이미 커밋된 파일은 gitignore에 추가해도 계속 추적·push되므로, `git rm -r --cached`로 별도 추적 해제가 필요하다.

## 내용

- gitignore의 실제 의미: "untracked 파일을 스테이징 후보에서 제외". 이미 인덱스에 있는 파일은 대상이 아님.
- 캐시 파일을 커밋한 뒤 gitignore에 추가 → 여전히 변경사항이 계속 push됨. 흔한 오진: "gitignore가 안 먹네".
- 해제: `git rm -r --cached <경로>` (로컬 파일은 유지, 추적만 해제) 후 커밋. 이후부터 gitignore 적용.
- **주의: 커밋 이력에는 남는다.** 비밀정보·PII가 들어갔다면 추적 해제로 부족 — 이력 재작성(filter-repo) + 키 폐기 필요.
- 예방 습관: 저장소에 gitignore를 처음 설정할 때 `git ls-files`로 이미 추적 중인 파일부터 감사하라. 특히 public repo면 캐시·개인정보·실명 파일이 이력에 있는지 push 전에 확인.

## 출처

- [[2026-07-15 ide_opened_fileThe user opened the file chealthcareCLAUDE.md (e0e1d313)]]
