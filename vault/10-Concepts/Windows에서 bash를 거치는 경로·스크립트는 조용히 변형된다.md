---
title: Windows에서 bash를 거치는 경로·스크립트는 조용히 변형된다
tags:
  - tool/windows
  - tool/claude-code
  - dev/debugging
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/Paths-and-Scripts-That-Pass-Through-Bash-on-Windows-Get-Silently-Mangled
created: 2026-11-21
sources:
  - "[[2026-11-02 해당 폴거 정보 읽고 우리가 이번에 상시 커피챗을 개설하려는데 공식 웹에서 이를 받으려고 해. 루트 폴더에 (8597bfd5)]]"
  - "[[2026-11-03 ide_opened_fileThe user opened the file cUsersUSERDesktophan (cf9e06de)]]"
---

## 한 줄 요약

Windows의 Claude Code는 훅 명령과 Bash 도구 명령을 Git Bash로 실행하므로, **따옴표 없는 백슬래시 경로·heredoc 스크립트·CRLF 패치가 셸을 지나며 다른 문자열로 바뀐다** — 아무도 출력을 보지 않는 훅에서는 흔적 없이 멈춘다. 경로는 슬래시와 따옴표로 쓰고, 스크립트는 파일로 만들어 실행한다.

## 내용

- 대표 사례(훅): `~/.claude/settings.json`의 SessionEnd 훅을 `C:\Users\<user>\...\python.exe C:\...\archive_session.py`처럼 따옴표 없는 백슬래시 경로로 적었다. bash가 `\`를 이스케이프로 처리해 명령은 `C:Users<user>AppData...python.exe: command not found`(exit 127)가 됐다.
- 흔적이 남지 않았다: 스크립트가 시작조차 못 해 스크립트 안 try/except의 오류 로그도 쓰이지 않았다. 세션 아카이브 파이프라인이 약 두 달 멈췄고(마지막 아카이브 10-02, 발견 11-21), Claude Code의 기본 30일 트랜스크립트 정리와 겹쳐 약 10-05~10-21 세션은 영구 유실됐다.
- 진단: 훅에 적힌 명령 문자열을 그대로 `bash -c '<명령>'`으로, 표준 입력에 샘플 JSON을 넣어 돌리면 exit 127이 재현된다. 같은 스크립트를 직접 실행하면 정상이다 — 고장 난 것은 스크립트가 아니라 명령 문자열이다.
- 수정과 감시: 경로를 슬래시와 따옴표로 바꾼다(`"C:/Users/<user>/.../python.exe" "C:/.../archive_session.py"`). 그리고 정기 실행 때마다 '가장 최근 아카이브 날짜 vs 오늘'을 비교해, 파이프라인이 멈추면 며칠 안에 알아채게 한다.
- 같은 계열 — heredoc 백슬래시: Bash 도구에 heredoc으로 넘긴 스크립트에서 백슬래시가 반으로 줄어 정규식이 깨졌다. 따옴표 없는 구분자(`<<EOF`)가 `\\`를 `\`로 바꾸는 bash 동작과 일치한다.
- 같은 계열 — 파싱·줄바꿈: 따옴표·특수문자가 섞인 인라인 heredoc 스크립트가 파싱 오류로 두 번 깨졌고, 작업 트리가 CRLF(`core.autocrlf=true`)인 저장소에서는 수정 스크립트의 줄바꿈이 두 번 깨졌다. 규칙: 새 파일은 LF로 써도 git이 정규화하고, 기존 CRLF 파일 패치는 Python `open(..., newline='')`로 열어 `\r\n`을 명시하며, heredoc에는 `\r\n`을 싣지 않는다.
- 공통 해법: bash를 지나는 문자열은 경로라면 슬래시와 따옴표로, 스크립트·패치라면 파일 쓰기 도구로 파일을 만든 뒤 실행한다. 셸 인용 규칙을 거치지 않으니 세 증상이 함께 사라진다 — 셸 경계를 지나는 텍스트는 파일로 우회시키라는 cp949 함정의 교훈과 같은 패턴이다.

## 출처

- [[2026-11-02 해당 폴거 정보 읽고 우리가 이번에 상시 커피챗을 개설하려는데 공식 웹에서 이를 받으려고 해. 루트 폴더에 (8597bfd5)]]
- [[2026-11-03 ide_opened_fileThe user opened the file cUsersUSERDesktophan (cf9e06de)]]
- 관련: [[플러그인 훅은 캐시 디렉토리에서 수동 실행해 진단한다]], [[fire-and-forget 훅은 침묵 실패한다]], [[Windows cp949 인코딩 함정 모음]]
