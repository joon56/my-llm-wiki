#!/usr/bin/env bash
#
# bootstrap.sh — Obsidian LLM 위키 셋업 자동화
#
# 서브커맨드:
#   init      볼트 폴더 생성, 세션 백업, 설정, CLAUDE.md, git 초기화
#   preview   세션 변환 미리보기 (파일 안 씀)
#   import    세션을 실제로 마크다운 변환
#   scan      비밀정보 검사
#   status    현재 상태 요약
#
# 사용:
#   bash bootstrap.sh init
#   bash bootstrap.sh preview --since 2026-01-01
#   bash bootstrap.sh import --since 2026-01-01 --min-prompts 3
#   bash bootstrap.sh scan
#
# 환경변수:
#   VAULT              볼트 경로 (기본: ~/llm-wiki)
#   CLAUDE_CONFIG_DIR  Claude Code 설정 경로 (기본: ~/.claude)
#
# 모든 서브커맨드는 여러 번 실행해도 안전합니다(idempotent).

set -euo pipefail

VAULT="${VAULT:-$HOME/llm-wiki}"
CC_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
PROJECTS_DIR="$CC_DIR/projects"
ARCHIVE_REL="90-Archive/claude-sessions"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ---------------------------------------------------------------- 출력 헬퍼
c_reset=$'\033[0m'; c_ok=$'\033[32m'; c_warn=$'\033[33m'; c_err=$'\033[31m'; c_dim=$'\033[2m'
say()  { printf '%s\n' "$*"; }
ok()   { printf '%s✓%s %s\n' "$c_ok" "$c_reset" "$*"; }
warn() { printf '%s!%s %s\n' "$c_warn" "$c_reset" "$*"; }
err()  { printf '%s✗%s %s\n' "$c_err" "$c_reset" "$*" >&2; }
dim()  { printf '%s%s%s\n' "$c_dim" "$*" "$c_reset"; }
hdr()  { printf '\n──── %s ────\n' "$*"; }

die() { err "$*"; exit 1; }

# ---------------------------------------------------------------- 사전 점검
require_python() {
  command -v python3 >/dev/null 2>&1 || die "python3 가 필요합니다. 설치 후 다시 실행하세요."
}

find_converter() {
  local candidates=(
    "$VAULT/_scripts/cc2obsidian.py"
    "$SCRIPT_DIR/cc2obsidian.py"
    "$PWD/cc2obsidian.py"
    "$HOME/Downloads/cc2obsidian.py"
  )
  for f in "${candidates[@]}"; do
    [ -f "$f" ] && { printf '%s' "$f"; return 0; }
  done
  return 1
}

# ---------------------------------------------------------------- init
cmd_init() {
  require_python

  hdr "1/7  세션 로그 백업"
  if [ -d "$PROJECTS_DIR" ]; then
    local n size dest
    n=$(find "$PROJECTS_DIR" -maxdepth 2 -name '*.jsonl' -type f 2>/dev/null | wc -l | tr -d ' ')
    size=$(du -sh "$PROJECTS_DIR" 2>/dev/null | cut -f1)
    dest="$HOME/claude-sessions-backup-$(date +%Y%m%d)"
    if [ -d "$dest" ]; then
      ok "백업이 이미 있습니다: $dest"
    else
      cp -r "$PROJECTS_DIR" "$dest"
      ok "백업 완료: $dest"
    fi
    ok "세션 파일 ${n}개, 용량 ${size}"
    [ "$n" -eq 0 ] && warn "세션 파일이 0개입니다. 보관 기간이 지나 정리되었을 수 있습니다."
  else
    warn "세션 디렉터리를 찾을 수 없습니다: $PROJECTS_DIR"
    warn "CLAUDE_CONFIG_DIR 를 바꿨다면 환경변수로 지정하고 다시 실행하세요."
  fi

  hdr "2/7  보관 기간 연장"
  local settings="$CC_DIR/settings.json"
  if command -v jq >/dev/null 2>&1; then
    mkdir -p "$CC_DIR"
    if [ -f "$settings" ]; then
      cp "$settings" "$settings.bak-$(date +%Y%m%d%H%M%S)"
      local cur
      cur=$(jq -r '.cleanupPeriodDays // "unset"' "$settings")
      if [ "$cur" = "3650" ]; then
        ok "cleanupPeriodDays 이미 3650"
      else
        jq '.cleanupPeriodDays = 3650' "$settings" > "$settings.tmp" && mv "$settings.tmp" "$settings"
        ok "cleanupPeriodDays: $cur → 3650 (원본은 .bak 으로 보관)"
      fi
    else
      printf '{\n  "cleanupPeriodDays": 3650\n}\n' > "$settings"
      ok "생성: $settings"
    fi
  else
    warn "jq 가 없어 자동 수정을 건너뜁니다. 직접 $settings 에 아래를 추가하세요:"
    dim '    { "cleanupPeriodDays": 3650 }'
  fi

  hdr "3/7  볼트 폴더 생성"
  mkdir -p "$VAULT"/{00-Inbox,10-Concepts,20-Techniques,30-Tools,40-Projects,50-MOC,99-Meta,_scripts,_templates}
  mkdir -p "$VAULT/$ARCHIVE_REL"
  ok "$VAULT"

  hdr "4/7  스크립트 배치"
  local conv
  if conv=$(find_converter); then
    if [ "$conv" != "$VAULT/_scripts/cc2obsidian.py" ]; then
      cp "$conv" "$VAULT/_scripts/cc2obsidian.py"
      ok "cc2obsidian.py → _scripts/ (원본: $conv)"
    else
      ok "cc2obsidian.py 이미 배치됨"
    fi
  else
    err "cc2obsidian.py 를 찾을 수 없습니다."
    dim "  다음 위치 중 하나에 두고 다시 실행하세요: $VAULT/_scripts/, $SCRIPT_DIR/, ~/Downloads/"
    exit 1
  fi
  [ -f "$SCRIPT_DIR/bootstrap.sh" ] && [ "$SCRIPT_DIR" != "$VAULT/_scripts" ] \
    && cp "$SCRIPT_DIR/bootstrap.sh" "$VAULT/_scripts/bootstrap.sh"
  for g in obsidian-llm-wiki-guide.md SETUP.md; do
    for src in "$SCRIPT_DIR/$g" "$HOME/Downloads/$g" "$PWD/$g"; do
      if [ -f "$src" ] && [ ! -f "$VAULT/99-Meta/$g" ]; then
        cp "$src" "$VAULT/99-Meta/$g"; ok "$g → 99-Meta/"; break
      fi
    done
  done

  hdr "5/7  CLAUDE.md 규칙서"
  if [ -f "$VAULT/CLAUDE.md" ]; then
    ok "CLAUDE.md 이미 존재 — 덮어쓰지 않음"
  else
    cat > "$VAULT/CLAUDE.md" <<'CLAUDEMD'
# 이 볼트에 대하여

Obsidian 기반 개인 LLM 위키. 모든 콘텐츠는 마크다운 파일이다.

## 절대 규칙

- `90-Archive/` 는 자동 생성된 원본 세션 로그다. **읽기만 하고 절대 수정·삭제하지 않는다.**
  정제 결과는 항상 새 노트로 만든다.
- 노트를 새로 만들거나 옮기기 전에 **반드시 사용자에게 제목 후보를 제시하고 확인받는다.**
  제목을 정하는 건 사용자의 몫이다.
- 한 번에 5개 이상의 노트를 생성하지 않는다. 먼저 계획을 보여주고 승인받는다.

## 폴더

| 폴더 | 용도 |
|---|---|
| `00-Inbox/` | 미분류 메모. 주 1회 비운다 |
| `10-Concepts/` | 핵심. 개념 하나 = 노트 하나 |
| `20-Techniques/` | 재사용 가능한 레시피·패턴 |
| `30-Tools/` | 도구별 노트 (Claude Code, vLLM 등) |
| `40-Projects/` | 진행 중 프로젝트 |
| `50-MOC/` | 주제별 지도 노트 |
| `90-Archive/` | 자동 생성물. 수정 금지 |
| `99-Meta/` | 이 볼트 자체에 대한 문서 |

## 노트 규칙

- 링크는 `[[노트 제목]]` 위키링크만. 마크다운 링크 금지
- 모든 새 노트에 YAML 프로퍼티 필수: `title`, `tags`, `status`, `created`
- `status` 값: `raw` → `triaged` → `distilled`
- 제목은 **개념이나 명제**로 짓는다
  - 좋음: `프롬프트 캐싱 히트율이 떨어지는 조건`
  - 나쁨: `2026-07-01 작업 로그`, `RAG 정리`
- 한 노트 = 한 개념. 길어지면 쪼개고 링크로 연결
- 태그는 계층형: `llm/rag`, `llm/finetuning`, `tool/claude-code`
- 정제 노트에는 출처를 남긴다: `출처:: [[원본 노트 제목]]`

## 자주 하는 작업

- **정제**: `90-Archive/` 로그를 읽고 재사용 가능한 교훈을 `10-Concepts/` 노트로 승격
- **MOC 갱신**: `50-MOC/*.md` 의 링크 목록을 현재 노트 기준으로 최신화
- **고아 노트 점검**: 아무도 링크하지 않는 `10-Concepts/` 노트 찾기
CLAUDEMD
    ok "CLAUDE.md 생성"
  fi

  hdr "6/7  시드 노트 · 템플릿"
  if [ ! -f "$VAULT/50-MOC/정제 대기열.md" ]; then
    cat > "$VAULT/50-MOC/정제 대기열.md" <<'QUEUE'
---
title: 정제 대기열
tags:
  - moc
---

# 정제 대기열

> Dataview 플러그인을 설치해야 아래 표가 보입니다.

## 아직 안 본 세션

```dataview
TABLE date AS 날짜, project AS 프로젝트, turns AS 턴수
FROM #claude-code/session
WHERE status = "raw"
SORT date DESC
LIMIT 20
```

## 봤지만 정제 안 한 것

```dataview
TABLE date AS 날짜, project AS 프로젝트
FROM #claude-code/session
WHERE status = "triaged"
SORT date DESC
```

## 고아 개념 노트 (아무도 링크 안 함)

```dataview
LIST
FROM "10-Concepts"
WHERE length(file.inlinks) = 0
```
QUEUE
    ok "50-MOC/정제 대기열.md"
  else
    ok "정제 대기열.md 이미 존재"
  fi

  if [ ! -f "$VAULT/_templates/개념 노트.md" ]; then
    cat > "$VAULT/_templates/개념 노트.md" <<'TPL'
---
title: 
tags:
  - llm/
status: distilled
created: 
출처: 
---

# 

## 요점

## 상세

## 언제 안 통하나

## 관련
- 
TPL
    ok "_templates/개념 노트.md"
  fi

  hdr "7/7  git"
  if [ ! -f "$VAULT/.gitignore" ]; then
    cat > "$VAULT/.gitignore" <<'GI'
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.trash/
.DS_Store

# 세션 원본 로그에는 키·토큰이 남아 있을 수 있습니다.
# `bash _scripts/bootstrap.sh scan` 으로 검사한 뒤에만 아래 줄을 지우세요.
90-Archive/
GI
    ok ".gitignore 생성 (90-Archive 는 기본 제외)"
  fi
  if [ ! -d "$VAULT/.git" ]; then
    (cd "$VAULT" && git init -q 2>/dev/null) && ok "git 저장소 초기화" || warn "git 초기화 실패(무시 가능)"
  else
    ok "git 저장소 이미 존재"
  fi

  hdr "완료"
  say "다음 단계:"
  dim "  bash $VAULT/_scripts/bootstrap.sh preview"
}

# ---------------------------------------------------------------- preview / import
run_converter() {
  require_python
  local script="$VAULT/_scripts/cc2obsidian.py"
  [ -f "$script" ] || die "먼저 'bootstrap.sh init' 을 실행하세요."
  python3 "$script" --src "$PROJECTS_DIR" --out "$VAULT/$ARCHIVE_REL" "$@"
}

cmd_preview() {
  hdr "변환 미리보기 (파일을 쓰지 않습니다)"
  run_converter --dry-run "$@"
  say ""
  dim "개수가 너무 많으면 --since 2026-01-01 --min-prompts 4 등으로 좁히세요."
  dim "괜찮으면: bash _scripts/bootstrap.sh import $*"
}

cmd_import() {
  hdr "세션 변환"
  run_converter --index "$@"
  say ""
  warn "다음은 반드시 비밀정보 검사입니다:"
  dim "  bash _scripts/bootstrap.sh scan"
}

# ---------------------------------------------------------------- scan
cmd_scan() {
  local target="$VAULT/$ARCHIVE_REL"
  [ -d "$target" ] || die "아직 변환된 노트가 없습니다: $target"

  hdr "비밀정보 검사"

  # 실제 키 포맷 — 걸리면 반드시 조치해야 함
  local high='sk-ant-[A-Za-z0-9_-]{10,}|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{30,}|xox[baprs]-[A-Za-z0-9-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----'
  # 단순 언급 — 대부분 오탐이지만 눈으로 확인할 것
  local med="(api[_-]?key|secret|passwd|password|access[_-]?token|client[_-]?secret)[\"']?[[:space:]]*[:=][[:space:]]*[\"']?[A-Za-z0-9._/+-]{12,}|Bearer [A-Za-z0-9._-]{12,}"

  local grepper=(grep -rEIn --color=never)
  command -v rg >/dev/null 2>&1 && grepper=(rg -nI --no-heading --color never -e)

  local hits=0
  say "[HIGH] 실제 키 형식"
  if "${grepper[@]}" "$high" "$target" 2>/dev/null | head -40; then :; fi
  if "${grepper[@]}" "$high" "$target" >/dev/null 2>&1; then
    hits=1
    err "위 항목은 실제 자격증명일 가능성이 높습니다. 해당 노트를 삭제하고 키를 폐기(rotate)하세요."
  else
    ok "발견되지 않음"
  fi

  say ""
  say "[MEDIUM] 키워드=값 패턴 (오탐 많음, 눈으로 확인)"
  if "${grepper[@]}" "$med" "$target" 2>/dev/null | head -30; then :; fi
  "${grepper[@]}" "$med" "$target" >/dev/null 2>&1 || ok "발견되지 않음"

  say ""
  if [ "$hits" -eq 1 ]; then
    err "검사 실패 — 정리 전까지 .gitignore 에서 90-Archive/ 를 빼지 마세요."
    return 1
  fi
  ok "HIGH 항목 없음. 그래도 MEDIUM 결과는 직접 확인하세요."
}

# ---------------------------------------------------------------- status
cmd_status() {
  hdr "상태"
  printf '  볼트          %s\n' "$VAULT"
  printf '  세션 원본     %s\n' "$PROJECTS_DIR"
  if [ -d "$PROJECTS_DIR" ]; then
    printf '  원본 세션 수  %s\n' "$(find "$PROJECTS_DIR" -maxdepth 2 -name '*.jsonl' | wc -l | tr -d ' ')"
  else
    printf '  원본 세션 수  %s\n' "(디렉터리 없음)"
  fi
  local a="$VAULT/$ARCHIVE_REL"
  printf '  변환된 노트   %s\n' "$([ -d "$a" ] && find "$a" -name '*.md' | wc -l | tr -d ' ' || echo 0)"
  printf '  개념 노트     %s\n' "$([ -d "$VAULT/10-Concepts" ] && find "$VAULT/10-Concepts" -name '*.md' | wc -l | tr -d ' ' || echo 0)"
  printf '  CLAUDE.md     %s\n' "$([ -f "$VAULT/CLAUDE.md" ] && echo 있음 || echo 없음)"
  printf '  git           %s\n' "$([ -d "$VAULT/.git" ] && echo 초기화됨 || echo 없음)"
}

# ---------------------------------------------------------------- 디스패치
usage() {
  sed -n '3,25p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
}

sub="${1:-help}"; shift || true
case "$sub" in
  init)    cmd_init "$@" ;;
  preview) cmd_preview "$@" ;;
  import)  cmd_import "$@" ;;
  scan)    cmd_scan "$@" ;;
  status)  cmd_status "$@" ;;
  help|-h|--help) usage ;;
  *) err "알 수 없는 명령: $sub"; usage; exit 1 ;;
esac
