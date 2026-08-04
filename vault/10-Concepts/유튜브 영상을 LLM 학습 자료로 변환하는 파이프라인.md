---
title: 유튜브 영상을 LLM 학습 자료로 변환하는 파이프라인
tags:
  - llm/pipeline
  - tool/claude-code
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/A-Pipeline-That-Turns-YouTube-Videos-Into-LLM-Readable-Material
created: 2026-08-04
sources:
  - "[[2026-07-17 command-namemodelcommand-name command-messagemodelcommand-me (0ac50409)]]"
---

## 한 줄 요약

영상은 LLM이 직접 볼 수 없지만, yt-dlp 자막(VTT) + ffmpeg 장면 프레임 추출 + 타임스탬프 트랜스크립트를 조합하면 LLM이 순차적으로 "시청"할 수 있는 학습 자료가 된다.

## 내용

- 1단계: `yt-dlp`로 자막(VTT)을 먼저 받는다 — 영상 전체 다운로드보다 자막이 훨씬 싸고, 내용 파악의 뼈대가 된다.
- 2단계: `ffmpeg`로 장면 전환을 감지해 대표 프레임만 추출한다. 균일 간격 캡처보다 프레임 수 대비 정보량이 높다.
- 3단계: VTT를 파싱해 타임스탬프 붙은 트랜스크립트로 만들고, LLM이 프레임 이미지를 순서대로 읽으며 트랜스크립트와 대조한다.
- 실전 함정 1: 자막 요청이 429(rate limit)에 자주 걸린다 — 재시도 로직이 필수.
- 실전 함정 2: 자막이 없는 영상은 Whisper 전사로 폴백한다.
- 관찰된 결과: 강의 영상 3개(12분/14분/33분)가 한 세션 안에서 문서화된 지식으로 변환됐다.

## 출처

- [[2026-07-17 command-namemodelcommand-name command-messagemodelcommand-me (0ac50409)]]
- 관련: [[멀티소스 문서화는 소스별 학습 후 차분 병합으로 한다]]
