---
title: train-val 지표 갭이 과적합의 신호다
tags:
  - ml/overfitting
  - ml/evaluation
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/The-Train-Validation-Metric-Gap-Signals-Overfitting
created: 2026-08-04
sources:
  - "[[2026-07-09 분석은 목요일 강의한 딥러닝 코드를 이용해서, 일부 하이퍼파라메터 및 데이터 입력 부분만 고치고, 세부적인 (acd3615e)]]"
  - "[[2026-07-09 command-nameclearcommand-name command-messageclearcommand-me (53e8d9be)]]"
---

## 한 줄 요약

train AUC와 val AUC의 갭이 과적합 진단의 1차 지표다 — baseline은 train 0.83 vs val 0.57(갭 0.257)로 사실상 암기 상태였고, val이 랜덤 수준이면 고칠 것은 모델이 아니라 피처와 데이터다.

## 내용

- 맥락: NHIS 입원 예측 과제(환자 2,532명, 모델 구조 고정). baseline이 train AUC 0.83, val AUC 0.57 — 갭 0.257.
- val AUC 0.57은 랜덤(0.5)에 가깝다: 모델이 학습 데이터를 암기했을 뿐 일반화 신호를 거의 못 배운 상태.
- 이 조합(높은 train + 랜덤 수준 val)의 처방은 모델 튜닝이 아니라 입력 개선이다 — 실제로 아키텍처는 고정한 채 피처를 보강해서 문제를 풀었다.
- 피처 보강 후 갭은 0.064로 줄었고, 최종 val AUC는 0.57에서 0.70까지 올라갔다.
- 개선 과정에서 train 점수가 내려가는 것은 퇴보가 아니라 암기가 줄었다는 뜻 — val이 오르면서 train이 내려가면 올바른 방향이다.
- 실무 습관: 실험마다 val 점수 하나만 보지 말고 (train, val, 갭) 세 숫자를 함께 기록해야 개선의 성격(일반화 향상 vs 암기 강화)을 구분할 수 있다.

## 출처

- [[2026-07-09 분석은 목요일 강의한 딥러닝 코드를 이용해서, 일부 하이퍼파라메터 및 데이터 입력 부분만 고치고, 세부적인 (acd3615e)]]
- [[2026-07-09 command-nameclearcommand-name command-messageclearcommand-me (53e8d9be)]]
- 관련: [[피처는 다 넣으면 진다 — 그룹 ablation과 상보성]]
