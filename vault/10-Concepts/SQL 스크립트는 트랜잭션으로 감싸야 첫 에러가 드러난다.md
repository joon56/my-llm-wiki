---
title: SQL 스크립트는 트랜잭션으로 감싸야 첫 에러가 드러난다
tags:
  - dev/db
  - dev/debugging
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Wrap-SQL-Scripts-in-a-Transaction-to-Surface-the-First-Error
created: 2026-07-26
sources:
  - "[[2026-07-16 ide_opened_fileThe user opened the file chealthcaredocsDATA_ (261ec49a)]]"
---

## 한 줄 요약

멀티스테이트먼트 SQL 스크립트에서 보이는 에러 메시지는 "마지막으로 실패한 문장"일 뿐이다 — 클라이언트가 앞선 실패 후에도 계속 실행해 캐스케이드 에러가 되므로, BEGIN/COMMIT으로 감싸야 진짜 원인 문장에서 멈춘다.

## 내용

- psql 등 다수 SQL 클라이언트는 기본적으로 문장 단위 실행: 3번째 문장이 실패해도 4, 5번째를 계속 실행한다. 4, 5번째는 3번째가 만들었어야 할 테이블/컬럼이 없어서 연쇄 실패 → 화면에 남는 건 마지막 에러.
- 마지막 에러를 원인으로 오진하면 엉뚱한 문장을 고치게 됨.
- `BEGIN; ... COMMIT;`으로 감싸면 첫 실패 지점에서 트랜잭션이 abort 상태가 되고 이후 문장은 전부 "current transaction is aborted"로 스킵 — 첫 에러 메시지가 곧 원인.
- 보너스: 부분 적용된 스키마(절반만 만들어진 상태)도 방지됨. 스키마 마이그레이션 스크립트는 기본적으로 트랜잭션으로.

## 출처

- [[2026-07-16 ide_opened_fileThe user opened the file chealthcaredocsDATA_ (261ec49a)]]
