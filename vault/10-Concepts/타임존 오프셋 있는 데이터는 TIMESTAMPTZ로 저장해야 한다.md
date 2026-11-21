---
title: 타임존 오프셋 있는 데이터는 TIMESTAMPTZ로 저장해야 한다
tags:
  - dev/db
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Store-Timezone-Offset-Data-as-TIMESTAMPTZ
created: 2026-07-26
sources:
  - "[[2026-07-16 ide_opened_fileThe user opened the file chealthcaredocsDATA_ (261ec49a)]]"
  - "[[2026-11-08 ide_opened_fileThe user opened the file cUsersUSERDesktopwal (3a852e2e)]]"
  - "[[2026-11-20 내일(1121) 실험 2·3 현장 데이터 점검을 이 세션에서 한다. .handoffHANDOFF_1121.m (1b699272)]]"
---

## 한 줄 요약

외부 페이로드가 타임존 오프셋을 포함하는데 `TIMESTAMP`(WITHOUT TIME ZONE) 컬럼에 저장하면 오프셋이 조용히 버려진다 — 서로 다른 시각이 같은 값으로 저장되는, 사후 복구 불가능한 데이터 손실.

## 내용

- PostgreSQL `TIMESTAMP`는 `2026-07-16T09:00:00+09:00`을 받으면 `+09:00`을 그냥 버리고 `09:00:00`으로 저장. 에러도 경고도 없음.
- `2026-07-16T09:00:00+09:00`(KST)과 `2026-07-16T09:00:00Z`(UTC)는 9시간 차이 나는 다른 시각인데 같은 값이 됨 — 저장된 후에는 어느 쪽이었는지 알 방법이 없다.
- `TIMESTAMPTZ`는 입력의 오프셋을 해석해 UTC로 정규화 저장, 조회 시 세션 타임존으로 변환. 원본 시각 정보가 보존됨.
- 원칙: 시간 데이터의 손실은 **저장 시점에만** 막을 수 있다. "나중에 마이그레이션하지" 불가 — 이미 뭉개진 값은 복구 못 함. 외부 API/로그 수집 스키마 설계 시 기본값을 TIMESTAMPTZ로.
- DB 밖에도 같은 함정이 있다: 센서 기록 앱(Sensor Logger)의 zip 파일명 시각은 UTC 기준이라 한국 시각보다 9시간 이르다(파일명 11:08:58 = 현지 20:08:58). 파일명으로 날짜 폴더·이름 규칙을 정하거나 시행을 짝지으면 날짜와 순서가 어긋나므로, 짝짓기는 파일 안 메타데이터의 현지 시작 시각으로 하고 이름에 쓰는 날짜는 현지 기준으로 쓴다.

## 출처

- [[2026-07-16 ide_opened_fileThe user opened the file chealthcaredocsDATA_ (261ec49a)]]
- [[2026-11-08 ide_opened_fileThe user opened the file cUsersUSERDesktopwal (3a852e2e)]]
- [[2026-11-20 내일(1121) 실험 2·3 현장 데이터 점검을 이 세션에서 한다. .handoffHANDOFF_1121.m (1b699272)]]
- 관련: [[SQL 스크립트는 트랜잭션으로 감싸야 첫 에러가 드러난다]]
