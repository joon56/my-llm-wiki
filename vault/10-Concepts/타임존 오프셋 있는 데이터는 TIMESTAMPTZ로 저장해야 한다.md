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
---

## 한 줄 요약

외부 페이로드가 타임존 오프셋을 포함하는데 `TIMESTAMP`(WITHOUT TIME ZONE) 컬럼에 저장하면 오프셋이 조용히 버려진다 — 서로 다른 시각이 같은 값으로 저장되는, 사후 복구 불가능한 데이터 손실.

## 내용

- PostgreSQL `TIMESTAMP`는 `2026-07-16T09:00:00+09:00`을 받으면 `+09:00`을 그냥 버리고 `09:00:00`으로 저장. 에러도 경고도 없음.
- `2026-07-16T09:00:00+09:00`(KST)과 `2026-07-16T09:00:00Z`(UTC)는 9시간 차이 나는 다른 시각인데 같은 값이 됨 — 저장된 후에는 어느 쪽이었는지 알 방법이 없다.
- `TIMESTAMPTZ`는 입력의 오프셋을 해석해 UTC로 정규화 저장, 조회 시 세션 타임존으로 변환. 원본 시각 정보가 보존됨.
- 원칙: 시간 데이터의 손실은 **저장 시점에만** 막을 수 있다. "나중에 마이그레이션하지" 불가 — 이미 뭉개진 값은 복구 못 함. 외부 API/로그 수집 스키마 설계 시 기본값을 TIMESTAMPTZ로.

## 출처

- [[2026-07-16 ide_opened_fileThe user opened the file chealthcaredocsDATA_ (261ec49a)]]
- 관련: [[SQL 스크립트는 트랜잭션으로 감싸야 첫 에러가 드러난다]]
