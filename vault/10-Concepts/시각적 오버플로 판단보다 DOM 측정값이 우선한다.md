---
title: 시각적 오버플로 판단보다 DOM 측정값이 우선한다
tags:
  - dev/frontend
  - dev/debugging
status: distilled
publish: false
created: 2026-07-26
sources:
  - "[[2026-07-16 command-nameclearcommand-name command-messageclearcommand-me (224d8bea)]]"
---

## 한 줄 요약

스크린샷에서 레이아웃이 잘려 보인다고 CSS 오버플로 버그로 단정하면 안 된다 — 헤드리스 브라우저는 창 너비에 강제 하한이 있어 좁은 뷰포트 스크린샷 자체가 왜곡될 수 있으므로, 판정은 `scrollWidth === clientWidth` 같은 DOM 측정값으로 한다.

## 내용

- 헤드리스 Chrome은 요청한 뷰포트보다 창 너비를 좁게 못 만드는 하한(약 500px 수준)이 있는 환경이 있다. 375px 모바일 스크린샷을 요청해도 실제 렌더는 더 넓은 창에서 일어나 화면이 잘리거나 어긋나 보임.
- 이 왜곡을 보고 "모바일에서 가로 스크롤 생기는 버그"로 오진하면, 존재하지 않는 버그를 고치느라 CSS를 망가뜨리게 됨.
- 올바른 판정: 브라우저 콘솔/스크립트에서 `document.documentElement.scrollWidth === document.documentElement.clientWidth` 확인. 같으면 가로 오버플로 없음 — 스크린샷이 이상해도 렌더 환경 문제.
- 일반화: 시각 결과물(스크린샷)은 렌더 환경의 제약이 섞인 간접 증거다. 레이아웃 판정의 1차 증거는 DOM이 직접 보고하는 측정값.

## 출처

- [[2026-07-16 command-nameclearcommand-name command-messageclearcommand-me (224d8bea)]]
- 관련: [[접근성 대비는 계산으로 검증하지 눈으로 판단하지 않는다]]
