---
title: 시각적 오버플로 판단보다 DOM 측정값이 우선한다
tags:
  - dev/frontend
  - dev/debugging
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/DOM-Measurements-Outrank-Visual-Overflow-Judgments
created: 2026-07-26
sources:
  - "[[2026-07-16 command-nameclearcommand-name command-messageclearcommand-me (224d8bea)]]"
  - "[[2026-11-02 해당 폴거 정보 읽고 우리가 이번에 상시 커피챗을 개설하려는데 공식 웹에서 이를 받으려고 해. 루트 폴더에 (8597bfd5)]]"
  - "[[2026-11-06 ide_opened_fileThe user opened the file cUsersUSERDesktop모프 (bff996c4)]]"
---

## 한 줄 요약

스크린샷에서 레이아웃이 잘려 보인다고 CSS 오버플로 버그로 단정하면 안 된다 — 헤드리스 브라우저는 창 너비에 강제 하한이 있어 좁은 뷰포트 스크린샷 자체가 왜곡될 수 있으므로, 판정은 `scrollWidth === clientWidth` 같은 DOM 측정값으로 한다.

## 내용

- 헤드리스 Chrome은 요청한 뷰포트보다 창 너비를 좁게 못 만드는 하한(약 500px 수준)이 있는 환경이 있다. 375px 모바일 스크린샷을 요청해도 실제 렌더는 더 넓은 창에서 일어나 화면이 잘리거나 어긋나 보임.
- 이 왜곡을 보고 "모바일에서 가로 스크롤 생기는 버그"로 오진하면, 존재하지 않는 버그를 고치느라 CSS를 망가뜨리게 됨.
- 올바른 판정: 브라우저 콘솔/스크립트에서 `document.documentElement.scrollWidth === document.documentElement.clientWidth` 확인. 같으면 가로 오버플로 없음 — 스크린샷이 이상해도 렌더 환경 문제.
- 일반화: 시각 결과물(스크린샷)은 렌더 환경의 제약이 섞인 간접 증거다. 레이아웃 판정의 1차 증거는 DOM이 직접 보고하는 측정값.
- 시각 버그도 실패하는 측정 검사부터 만든다: 수정 전 DOM 기준선 검사로 겹침 3장·가림 10장을 실패로 잡고, 수정 후 0장이 된 것을 배포 뒤 운영 URL에서 다시 확인했다. UX 진단도 수치로 했다(하위 페이지 히어로 360px 때문에 본문이 524px에서 시작, 9~11px 글자 지정 39곳). 단, 이미지 압축 화질처럼 수치가 품질을 대변하지 못하는 항목은 화면으로 따로 본다.
- Android에서도 같다: 색 선택 링이 스크린샷에 안 보였지만 `uiautomator dump`로는 checked=true였다. 상태는 정상이니 렌더링 문제(배경 틴트가 링까지 칠함)로 범위가 좁혀졌고, 링을 foreground로 옮겨 해결했다.
- 자동화가 만든 가짜 버그도 있다: 스크린샷 3장이 전부 상세 화면이라 '뒤로 가기 버그'를 의심했지만, 실제로는 터치 모드 복귀용 좌표 탭이 스크롤된 홈의 카드를 다시 연 것이었다(이후 좌표 대신 resource id로 탭). 검은 화면도 크래시가 아니라 화면 전환 중의 프레임이었다.

## 출처

- [[2026-07-16 command-nameclearcommand-name command-messageclearcommand-me (224d8bea)]]
- [[2026-11-02 해당 폴거 정보 읽고 우리가 이번에 상시 커피챗을 개설하려는데 공식 웹에서 이를 받으려고 해. 루트 폴더에 (8597bfd5)]]
- [[2026-11-06 ide_opened_fileThe user opened the file cUsersUSERDesktop모프 (bff996c4)]]
- 관련: [[접근성 대비는 계산으로 검증하지 눈으로 판단하지 않는다]]
