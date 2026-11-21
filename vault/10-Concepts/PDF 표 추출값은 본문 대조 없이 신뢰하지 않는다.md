---
title: PDF 표 추출값은 본문 대조 없이 신뢰하지 않는다
tags:
  - dev/data
  - research/writing
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Never-Trust-PDF-Table-Extraction-Without-Cross-Checking-the-Prose
created: 2026-07-26
sources:
  - "[[2026-07-25 I need an English write-up of a research paper of mine, for (fce4a47b)]]"
  - "[[2026-11-12 정보보안 과제 2(AES)를 시작해. 1) 루트의 CLAUDE.md, 과제_진행_플레이북.md, 과제_공통_ (669db9d1)]]"
---

## 한 줄 요약

pdftotext 같은 PDF 텍스트 추출 도구는 표(table)의 열을 뒤섞는다 — 표에서 뽑은 숫자는 반드시 본문 서술(prose)과 대조해서 확인한 뒤에만 인용한다.

## 내용

- PDF의 표는 시각적 배치일 뿐 내부적으로 행·열 구조가 없다. 텍스트 추출 시 읽기 순서가 뒤엉켜 옆 열의 숫자가 붙어 나오는 일이 흔함.
- 위험한 이유: 추출 결과가 "그럴듯한 숫자 나열"이라 뒤섞였는지 눈으로 티가 안 남. 그대로 인용하면 다른 변수의 값을 보고하게 됨.
- 검증 방법: 논문·보고서 본문에는 핵심 수치가 문장으로 다시 언급되는 경우가 많다("계수는 0.42로 유의했다") — 표 추출값을 이 서술과 대조. 서술이 없으면 PDF를 직접 열어 눈으로 확인.
- 일반화: 구조 정보를 잃는 변환(표→텍스트, 레이아웃→플레인텍스트)을 거친 데이터는 독립된 경로로 교차 확인하기 전까지 잠정값으로 취급한다.
- 표가 이미지면 텍스트 추출이 아예 안 된다: 쪽을 고해상도로 렌더해 판독하고, 별도 에이전트에게 기대값 없이 같은 표를 다시 옮겨 적게 해 두 판독을 기계로 대조한다(이중 입력). S-박스 2개(512칸)가 일치했고, 표준과 다른 칸은 1개로 확정됐다.
- 판독값은 내부 일관성(역표와 서로 역관계인지, 순열인지)과 외부 기준(표준 테스트 벡터)으로 한 번 더 검증한다 — [[교재·명세의 표는 구조 불변식과 참조 모델로 검증한다]].

## 출처

- [[2026-07-25 I need an English write-up of a research paper of mine, for (fce4a47b)]]
- [[2026-11-12 정보보안 과제 2(AES)를 시작해. 1) 루트의 CLAUDE.md, 과제_진행_플레이북.md, 과제_공통_ (669db9d1)]]
