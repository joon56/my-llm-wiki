---
title: base64 내장 단일 HTML은 배포 없는 배포다
tags:
  - dev/frontend
  - dev/docs
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/A-Single-HTML-File-With-Base64-Assets-Is-Deployment-Without-a-Server
created: 2026-08-04
sources:
  - "[[2026-07-17 command-namemodelcommand-name command-messagemodelcommand-me (0ac50409)]]"
---

## 한 줄 요약

이미지·CSS·JS를 전부 파일 안에 내장한 단일 HTML은 서버·호스팅 없이 메신저로 그냥 보내면 되는 "배포 없는 배포" 수단이다.

## 내용

- 스크린샷 15장을 PIL로 리사이즈·최적화한 뒤 base64 data URI로 HTML에 직접 내장했다.
- CSS/JS도 전부 인라인 — 외부 요청이 0인 완전 자기완결(self-contained) 파일이 된다.
- 결과물: 712KB짜리 HTML 파일 하나. 서버도 호스팅도 없이 메신저 첨부만으로 공유 완료.
- 부수 효과: 외부 요청이 없는 구조는 Artifact의 CSP 제약(외부 호스트 요청 차단)과도 그대로 호환된다 — 같은 파일이 두 배포 경로에서 동작.
- 트레이드오프: base64 인코딩은 에셋당 파일 크기를 약 33% 키운다 — 내장 전에 이미지를 반드시 리사이즈·압축(최적화)할 것.
- 적용 기준: 수백 KB~수 MB급 문서형 결과물에 적합. 대용량 미디어가 많으면 파일이 급격히 커져 부적합.

## 출처

- [[2026-07-17 command-namemodelcommand-name command-messagemodelcommand-me (0ac50409)]]
- 관련: [[오프라인 HTML 사본에는 메타태그가 빠져 있을 수 있다]]
