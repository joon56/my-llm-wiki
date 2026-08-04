---
title: PDF 개인정보는 오버레이가 아니라 redaction으로 지운다
tags:
  - dev/security
  - dev/data
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Remove-PDF-PII-With-True-Redaction-Not-Overlays
created: 2026-08-04
sources:
  - "[[2026-07-11 command-namemodelcommand-name command-messagemodelcommand-me (907a6c84)]]"
---

## 한 줄 요약

PDF에서 전화번호·이메일을 지울 때 검은 박스를 덮는 것(오버레이)은 텍스트가 그대로 추출되는 가짜 삭제다 — pymupdf의 redaction annotation을 추가하고 apply해야 콘텐츠가 실제로 삭제된다.

## 내용

- 오버레이의 함정: 텍스트 위에 사각형을 그려 가리면 화면에서는 안 보이지만, 텍스트 레이어는 그대로라서 복사·추출·검색으로 전부 복원된다. 시각적 가림 ≠ 삭제.
- 진짜 삭제: pymupdf(fitz)로 대상 영역에 **redaction annotation**을 추가한 뒤 `apply_redactions()`를 호출하면 해당 영역의 콘텐츠 자체가 PDF에서 제거된다.
- 한글 PDF에서의 핵심 통찰: 텍스트 추출이 한글 인코딩 문제로 깨져(mojibake) 나와도, **전화번호와 이메일은 ASCII**라서 검색으로 위치(좌표)를 정확히 찾을 수 있다. 한글이 깨진다고 redaction이 불가능한 게 아니다.
- 검증 필수: redaction 적용 후 텍스트를 **다시 추출해서** 전화번호·이메일 패턴이 안 나오는지 확인한다. "박스가 보이니 지워졌겠지"는 검증이 아니다.
- 원본 보존: redaction은 비가역이므로, 원본 PDF는 repo 바깥에 백업으로 보관한다. repo에는 redaction된 버전만 들어간다.

## 출처

- [[2026-07-11 command-namemodelcommand-name command-messagemodelcommand-me (907a6c84)]]
- 관련: [[공개 전환 전 개인정보·라이선스 스위프 체크리스트]]
