---
title: 오프라인 HTML 사본에는 메타태그가 빠져 있을 수 있다
tags:
  - dev/frontend
  - tool/claude-code
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Offline-HTML-Copies-May-Lack-Required-Meta-Tags
created: 2026-08-04
sources:
  - "[[2026-07-17 command-namemodelcommand-name command-messagemodelcommand-me (0ac50409)]]"
---

## 한 줄 요약

Artifact 발행 파이프라인은 `<meta charset>`·viewport를 자동 주입하지만, 같은 HTML을 독립 파일로 빼내는 순간 둘 다 사라진다 — HTML이 원래 파이프라인을 벗어날 때는 charset/viewport부터 확인하라.

## 내용

- Artifact 발행 시 파이프라인이 `<meta charset="utf-8">`과 `<meta name="viewport">`를 자동으로 주입해 준다 — 작성자가 안 써도 결과 페이지는 정상.
- 같은 HTML을 오프라인 사본(독립 파일)으로 복사하면 이 자동 주입이 없다 → 두 태그가 모두 빠진 채 배포된다.
- 증상 1: charset 누락 → 한글이 모지바케(깨진 문자)로 렌더링.
- 증상 2: viewport 누락 → 모바일에서 축소된 데스크톱 레이아웃으로 렌더링.
- 교훈: "같은 HTML"이라도 배포 경로가 다르면 필요한 보일러플레이트가 다르다. 파이프라인이 무엇을 대신 채워주는지는 파이프라인을 벗어나는 순간 드러난다.
- 체크리스트: HTML을 원래 발행 경로 밖으로 옮길 때마다 `<meta charset="utf-8">`, `<meta name="viewport" content="width=device-width, initial-scale=1">` 존재 여부를 확인.

## 출처

- [[2026-07-17 command-namemodelcommand-name command-messagemodelcommand-me (0ac50409)]]
- 관련: [[base64 내장 단일 HTML은 배포 없는 배포다]]
