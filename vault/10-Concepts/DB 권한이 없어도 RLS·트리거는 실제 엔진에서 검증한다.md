---
title: DB 권한이 없어도 RLS·트리거는 실제 엔진에서 검증한다
tags:
  - dev/db
  - dev/security
  - dev/testing
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Verify-RLS-and-Triggers-on-a-Real-Engine-Even-Without-DB-Access
created: 2026-11-21
sources:
  - "[[2026-11-02 해당 폴거 정보 읽고 우리가 이번에 상시 커피챗을 개설하려는데 공식 웹에서 이를 받으려고 해. 루트 폴더에 (8597bfd5)]]"
---

## 한 줄 요약

마이그레이션은 사람이 Supabase SQL Editor에서 손으로 돌리고 에이전트에겐 DB 권한도 테스트 프레임워크도 없었지만, 검증을 **내장 Postgres → 가짜 백엔드 위 실제 앱 → 배포 후 공개 키 탐침 → 사람용 자가점검 SQL**의 4층으로 나눠 운영 첫 실행 전에 대부분을 확인했다.

## 내용

- 원칙: DB 권한이 없다고 검증을 사람의 운영 시험으로 미루면 운영이 첫 테스트가 된다. 층마다 잡는 실패가 다르다 — SQL 의미·트리거 순서(엔진), 화면 배선과 권한 오류 처리(가짜 백엔드), 실제 적용된 정책(탐침), 에이전트가 볼 수 없는 설정(자가점검).
- 1층 DB 로직: PGlite(WASM으로 도는 실제 Postgres)에 auth 스키마·프로필 표·Vault·pg_net·Supabase 기본 권한을 스텁으로 깔고 마이그레이션을 그대로 실행한다. 실패하는 시나리오 테스트를 먼저 쓰고 SQL을 작성해 RLS·트리거·제약 시나리오 46개를 통과시켰다.
- 2층 화면: 실제 앱을 저장소 밖에서 Vite `createServer`(`configFile:false`, `envFile:false`)로 띄우고 `resolveId` 훅으로 Supabase 클라이언트 모듈을 가짜로 바꿔치기한다 — 구조적으로 실 DB에 닿을 수 없다. 가짜는 같은 RLS·컬럼 권한·트리거·제약·없는 컬럼 오류까지 흉내 내고, 관리자 화면 검사 63개는 DB 쓰기 요청 0건으로 고정했다.
- 3층 배포 후 외부 탐침: 운영 DB를 공개(anon) 키로 조회해 비공개 표 읽기와 모든 표 쓰기가 막혔는지 확인한다. 쓰기 시험은 존재하지 않는 id와 빈 배열만 써서 바뀐 행이 0임을 보장하고, Vault·pg_net·트리거 함수가 API로 호출되지 않는지도 본다.
- 4층 자가점검 SQL: 사람이 SQL Editor에서 돌릴 `item / actual / expected / ok` 형태의 CTE를 준다. RLS 켜진 표 수, 정책 수, 켜진 트리거, security definer 함수, `has_table_privilege('anon', …)` 결과를 기대값과 대조하되 비밀값·개인정보는 출력하지 않는다. 이 SQL도 먼저 1층 엔진에서 25개 항목으로 검증했다.
- 경계를 보고에 적는다: 인증·Vault·메일 발송은 흉내 낸 환경이었다는 점과 "로그인 상태의 운영 쓰기·실제 신청 저장은 미확인"을 분리해 적고, 그 부분은 사람이 운영 첫 시험으로 확인하도록 넘긴다.

## 출처

- [[2026-11-02 해당 폴거 정보 읽고 우리가 이번에 상시 커피챗을 개설하려는데 공식 웹에서 이를 받으려고 해. 루트 폴더에 (8597bfd5)]]
- 관련: [[RLS에 기댄 무필터 쿼리는 관리자 계정에서 샌다]], [[SQL 스크립트는 트랜잭션으로 감싸야 첫 에러가 드러난다]]
