---
title: IDE에서 되는 빌드가 터미널에서 깨지면 런타임부터 본다
tags:
  - tool/windows
  - dev/tooling
  - dev/debugging
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/When-a-Build-Works-in-the-IDE-but-Fails-in-the-Terminal,-Check-the-Runtime-First
created: 2026-11-21
sources:
  - "[[2026-08-15 백그라운드 에뮬 중지해줘 (b94a3c60)]]"
---

## 한 줄 요약

IDE는 자기가 번들한 런타임(JDK·Node·Python)을 쓰고, 터미널과 에이전트 셸은 PATH·`JAVA_HOME`의 시스템 런타임을 쓴다 — **IDE에서는 되는 빌드가 터미널에서만 깨지면 코드보다 런타임 버전 차이를 먼저 의심한다.**

## 내용

- 증상: Claude Code가 PowerShell에서 `.\gradlew :app:assembleDebug :mobile:assembleDebug`를 돌리자 빌드가 실패했다. 원인은 시스템 기본 JVM 8이었다 — Android Studio 안에서는 내장 JDK(JBR)를 쓰므로 IDE 빌드만 됐다.
- 해결: `$env:JAVA_HOME = 'C:\Program Files\Android\Android Studio\jbr'`로 IDE의 JBR을 지정하고 다시 빌드하자 워치 앱 APK(34.4MB)와 폰 동반 앱 APK(10.1MB)가 모두 나왔다.
- 정리 명령에도 같은 지정이 필요하다: 빌드 뒤 `gradlew --stop`으로 데몬을 끌 때도 `JAVA_HOME`을 다시 지정했다. 에이전트 셸은 명령 사이에 환경 변수를 유지하지 않으므로 같은 명령 줄에 함께 쓴다.
- 기록해야 반복되지 않는다: 해결 직후 프로젝트 메모리에 규칙 파일(`gradle-needs-jbr-java-home`)로 남겼다 — 다음 세션이 같은 실패에서 다시 시작하지 않는다.
- 진단 순서: 터미널의 `java -version`(또는 `node -v`, `python --version`)과 IDE 설정에 잡힌 런타임 경로를 나란히 본다. 다르면 IDE 쪽 경로를 환경 변수로 넘겨 재현한다.
- 일반화: 번들 런타임 대 시스템 런타임 문제는 Android만의 일이 아니다. "IDE에서는 되는데 CI·터미널·에이전트에서는 안 된다"는 증상의 첫 용의자다.

## 출처

- [[2026-08-15 백그라운드 에뮬 중지해줘 (b94a3c60)]]
- 관련: [[Windows PowerShell 실행 정책이 npm 전역 CLI를 차단한다]], [[프로젝트 메모리 디렉토리로 세션 간 컨텍스트를 잇는다]], [[Windows에서 bash를 거치는 경로·스크립트는 조용히 변형된다]]
