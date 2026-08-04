---
title: gh CLI 없이 PAT만으로 repo를 만들고 push한다
tags:
  - tool/git
  - dev/security
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Create-and-Push-a-GitHub-Repo-With-Only-a-PAT
created: 2026-08-04
sources:
  - "[[2026-07-11 command-namemodelcommand-name command-messagemodelcommand-me (907a6c84)]]"
---

## 한 줄 요약

gh CLI가 없어도 PAT 하나로 repo 생성부터 push까지 가능하다 — 단, 진행 전에 `X-OAuth-Scopes` 응답 헤더로 토큰 권한을 확인해야 하고, push 후에는 remote URL에서 토큰을 즉시 제거해야 한다.

## 내용

- 1단계 — 토큰 검증: `curl -H "Authorization: token ghp_xxxx" https://api.github.com/user`로 토큰이 살아있는지, 어느 계정인지 확인한다.
- 2단계 — 스코프 확인(비자명한 핵심): 같은 응답의 **`X-OAuth-Scopes` 헤더**를 본다. 이 헤더가 비어 있으면 토큰에 아무 권한이 없는 것이고, 이때 repo 생성 API는 권한 오류가 아니라 **오해를 부르는 "Not Found"(404)**를 돌려준다. 404를 보고 URL을 의심하기 전에 스코프부터 확인하라.
- 3단계 — repo 생성: `POST https://api.github.com/user/repos`에 `{"name": "...", "private": true}` 같은 JSON을 보내면 repo가 만들어진다 (`repo` 스코프 필요).
- 4단계 — push: remote를 토큰 내장 URL로 설정한다. `git remote add origin https://ghp_xxxx@github.com/USER/REPO.git` 후 `git push -u origin main`.
- 5단계 — 즉시 정리: push가 성공하면 **바로** `git remote set-url origin https://github.com/USER/REPO.git`으로 토큰을 `.git/config`에서 제거한다. 안 하면 토큰이 설정 파일에 평문으로 남는다.
- 토큰 자체도 짧은 만료로 발급하고 작업 후 revoke한다 — 채팅·로그 어딘가에 남았을 가능성을 전제로 움직인다.

## 출처

- [[2026-07-11 command-namemodelcommand-name command-messagemodelcommand-me (907a6c84)]]
- 관련: [[채팅에 붙여넣은 시크릿은 세션 로그에 영구 보존된다]]
