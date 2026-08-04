---
title: plugin uninstall은 마켓플레이스 한정자를 무시한다
tags:
  - tool/claude-code
  - dev/debugging
status: distilled
publish: true
lang: ko
translation: en/10-Concepts/plugin-uninstall-Ignores-the-Marketplace-Qualifier
created: 2026-08-04
sources:
  - "[[2026-07-15 ~.claudeskills 와 .claudeskills 안에 있는 스킬 폴더 목록과 각 SKILL.md 파일 (b9221c3a)]]"
---

## 한 줄 요약

`claude plugin uninstall 이름@마켓플레이스` 형태로 정확히 지정해도 **CLI는 `@` 뒤의 마켓플레이스 한정자를 무시하고 플러그인 이름만으로 매칭**하기 때문에, 같은 이름의 플러그인이 두 마켓플레이스에 설치돼 있으면 의도하지 않은 쪽이 지워질 수 있다.

## 내용

- 실제 사례: `superpowers@superpowers-marketplace`를 제거해 달라고 지정했는데, CLI가 한정자를 무시하고 이름 `superpowers`로만 매칭해서 다른 마켓플레이스(claude-plugins-official) 쪽 사본을 삭제했다.
- 즉 `이름@마켓플레이스` 문법은 uninstall에서 정밀 타게팅을 보장하지 않는다 — 어느 사본이 지워질지는 CLI의 이름 매칭에 달려 있다.
- 예방책: **같은 이름의 플러그인을 두 마켓플레이스에서 동시에 설치하지 말 것.** 이름이 유일하면 이 문제 자체가 발생하지 않는다.
- 복구 절차: 잘못된 쪽이 지워졌다면, 남아 있는 사본을 마저 uninstall한 뒤 원하는 마켓플레이스에서 다시 install한다 (지운 것을 "되돌리는" 방법은 없다).
- 완충 요인: 두 사본이 같은 버전이면 스킬 목록에 중복 노출될 뿐 내용은 동일하므로, 어느 쪽이 지워져도 기능이 사라지지는 않는다 — 문제가 되는 건 버전이 다르거나 한쪽만 남기고 싶을 때다.

## 출처

- [[2026-07-15 ~.claudeskills 와 .claudeskills 안에 있는 스킬 폴더 목록과 각 SKILL.md 파일 (b9221c3a)]]
