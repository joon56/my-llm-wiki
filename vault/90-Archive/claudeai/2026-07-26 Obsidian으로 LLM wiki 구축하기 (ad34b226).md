---
title: "Obsidian으로 LLM wiki 구축하기"
source: claude-ai
session_id: ad34b226-9a45-4a0f-971c-cfd31f3388fa
date: 2026-07-26
turns: 6
prompts: 3
status: distilled
tags:
  - claude-ai/session
---

# Obsidian으로 LLM wiki 구축하기

> [!info] claude.ai 대화 원본입니다. 배운 것은 개념 노트로 옮기고, 여기엔 링크만 거세요.

**정제 메모**
- 핵심 교훈:: [[자기 로그를 다루는 도구의 재귀 오염 함정]], [[비밀정보 검사는 경고가 아닌 실패로 자동화를 막는다]]
- 관련 노트:: 

---

## 🙋 나

내가 obsidian 등을 이용하여 LLM wiki를 만드려고 하는데 obsidian 사용법을 잘 모르기도 하고 md 파일을 기준으로 구성한다고 아는데 내가 여태까지 claude code에서 진행한 세션들에 대해서도 진행이 가능한지 잘 몰라.
가이드 제시해줘.

### 🤖 Claude

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

결론부터: **가능합니다.** Claude Code는 모든 세션을 `~/.claude/projects/<프로젝트경로>/<세션ID>.jsonl` 로 로컬에 저장하고 있고, 이건 그냥 파일이라 마크다운으로 변환해서 볼트에 넣을 수 있습니다.

다만 먼저 알아야 할 게 두 가지입니다.

**하나, 지금 바로 백업하세요.** 세션 로그는 기본 30일이 지나면 정리됩니다 (`cleanupPeriodDays`). 가이드를 읽기 전에 이것부터:

```bash
cp -r ~/.claude/projects ~/claude-sessions-backup-$(date +%Y%m%d)
find ~/.claude/projects -name '*.jsonl' | wc -l   # 뭐가 남았는지 확인
```

**둘, 로그를 통째로 붓는 게 위키가 아닙니다.** 이게 가장 흔한 실패 패턴이라 가이드의 절반을 여기에 썼습니다. 세션 로그 300개를 볼트에 넣으면 검색은 되지만 아무도 안 읽는 무덤이 됩니다. 원본 아카이브(자동 생성) / 개념 노트(사람이 정제) / MOC 세 층으로 나누고, 진짜 위키는 가운데 층에서 만들어집니다.

첨부한 두 파일입니다.

**가이드**에는 Obsidian 최소 개념 6개(볼트=폴더, `[[링크]]`, 백링크, 태그, 프로퍼티, 임베드), 볼트 폴더 구조, 세션 가져오는 네 가지 방법, 주 1회 정제 루틴, 첫 주 일정표가 들어 있습니다. Obsidian이 처음이라도 순서대로 따라가면 됩니다.

**`cc2obsidian.py`** 는 과거 세션 전체를 한 번에 마크다운으로 변환하는 스크립트입니다. 서브에이전트 로그와 도구 결과 원문(엄청 깁니다)은 걸러내고, 도구 호출은 한 줄로 압축하고, `session_id`/`project`/`date`/`status` 프로퍼티를 자동으로 붙입니다.

```bash
python3 cc2obsidian.py --out ~/llm-wiki/90-Archive/claude-sessions --dry-run   # 먼저 이걸로 확인
```

한 가지 주의할 점은, 공식 문서가 이 JSONL의 내부 포맷은 버전마다 바뀔 수 있다고 명시하고 있다는 겁니다. 그래서 스크립트는 모르는 필드를 무시하도록 방어적으로 짰지만, 언젠가 깨질 수 있습니다. 안정성이 중요한 자동화는 `/export` 명령이나 `claude -p --resume <세션ID> --output-format json` 쪽을 쓰는 게 낫고, 둘 다 가이드에 예제로 넣어뒀습니다.

그리고 이 구성의 진짜 장점은 마지막에 나옵니다 — 볼트가 그냥 마크다운 폴더라서, `cd ~/llm-wiki && claude` 로 Claude Code를 볼트 안에서 돌리면 위키 전체를 읽고 정제하는 에이전트가 됩니다. 볼트 루트에 둘 `CLAUDE.md` 규칙서 예시도 같이 넣어뒀습니다.

## 🙋 나

이 두 파일로 어떻게 하라는 거야? 일단 작업은 아마 vscode에 claude code에서 할 거 같긴 한데, 정확하게 흐름을 알려줘.

### 🤖 Claude

두 파일의 성격이 다릅니다. 여기서 헷갈리신 것 같아요.

- **`obsidian-llm-wiki-guide.md`** → 실행하는 게 아니라 **읽는 문서**입니다. 마크다운이니까 볼트 안에 넣으면 그대로 첫 번째 노트가 됩니다.
- **`cc2obsidian.py`** → **딱 한 번 돌리는 도구**입니다. 과거 세션을 마크다운으로 뽑아내고 나면 역할 끝(이후엔 가끔만).

전체 흐름을 순서대로 정리하면 이렇습니다. macOS/Linux 기준이고, Windows면 `~/.claude` 대신 `%USERPROFILE%\.claude` 입니다.

## 1단계 · 백업 (터미널, 3분)

다른 거 하기 전에 이것부터. 30일 지난 세션은 이미 지워지고 있습니다.

```bash
cp -r ~/.claude/projects ~/claude-sessions-backup-$(date +%Y%m%d)
find ~/.claude/projects -name '*.jsonl' | wc -l
```

마지막 숫자가 앞으로 다룰 세션 개수입니다. 0이 나오면 경로가 다른 거니 거기서 멈추고 알려주세요.

## 2단계 · 볼트 폴더 만들고 두 파일 배치 (터미널, 3분)

볼트 = 그냥 폴더입니다. 이 폴더가 앞으로 **Obsidian 볼트이자 VS Code 작업 폴더**가 됩니다. 하나의 폴더를 두 프로그램이 같이 보는 구조예요.

```bash
mkdir -p ~/llm-wiki/{00-Inbox,10-Concepts,20-Techniques,30-Tools,40-Projects,50-MOC,90-Archive,_scripts,_templates,99-Meta}

# 다운로드한 두 파일을 각자 자리로
mv ~/Downloads/cc2obsidian.py            ~/llm-wiki/_scripts/
mv ~/Downloads/obsidian-llm-wiki-guide.md ~/llm-wiki/99-Meta/
```

가이드를 `99-Meta/`에 넣는 이유는, Obsidian을 열자마자 그 가이드를 **볼트 안에서 읽으면서** 따라가게 하려는 겁니다.

## 3단계 · 변환 스크립트 실행 (터미널, 5분)

먼저 `--dry-run`으로 뭐가 나올지만 봅니다. 이 단계에선 파일이 하나도 안 생깁니다.

```bash
cd ~/llm-wiki
python3 _scripts/cc2obsidian.py --out 90-Archive/claude-sessions --dry-run
```

목록이 쭉 나옵니다. 여기서 판단하세요.

- 개수가 200개 넘게 나온다 → 너무 많습니다. `--since 2026-01-01 --min-prompts 4` 를 붙여 줄이세요.
- 제목들이 알아볼 만하다 → 그대로 진행
- 에러가 난다 → `--debug` 붙여서 나온 메시지를 알려주세요

괜찮으면 `--dry-run`을 빼고 실제로 씁니다.

```bash
python3 _scripts/cc2obsidian.py --out 90-Archive/claude-sessions --min-prompts 3 --index
```

## 4단계 · 비밀정보 검사 (터미널, 1분)

세션 로그엔 API 키가 그대로 남아 있을 수 있습니다. git에 올리기 전에 반드시.

```bash
rg -i "api[_-]?key|secret|password|sk-ant|Bearer " 90-Archive/
```

뭔가 걸리면 해당 노트를 지우거나, `.gitignore`에 `90-Archive/`를 넣으세요.

## 5단계 · Obsidian에서 열기 (Obsidian, 5분)

Obsidian 실행 → **"폴더를 볼트로 열기(Open folder as vault)"** → `~/llm-wiki` 선택.

열리면 `99-Meta/obsidian-llm-wiki-guide.md`를 여세요. 이제부터는 그 가이드의 2장(플러그인 설정)과 5장(정제 루틴)을 볼트 안에서 보면서 따라가면 됩니다.

바로 켤 것: 설정 → 코어 플러그인에서 `백링크`, `그래프 뷰`, `템플릿`. 커뮤니티 플러그인은 `Dataview` 하나만.

## 6단계 · VS Code + Claude Code (여기가 본 작업)

```bash
cd ~/llm-wiki
code .        # VS Code로 볼트 폴더 열기
```

VS Code 통합 터미널에서 `claude` 실행. **Obsidian은 켜둔 채로** 두세요. Claude Code가 파일을 고치면 Obsidian에 몇 초 안에 반영되고, 그걸 보면서 작업하는 게 이 셋업의 핵심입니다.

첫 작업은 볼트 규칙서를 만드는 것입니다. Claude Code에 이렇게:

```
99-Meta/obsidian-llm-wiki-guide.md 를 읽고, 거기 6장에 있는
CLAUDE.md 예시를 볼트 루트에 만들어줘. 현재 폴더 구조에 맞게 조정해서.
```

그 다음부터는 이런 식으로 씁니다.

```
90-Archive/claude-sessions/ 에서 최근 10개 노트를 읽고,
반복해서 나오는 문제 패턴 3~5개를 뽑아줘. 아직 파일은 만들지 말고 목록만.
```

```
그중 2번, 4번을 10-Concepts/ 에 개념 노트로 만들어줘.
제목은 내가 정할 테니 후보를 3개씩 제안하고 기다려줘.
```

## 두 가지 주의

**첫째, `90-Archive/`는 Claude Code가 고치지 못하게 하세요.** CLAUDE.md에 "읽기만, 수정 금지"라고 명시해야 합니다. 원본 로그가 오염되면 복구가 안 됩니다.

**둘째, 이제부터 볼트에서 돌리는 Claude Code 세션도 로그로 쌓입니다.** `~/.claude/projects/-Users-당신-llm-wiki/` 라는 폴더가 새로 생기고, 나중에 스크립트를 또 돌리면 "위키 만드는 대화"까지 위키에 들어옵니다. 재귀를 피하려면 다음부터는 `--project` 필터를 쓰세요.

정리하면 **1~4단계는 터미널에서 한 번, 5단계는 Obsidian 설정 한 번, 6단계부터가 계속 반복하는 실제 작업**입니다. 앞의 다섯 단계는 30분이면 끝납니다.

## 🙋 나

그럼 터미널 명령까지 해서 흐름 가이드를 적거나 해줘. 그대로 claude code에 읽혀서 자동화로 생성할 예정이야.

### 🤖 Claude

터미널 명령까지 전부 들어간, Claude Code가 그대로 읽고 실행할 수 있는 형태로 만들겠습니다. 스크립트를 실제로 돌려서 검증한 뒤 드릴게요.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

4개 파일을 샌드박스에서 처음부터 끝까지 실제로 돌려서 검증했습니다.

**쓰는 법은 두 줄입니다.** 4개 파일을 아무 폴더(예: `~/Downloads`)에 모아두고:

```bash
cd ~/Downloads && claude
```

Claude Code가 뜨면:

```
SETUP.md 를 읽고 PHASE 0부터 순서대로 진행해줘. 각 STOP 지점에서는 반드시 멈추고 나한테 물어봐.
```

끝입니다. 나머지는 Claude Code가 진행합니다.

## 각 파일의 역할

| 파일 | 역할 |
|---|---|
| **SETUP.md** | Claude Code에게 주는 실행 지시서. PHASE 0~5, 판단 기준, STOP 지점, 트러블슈팅 |
| **bootstrap.sh** | 실제 작업하는 스크립트. `init`/`preview`/`import`/`scan`/`status` |
| **cc2obsidian.py** | 세션 JSONL → 마크다운 변환기. bootstrap이 내부에서 호출 |
| **obsidian-llm-wiki-guide.md** | 사람이 읽는 개념 문서. `99-Meta/`로 자동 배치됨 |

## 자동화에서 일부러 막아둔 것

전부 자동으로 흘려보내면 위험한 지점이 있어서 **5개의 STOP 게이트**를 넣었습니다.

- **STOP 3 (미리보기 → 변환)** — 여기가 제일 중요합니다. 세션이 300개면 노트 300개가 쏟아지고 볼트가 시작부터 망가집니다. `preview`로 개수를 보고 `--since`, `--min-prompts`로 좁힌 뒤에만 진행하게 했습니다.
- **STOP 4 (비밀정보 검사)** — `scan`이 실제 키 형식(`sk-ant-`, `ghp_`, `AKIA` 등)을 찾으면 **exit 1로 실패**하고 git 커밋을 막습니다. 오염된 볼트로 테스트해서 정상 차단되는 것까지 확인했습니다.
- **파일 삭제·수정 금지** — 키가 발견돼도 Claude Code가 임의로 지우지 않고 보고만 하게 했습니다.

`bootstrap.sh init`은 여러 번 돌려도 안전합니다. 기존 `CLAUDE.md`나 노트를 덮어쓰지 않고, `settings.json`은 수정 전에 `.bak`을 남깁니다.

## 미리 알아둘 것

**Windows면 Git Bash나 WSL에서 실행해야 합니다.** PowerShell에서는 안 돕니다. PHASE 0에서 감지해서 알려주긴 합니다.

**`jq`와 `ripgrep`은 없어도 됩니다.** 대체 경로가 있고, 없으면 수동 안내가 나옵니다. 있으면 더 매끄럽습니다.

**PHASE 5(Obsidian GUI 설정)는 자동화 불가입니다.** 플러그인 설치는 손으로 해야 해서, Claude Code가 체크리스트만 안내합니다.

**재귀 주의** — 이 볼트에서 Claude Code를 쓰기 시작하면 그 대화도 세션 로그로 쌓입니다. 나중에 다시 import할 때 "위키 만드는 대화"가 위키에 들어오는 걸 막으려면 `--project` 필터를 쓰라고 SETUP.md에 적어뒀습니다.

한 가지 남은 리스크는 JSONL 내부 포맷이 Claude Code 버전마다 바뀔 수 있다는 점(공식 문서에 명시된 사항)입니다. 파서를 방어적으로 짜서 모르는 필드는 건너뛰지만, 언젠가 결과가 이상해지면 `--debug`로 확인하고 `/export`로 우회하는 절차까지 트러블슈팅에 넣어뒀습니다.

