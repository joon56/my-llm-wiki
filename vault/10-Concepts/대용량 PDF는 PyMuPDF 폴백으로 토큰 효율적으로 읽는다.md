---
title: 대용량 PDF는 PyMuPDF 폴백으로 토큰 효율적으로 읽는다
tags:
  - llm/pipeline
  - tool/claude-code
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Read-Large-PDFs-Token-Efficiently-With-a-PyMuPDF-Fallback
created: 2026-08-04
sources:
  - "[[2026-07-17 command-namemodelcommand-name command-messagemodelcommand-me (0ac50409)]]"
---

## 한 줄 요약

Read 도구의 PDF 렌더링이 실패하면(poppler 미설치) PyMuPDF(fitz)로 전체 텍스트를 싸게 추출하고, 이미지는 필요한 페이지만 골라 렌더한다 — "텍스트 우선, 이미지는 온디맨드"가 토큰 비용을 실제 필요량에 비례시킨다.

## 내용

- 상황: Read 도구의 PDF 페이지 렌더링이 poppler 미설치로 실패 → PyMuPDF(`fitz`)를 폴백으로 사용.
- 1차 패스: `fitz`로 76쪽 전체의 텍스트를 추출 — 텍스트는 이미지 대비 토큰 비용이 훨씬 싸다.
- 2차 패스: 텍스트만으로 부족한 페이지(표·스크린샷·레이아웃 의존 내용)만 이미지로 렌더해서 확인.
- 실측: 76쪽 중 28쪽만 이미지로 열람 — 나머지 48쪽은 텍스트 추출로 충분했다.
- 원칙: 전 페이지를 이미지로 읽으면 토큰 비용이 문서 크기에 비례하지만, 텍스트 우선 + 이미지 온디맨드면 비용이 "실제로 봐야 하는 양"에 비례한다.
- 단, 텍스트 추출 결과는 구조(표 등)가 깨질 수 있으므로 수치 인용 전 검증이 필요하다.

## 출처

- [[2026-07-17 command-namemodelcommand-name command-messagemodelcommand-me (0ac50409)]]
- 관련: [[PDF 표 추출값은 본문 대조 없이 신뢰하지 않는다]]
