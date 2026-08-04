---
title: Windows cp949 인코딩 함정 모음
tags:
  - tool/windows
  - dev/debugging
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Windows-cp949-Encoding-Pitfalls
created: 2026-08-04
sources:
  - "[[2026-07-11 command-namemodelcommand-name command-messagemodelcommand-me (907a6c84)]]"
---

## 한 줄 요약

한국어 Windows(cp949)에서 반복해서 걸리는 인코딩 함정 세 가지 — 공통 패턴은 "한글 텍스트는 argv나 콘솔이 아니라 UTF-8 파일을 통해 흘려보내라"이다.

## 내용

- 함정 1 — curl JSON 페이로드의 한글 깨짐: 커맨드라인 인자로 한글이 든 JSON을 넘기면 cp949 변환 과정에서 깨진다. 해법은 페이로드를 **UTF-8 파일로 저장**하고 `curl --data @file.json`으로 파일 참조로 넘기는 것.
- 함정 2 — pypdf 한글 추출 mojibake: pypdf로 한글 PDF의 텍스트를 추출하면 인코딩이 깨져 나온다. 단, ASCII 문자(전화번호·이메일·URL)는 살아남으므로 그 부분 검색은 여전히 가능하다.
- 함정 3 — 콘솔 출력 UnicodeEncodeError: Python 스크립트가 한글이나 유니코드 기호를 print하면 cp949 콘솔에서 `UnicodeEncodeError`로 죽는다. 출력을 UTF-8 파일로 쓰거나, 출력 인코딩을 명시적으로 UTF-8로 설정해야 한다.
- 공통 패턴: 세 함정 모두 "한글 텍스트가 cp949 경계(argv, 콘솔, 기본 인코딩)를 통과하는 순간" 발생한다. **한글은 UTF-8 파일 경유로 우회**시키는 것이 일관된 해법.
- 파일을 쓸 때도 `encoding="utf-8"`을 명시해야 한다 — Windows Python의 기본 파일 인코딩 역시 cp949다.

## 출처

- [[2026-07-11 command-namemodelcommand-name command-messagemodelcommand-me (907a6c84)]]
- 관련: [[Windows PowerShell 실행 정책이 npm 전역 CLI를 차단한다]]
