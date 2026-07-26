# SETUP.md — Claude Code 실행용 런북

> **이 문서는 Claude Code에게 주는 작업 지시서입니다.**
> 사용법: 이 파일과 `bootstrap.sh`, `cc2obsidian.py`, `obsidian-llm-wiki-guide.md` 를 같은 폴더에 두고,
> 그 폴더에서 `claude` 를 실행한 뒤 아래 한 줄을 입력하세요.
>
> ```
> SETUP.md 를 읽고 PHASE 0부터 순서대로 진행해줘. 각 STOP 지점에서는 반드시 멈추고 나한테 물어봐.
> ```

---

## 역할과 목표

당신(Claude Code)은 사용자의 Obsidian LLM 위키를 셋업합니다.
최종 결과물은 `~/llm-wiki` 볼트이며, 그 안에 과거 Claude Code 세션이 마크다운으로 아카이브되어 있어야 합니다.

## 절대 규칙

1. **STOP 표시가 있는 지점에서는 반드시 멈추고 사용자에게 묻습니다.** 임의로 다음 단계로 넘어가지 않습니다.
2. **`bootstrap.sh` 를 수정하지 않습니다.** 동작이 이상하면 사용자에게 보고합니다.
3. **파일을 삭제하지 않습니다.** 정리가 필요하면 사용자에게 목록을 보여주고 승인받습니다.
4. **`~/.claude/` 안의 원본 세션 로그를 절대 수정·삭제하지 않습니다.** 읽기만 합니다.
5. 명령 출력은 **요약하지 말고 중요한 부분을 그대로** 사용자에게 보여줍니다. 특히 개수와 에러 메시지.
6. 한 PHASE가 끝나면 무엇을 했는지 2~3줄로 보고합니다.

---

## PHASE 0 — 환경 확인

이 단계에서는 아무것도 변경하지 않습니다.

```bash
uname -s
python3 --version
git --version
command -v jq  || echo "jq 없음"
command -v rg  || echo "ripgrep 없음"
ls -d ~/.claude/projects 2>/dev/null || echo "projects 디렉터리 없음"
find ~/.claude/projects -maxdepth 2 -name '*.jsonl' 2>/dev/null | wc -l
du -sh ~/.claude/projects 2>/dev/null
```

**판단 기준**

| 상황 | 조치 |
|---|---|
| `python3` 없음 | 여기서 중단. 설치 방법 안내 후 사용자 응답 대기 |
| `projects 디렉터리 없음` | **STOP.** `CLAUDE_CONFIG_DIR` 를 바꿨는지 사용자에게 확인 |
| 세션 파일 0개 | **STOP.** 보관 기간(기본 30일)이 지나 정리되었을 수 있다고 알림 |
| `jq` / `rg` 없음 | 진행 가능. 스크립트에 대체 경로가 있음. 단 사용자에게 언급 |
| Windows(`uname` 이 MINGW/MSYS) | Git Bash 또는 WSL에서 실행해야 함을 알리고 확인 |

> **STOP 1.** 위 결과와 세션 개수를 사용자에게 보고하고, 계속할지 확인받습니다.

---

## PHASE 1 — 볼트 생성 (`init`)

```bash
bash bootstrap.sh init
```

이 명령이 하는 일 — 사용자에게 미리 이렇게 설명하세요:

1. `~/.claude/projects` 를 `~/claude-sessions-backup-<날짜>` 로 복사
2. `~/.claude/settings.json` 의 `cleanupPeriodDays` 를 3650으로 변경 (원본은 `.bak` 으로 보관)
3. `~/llm-wiki` 볼트 폴더 구조 생성
4. `cc2obsidian.py` 를 `_scripts/`, 가이드 문서를 `99-Meta/` 로 배치
5. 볼트 규칙서 `CLAUDE.md`, 시드 노트, 템플릿 생성
6. `.gitignore` 생성(`90-Archive/` 제외) 및 `git init`

이미 있는 파일은 덮어쓰지 않으며, 여러 번 실행해도 안전합니다.

실패하면 어느 단계(`1/7` ~ `7/7`)에서 멈췄는지 그대로 보고하고 중단합니다.

확인:

```bash
bash bootstrap.sh status
```

> **STOP 2.** `status` 출력을 보여주고, 볼트 경로가 원하는 위치가 맞는지 확인받습니다.
> 다른 경로를 원하면 이후 모든 명령 앞에 `VAULT=/원하는/경로` 를 붙여 다시 실행합니다.

---

## PHASE 2 — 변환 미리보기

**파일을 쓰지 않는 단계입니다. 반드시 import 전에 실행합니다.**

```bash
cd ~/llm-wiki
bash _scripts/bootstrap.sh preview
```

출력에서 확인할 것:

- 변환 대상 개수
- 세션 제목들이 알아볼 만한지
- 에러 발생 여부

**개수에 따른 권고**

| 개수 | 권고 |
|---|---|
| ~50개 | 그대로 진행 |
| 50~200개 | `--min-prompts 4` 로 좁히기 권장 |
| 200개 초과 | `--since <최근 6개월>` + `--min-prompts 4` 강력 권장. 나중에 더 넣으면 됨 |

옵션을 붙여 다시 미리보기:

```bash
bash _scripts/bootstrap.sh preview --since 2026-01-01 --min-prompts 4
```

에러가 나면 `--debug` 를 붙여 다시 실행하고, 출력을 사용자에게 그대로 보여준 뒤 중단합니다.

> **STOP 3.** 대상 개수와 제목 샘플 10개를 보여주고, 이 범위로 변환할지 사용자에게 확정받습니다.
> **사용자 승인 없이 PHASE 3으로 넘어가지 않습니다.**

---

## PHASE 3 — 실제 변환

PHASE 2에서 확정한 옵션을 **그대로** 붙여 실행합니다.

```bash
bash _scripts/bootstrap.sh import --since 2026-01-01 --min-prompts 4
```

확인:

```bash
bash _scripts/bootstrap.sh status
ls ~/llm-wiki/90-Archive/claude-sessions/
head -30 "$(find ~/llm-wiki/90-Archive/claude-sessions -name '*.md' | head -1)"
```

샘플 노트의 앞부분을 사용자에게 보여주고, 프로퍼티와 본문이 제대로 들어갔는지 함께 확인합니다.

---

## PHASE 4 — 비밀정보 검사 (건너뛰기 금지)

```bash
bash _scripts/bootstrap.sh scan
```

- **종료 코드 0** → HIGH 항목 없음. MEDIUM 결과는 사용자에게 그대로 보여주고 판단을 맡깁니다.
- **종료 코드 1** → HIGH 항목 발견. 다음을 수행합니다:
  1. 어느 파일의 몇 번째 줄인지 사용자에게 보고
  2. **파일을 임의로 지우거나 고치지 않습니다**
  3. 해당 키를 폐기(rotate)하라고 안내
  4. `.gitignore` 에서 `90-Archive/` 를 빼지 말라고 경고
  5. **STOP.** 사용자 지시 대기

검사를 통과했고 사용자가 아카이브까지 git에 넣고 싶어 하면, 그때만 `.gitignore` 의 `90-Archive/` 줄을 지웁니다.

첫 커밋은 사용자 승인 후에만:

```bash
cd ~/llm-wiki && git add -A && git status --short | head -30
```

> **STOP 4.** `git status` 결과를 보여주고 커밋 여부를 확인받습니다.

---

## PHASE 5 — Obsidian 연결 안내

여기서부터는 사용자가 GUI에서 직접 해야 합니다. 다음을 안내하세요.

1. Obsidian 실행 → **"폴더를 볼트로 열기(Open folder as vault)"** → `~/llm-wiki` 선택
2. 설정 → 코어 플러그인: `백링크`, `그래프 뷰`, `템플릿` 켜기
3. 설정 → 커뮤니티 플러그인 → 제한 모드 해제 → **Dataview** 설치·활성화
4. 설정 → 파일 및 링크 → "새 링크 형식" → `짧은 경로`, "위키링크 사용" 켜기
5. 설정 → 템플릿 → 템플릿 폴더를 `_templates` 로 지정
6. `50-MOC/정제 대기열.md` 를 열어 표가 렌더링되는지 확인 (Dataview가 켜져야 보임)

그다음 VS Code에서:

```bash
cd ~/llm-wiki && code .
```

VS Code 통합 터미널에서 `claude` 를 실행합니다. **Obsidian은 켜둔 채로 두라고** 안내하세요.
파일 변경이 몇 초 안에 Obsidian에 반영되므로, 결과를 보면서 작업할 수 있습니다.

> **STOP 5.** 셋업 완료 보고. 볼트 경로, 변환된 노트 수, 다음 할 일을 정리해 보여줍니다.

---

## 셋업 이후 — 정기 작업

셋업이 끝난 뒤 사용자가 요청할 때 수행하는 작업들입니다. 볼트 루트의 `CLAUDE.md` 규칙을 따릅니다.

### 주간 정제 (핵심 루틴)

```
90-Archive/claude-sessions/ 에서 status가 raw인 노트 중 최근 10개를 읽고,
재사용 가능한 교훈이 있는 것과 없는 것으로 분류해줘. 아직 파일은 만들지 마.
```

이때 당신이 할 일:

1. 해당 노트들을 읽습니다
2. **분류 결과만 표로 제시**합니다 — 교훈 있음 / 없음, 한 줄 근거
3. 교훈이 없는 것은 프로퍼티를 `status: triaged` 로만 바꿉니다
4. 교훈이 있는 것은 **개념 노트 제목 후보를 3개씩 제안하고 사용자의 선택을 기다립니다**
5. 제목이 정해지면 `10-Concepts/` 에 `_templates/개념 노트.md` 형식으로 생성
6. 원본 노트에 `status: distilled` 및 역링크를 남깁니다

**한 번에 5개를 초과해 생성하지 않습니다.**

### 세션 요약본 만들기 (토큰 소모 있음)

로그 전체 대신 정제된 초안이 필요할 때. 공식 스크립트 인터페이스입니다:

```bash
claude -p --resume <세션ID> --output-format json \
  "이 세션에서 배운 재사용 가능한 교훈만 뽑아줘. 형식: ## 문제 / ## 원인 / ## 해결 / ## 일반화 가능한 원칙. 프로젝트 고유 세부사항은 제외." \
  | jq -r '.result' > ~/llm-wiki/00-Inbox/요약-<주제>.md
```

세션 ID는 아카이브 노트의 `session_id` 프로퍼티에 있습니다.

### 신규 세션 자동 아카이브 (선택)

앞으로의 세션을 자동으로 볼트에 넣고 싶을 때. `~/.claude/settings.json` 에 `SessionEnd` 훅을 추가합니다.
훅의 입력에는 `transcript_path` 필드가 들어옵니다.

**이 설정은 사용자에게 먼저 제안하고 승인받은 뒤에만 적용합니다.**
훅 스키마는 버전에 따라 다를 수 있으므로, 적용 전에 `code.claude.com/docs/en/hooks` 를 확인하도록 안내하세요.

### 재귀 주의

이 볼트에서 Claude Code를 쓰면 그 대화도 `~/.claude/projects/-...-llm-wiki/` 에 쌓입니다.
나중에 다시 import 할 때 "위키를 만드는 대화"까지 위키에 들어오는 걸 막으려면 필터를 씁니다:

```bash
bash _scripts/bootstrap.sh preview --project myapp
```

---

## 트러블슈팅

| 증상 | 조치 |
|---|---|
| `cc2obsidian.py 를 찾을 수 없습니다` | 파일을 `~/llm-wiki/_scripts/` 또는 `bootstrap.sh` 와 같은 폴더에 두고 재실행 |
| `.jsonl 파일을 찾지 못했습니다` | `--src` 로 실제 경로 지정. `CLAUDE_CONFIG_DIR` 확인 |
| 노트 제목이 전부 UUID | 세션 요약이 없는 경우. 정상 동작이며 정제 단계에서 제목을 다시 붙임 |
| 파싱 에러가 다수 | JSONL 내부 포맷은 버전마다 바뀔 수 있음(공식 문서 명시). `--debug` 출력 보고 후 `/export` 로 우회 |
| Dataview 표가 안 보임 | 플러그인 미설치 또는 미활성. 설정 → 커뮤니티 플러그인 확인 |
| 노트가 너무 김 | `--max-chars` 를 줄여 재변환 (예: `--max-chars 15000`) |
