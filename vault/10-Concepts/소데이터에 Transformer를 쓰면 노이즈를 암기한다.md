---
title: 소데이터에 Transformer를 쓰면 노이즈를 암기한다
tags:
  - ml/overfitting
  - ml/data
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Transformers-on-Small-Data-Memorize-Noise
created: 2026-08-04
sources:
  - "[[2026-07-09 command-nameclearcommand-name command-messageclearcommand-me (53e8d9be)]]"
---

## 한 줄 요약

2.5K 샘플 규모에서 Transformer의 attention 용량은 일반화가 아니라 암기에 쓰인다 — 진단된 실패는 아키텍처가 아니라 입력 구성의 문제였고, 고칠 곳도 입력이다.

## 내용

- 맥락: NHIS 입원 예측(환자 2,532명)에 Transformer 계열 모델을 쓰면서 두 가지 실패 모드가 진단됐다.
- 실패 1 — 가짜 시퀀스: 순서가 없는 진단코드 bag을 시퀀스로 넣고 positional embedding까지 얹으면, 모델은 존재하지 않는 "순서"라는 노이즈를 암기한다. 코드 나열 순서는 의미가 없는데 위치 정보가 학습 대상이 되는 것.
- 실패 2 — 전처리 누수: vocab과 StandardScaler를 train/val 분리 전에 전체 데이터로 fit하면 검증 세트 정보가 학습에 새어 들어간다. fit은 train에만, transform은 양쪽에.
- 공통 원리: 샘플 2.5K 수준에서는 attention의 표현 용량이 신호 학습이 아니라 노이즈 암기로 흘러간다. 데이터가 작을수록 모델이 암기할 "가짜 패턴"의 비중이 커진다.
- 처방: 아키텍처를 바꾸는 게 아니라 입력을 고친다 — 순서 없는 데이터는 순서 없는 표현(집계·bag)으로, 전처리는 누수 없는 파이프라인으로.
- 일반화: "모델이 이상하다"의 상당수는 모델 문제가 아니라 입력 표현이 데이터의 실제 구조와 어긋난 문제다.

## 출처

- [[2026-07-09 command-nameclearcommand-name command-messageclearcommand-me (53e8d9be)]]
- 관련: [[train-val 지표 갭이 과적합의 신호다]]
