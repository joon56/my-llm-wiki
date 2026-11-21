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
  - "[[2026-10-02 최근 문서들을 확인해보면 알겠지만, 몇주 전부터 코어 인원도 운영진 회의 시간에 올 수 있게 되었어. 원래도 (b0e5f24a)]]"
  - "[[2026-11-06 ide_opened_fileThe user opened the file cUsersUSERDesktop모프 (bff996c4)]]"
  - "[[2026-11-12 정보보안 과제 2(AES)를 시작해. 1) 루트의 CLAUDE.md, 과제_진행_플레이북.md, 과제_공통_ (669db9d1)]]"
---

## 한 줄 요약

한국어 Windows(cp949)에서 반복해서 걸리는 인코딩 함정 여섯 가지 — 공통 패턴은 "한글 텍스트는 argv나 콘솔이 아니라 UTF-8 파일을 통해 흘려보내라"이다.

## 내용

- 함정 1 — curl JSON 페이로드의 한글 깨짐: 커맨드라인 인자로 한글이 든 JSON을 넘기면 cp949 변환 과정에서 깨진다. 해법은 페이로드를 **UTF-8 파일로 저장**하고 `curl --data @file.json`으로 파일 참조로 넘기는 것.
- 함정 2 — pypdf 한글 추출 mojibake: pypdf로 한글 PDF의 텍스트를 추출하면 인코딩이 깨져 나온다. 단, ASCII 문자(전화번호·이메일·URL)는 살아남으므로 그 부분 검색은 여전히 가능하다.
- 함정 3 — 콘솔 출력 UnicodeEncodeError: Python 스크립트가 한글이나 유니코드 기호를 print하면 cp949 콘솔에서 `UnicodeEncodeError`로 죽는다. 출력을 UTF-8 파일로 쓰거나, 출력 인코딩을 명시적으로 UTF-8로 설정해야 한다.
- 공통 패턴: 어느 함정이든 "한글 텍스트가 cp949 경계(argv, 콘솔, 기본 인코딩)를 통과하는 순간" 발생한다. **한글은 UTF-8 파일 경유로 우회**시키는 것이 일관된 해법.
- 파일을 쓸 때도 `encoding="utf-8"`을 명시해야 한다 — Windows Python의 기본 파일 인코딩 역시 cp949다.
- 함정 4 — PowerShell 5.1 스크립트: BOM 없는 UTF-8 `.ps1`을 ANSI(CP949)로 읽어 스크립트 안의 한글 문자열·경로가 깨진다. 깨진 한글 주석이 다음 줄(`Add-Type`)까지 삼켜 엉뚱한 오류가 나기도 했다. PS 5.1이 실행할 스크립트는 UTF-8 BOM으로 저장하고, 다른 도구가 읽을 소스·XML은 `UTF8Encoding($false)`(BOM 없음)로 쓴다 — BOM 여부는 '누가 읽나'로 정한다.
- 함정 5 — MSVC: `/utf-8` 없이 BOM 없는 UTF-8 소스를 시스템 코드 페이지(CP949)로 읽어 C4819 경고가 나고, `#include`의 한글 파일명이 깨져 C1083(파일 없음)이 난다. 소스를 UTF-8 BOM으로 저장하거나, 동작에 쓰는 한글 문자열은 `\uXXXX`로 쓴다(재저장 인코딩별 검증은 [[붙여넣기 이식성은 빈 프로젝트와 인코딩 매트릭스로 검증한다]]).
- 함정 6 — IDE 기본 인코딩: 한국어 Windows의 이클립스는 기본 텍스트 인코딩이 MS949일 수 있어(버전에 따라 다름) UTF-8로 쓴 한글 주석이 깨진다. 배포용 프로젝트에는 프로젝트 단위 UTF-8 설정을 미리 넣고, 안내문에 복구 경로(Properties → Resource → Text file encoding → UTF-8)를 적어 둔다.

## 출처

- [[2026-07-11 command-namemodelcommand-name command-messagemodelcommand-me (907a6c84)]]
- [[2026-10-02 최근 문서들을 확인해보면 알겠지만, 몇주 전부터 코어 인원도 운영진 회의 시간에 올 수 있게 되었어. 원래도 (b0e5f24a)]]
- [[2026-11-06 ide_opened_fileThe user opened the file cUsersUSERDesktop모프 (bff996c4)]]
- [[2026-11-12 정보보안 과제 2(AES)를 시작해. 1) 루트의 CLAUDE.md, 과제_진행_플레이북.md, 과제_공통_ (669db9d1)]]
- 관련: [[Windows PowerShell 실행 정책이 npm 전역 CLI를 차단한다]], [[붙여넣기 이식성은 빈 프로젝트와 인코딩 매트릭스로 검증한다]]
