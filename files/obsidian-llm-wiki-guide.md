---
title: Obsidian LLM 위키 구축 가이드
tags:
  - moc
  - meta/guide
created: 2026-07-26
---

# Obsidian으로 LLM 위키 만들기 + Claude Code 세션 가져오기

> 짧은 답부터: **네, 지금까지의 Claude Code 세션도 가져올 수 있습니다.** 전부 로컬에 파일로 남아 있습니다.
> 단, 기본 보관 기간이 **30일**이라 오래된 건 이미 지워졌을 수 있습니다. → [[#0. 지금 당장 할 일 백업]]

---

## 0. 지금 당장 할 일: 백업

다른 걸 읽기 전에 이것부터 하세요. Claude Code는 세션 로그를 30일이 지나면 정리합니다(`cleanupPeriodDays` 설정, 기본 30).

```bash
# 1) 통째로 백업 (몇 초면 끝납니다)
cp -r ~/.claude/projects ~/claude-sessions-backup-$(date +%Y%m%d)

# 2) 앞으로는 지우지 않도록 보관 기간 늘리기
#    ~/.claude/settings.json 에 추가:
#    { "cleanupPeriodDays": 3650 }
```

무엇이 남아 있는지 먼저 확인:

```bash
ls ~/.claude/projects                      # 프로젝트별 폴더 목록
find ~/.claude/projects -name '*.jsonl' | wc -l   # 총 세션 개수
du -sh ~/.claude/projects                  # 전체 용량
rg -i "찾고싶은키워드" ~/.claude/projects   # 전체 검색 (ripgrep)
```

---

## 1. 큰 그림: 3층 구조

**가장 중요한 조언 하나**: 세션 로그를 통째로 볼트에 쏟아붓고 "위키 완성"이라고 하면, 검색은 되지만 아무도 안 읽는 무덤이 됩니다. 위키의 가치는 *로그*가 아니라 *로그에서 뽑아낸 결론*에 있습니다.

세 층으로 나누세요.

```
[3층] MOC / 인덱스     ← 주제별 진입점. 손으로 관리. 10~30개.
          ↑ 링크
[2층] 정제 노트        ← "RAG 청킹 전략", "JWT 만료 버그 패턴" 같은 개념 노트.
          ↑ 출처 링크    한 노트 = 한 개념. 여기가 진짜 위키.
[1층] 원본 아카이브    ← Claude Code 세션 로그 그대로. 자동 생성. 절대 손으로 안 고침.
```

1층은 자동화, 2층은 사람(+LLM)이 만들고, 3층은 2층이 쌓이면 자연히 생깁니다.
1층 노트에는 **절대 위키 링크를 촘촘히 걸지 마세요.** 그래프가 스파게티가 됩니다.

---

## 2. Obsidian 최소한만 알기

Obsidian을 처음 쓴다면 이 6개면 시작하기 충분합니다. 나머지는 필요할 때 배우세요.

| 개념 | 설명 |
|---|---|
| **볼트(Vault)** | 그냥 **폴더 하나**입니다. 그 안의 `.md` 파일들이 전부. DB도 락인도 없습니다. |
| **`[[링크]]`** | `[[노트 이름]]` 이라고 쓰면 그 노트로 연결됩니다. 없는 노트면 클릭 시 생성됩니다. |
| **백링크** | 나를 링크한 노트 목록. 노트 하단/우측 패널에 자동 표시. **위키의 핵심 기능.** |
| **태그** | 본문에 `#llm/rag`, 또는 프로퍼티에 `tags:`. 계층형(`#llm/rag/chunking`) 지원. |
| **프로퍼티(Properties)** | 파일 맨 위의 YAML 블록. `date`, `status`, `tags` 등 구조화 데이터. |
| **`![[임베드]]`** | 다른 노트의 내용을 이 노트 안에 끼워 넣습니다. |

### 프로퍼티 예시

```markdown
---
title: RAG 청킹 전략
tags:
  - llm/rag
status: distilled
confidence: high
sources:
  - "[[2026-07-01 임베딩 파이프라인 튜닝 (9f558c28)]]"
---

# RAG 청킹 전략

고정 크기 청킹은 ...
```

### 처음 켜야 할 것

- **설정 → 코어 플러그인**: `백링크`, `아웃고잉 링크`, `그래프 뷰`, `템플릿`, `데일리 노트` 켜기
- **설정 → 파일 및 링크 → "새 링크 형식"** → `상대 경로` 또는 `짧은 경로` (폴더 옮겨도 링크 안 깨짐)
- **설정 → 편집기 → "위키링크 사용"** 켜기

### 커뮤니티 플러그인 (딱 3개만)

| 플러그인 | 왜 |
|---|---|
| **Dataview** | 프로퍼티로 자동 목록/표 생성. `status: raw`인 노트 목록 같은 걸 쿼리로 뽑습니다. |
| **Templater** | 노트 생성 시 템플릿 자동 삽입. 위키 일관성 유지에 필수. |
| **Omnisearch** | 기본 검색보다 훨씬 나은 전문 검색. 로그가 수백 개가 되면 체감됩니다. |

> LLM 연동 플러그인(Copilot, Smart Connections, Text Generator 등)도 있지만, **처음엔 넣지 마세요.**
> 볼트 구조가 잡히기 전에 붙이면 쓰레기를 빠르게 양산합니다. 어차피 Claude Code를 볼트에서 직접 돌리는 게 더 강력합니다([[#6. Claude Code를 볼트 안에서 돌리기]]).

---

## 3. 볼트 폴더 구조 제안

번호를 붙이면 정렬이 고정돼서 편합니다.

```
llm-wiki/
├── 00-Inbox/              # 정제 안 된 아무 메모. 주 1회 비우기.
├── 10-Concepts/           # ★ 진짜 위키. 개념 하나 = 노트 하나.
│   ├── RAG 청킹 전략.md
│   ├── 컨텍스트 윈도우 관리.md
│   └── 프롬프트 캐싱.md
├── 20-Techniques/         # 재사용 가능한 레시피/패턴
├── 30-Tools/              # Claude Code, LangChain, vLLM 등 도구별 노트
├── 40-Projects/           # 프로젝트별 노트 (진행 중인 것)
├── 50-MOC/                # 주제별 지도 노트
│   └── LLM MOC.md
├── 90-Archive/
│   └── claude-sessions/   # ★ 자동 생성된 세션 로그. 읽기 전용 취급.
│       ├── myapp/
│       └── blog/
├── _templates/            # Templater 템플릿
└── CLAUDE.md              # ★ Claude Code용 볼트 규칙서
```

**폴더보다 링크가 중요합니다.** 어디에 뒀는지 고민되면 `10-Concepts`에 던지고 링크를 거세요.

---

## 4. Claude Code 세션은 어디 있고, 어떻게 가져오나

### 저장 위치 (사실 확인됨)

```
~/.claude/projects/<프로젝트-경로-인코딩>/<세션ID>.jsonl
```

- 프로젝트 폴더명 = 작업 디렉터리 절대경로에서 영숫자가 아닌 문자를 `-`로 바꾼 것
  (예: `/Users/alice/code/myapp` → `-Users-alice-code-myapp`)
- 한 줄에 JSON 객체 하나(JSONL). 내 프롬프트, Claude 응답, 도구 호출이 시간순으로 기록
- `<세션ID>/subagents/` 하위 폴더에는 서브에이전트 대화가 따로 저장됨
- `CLAUDE_CONFIG_DIR` 환경변수를 바꿨다면 위치도 달라짐

> ⚠️ **주의**: 공식 문서는 이 JSONL의 **내부 포맷이 버전마다 바뀔 수 있다**고 명시합니다.
> 직접 파싱하는 스크립트는 언젠가 깨질 수 있으니, 중요한 자동화는 `/export`나 아래 공식 인터페이스를 쓰세요.

---

### 방법 A — `/export` (가장 안전, 세션 1개씩)

세션 안에서:

```
/export
```

메뉴가 뜨면서 클립보드 복사 / 파일 저장을 고를 수 있습니다. 파일명을 붙이면 메뉴 없이 바로 저장:

```
/export ~/llm-wiki/90-Archive/claude-sessions/2026-07-26-auth-debug.md
```

지난 세션을 꺼내려면 먼저 재개한 뒤 export 하면 됩니다:

```bash
claude --resume          # 세션 선택창. Ctrl+A 로 전체 프로젝트 보기
# 세션 진입 후 → /export <파일경로>
```

### 방법 B — 전체 일괄 변환 (`cc2obsidian.py`)

수십~수백 개 세션을 한 번에 옮길 때. 함께 제공한 스크립트를 쓰세요.

```bash
# 1) 먼저 뭐가 나올지 확인 (파일 안 씀)
python3 cc2obsidian.py --out ~/llm-wiki/90-Archive/claude-sessions --dry-run

# 2) 실제 변환 + 인덱스 노트 생성
python3 cc2obsidian.py \
  --out ~/llm-wiki/90-Archive/claude-sessions \
  --since 2026-01-01 \
  --min-prompts 3 \
  --index
```

주요 옵션:

| 옵션 | 의미 |
|---|---|
| `--dry-run` | 쓰지 않고 목록만 출력 (항상 먼저 실행) |
| `--since 2026-01-01` | 해당 날짜 이후 세션만 |
| `--project myapp` | 프로젝트 이름 부분 일치 필터 |
| `--min-prompts 3` | 발화 3개 미만인 잡세션 제외 (기본 2) |
| `--max-chars 40000` | 노트 하나 최대 길이. 0이면 무제한 |
| `--index` | Dataview 쿼리가 포함된 MOC 인덱스 노트 생성 |
| `--src` | `~/.claude/projects` 가 아닐 때 경로 지정 |

스크립트가 하는 일:
- 서브에이전트 로그, 도구 결과 원문(엄청 길어서), thinking 블록은 제외
- 도구 호출은 `🔧 Bash — npm test` 같은 한 줄 요약으로 압축
- 프로퍼티(`session_id`, `project`, `date`, `tools`, `status: raw`)를 자동으로 붙임
- 깨진 줄/알 수 없는 필드는 조용히 건너뜀 (포맷이 바뀌어도 전체가 죽지 않게)

### 방법 C — 앞으로의 세션은 자동 아카이브 (SessionEnd 훅)

세션이 끝날 때마다 자동으로 볼트에 넣습니다. `~/.claude/settings.json`:

```json
{
  "cleanupPeriodDays": 3650,
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.transcript_path' | xargs -I{} cp {} ~/llm-wiki/90-Archive/claude-sessions/_raw/"
          }
        ]
      }
    ]
  }
}
```

훅은 입력으로 `transcript_path` 필드를 받습니다. 위는 원본 JSONL을 복사만 하는 최소 버전이고,
`cc2obsidian.py`를 호출하도록 바꾸면 바로 마크다운으로 떨어집니다.
(훅 스키마는 버전에 따라 다를 수 있으니 `/docs` 또는 code.claude.com/docs/en/hooks 확인)

### 방법 D — 요약본만 뽑기 (토큰 좀 쓰지만 품질 최고)

전체 로그 대신 **정제된 위키 초안**을 바로 받고 싶을 때. 공식 스크립트 인터페이스입니다:

```bash
claude -p --resume <세션ID> --output-format json \
  "이 세션에서 배운 재사용 가능한 교훈만 뽑아 마크다운으로 정리해줘. \
   형식: ## 문제 / ## 원인 / ## 해결 / ## 일반화할 수 있는 원칙. \
   프로젝트 고유 세부사항은 빼고." \
  | jq -r '.result' > ~/llm-wiki/00-Inbox/세션요약.md
```

세션 ID는 `~/.claude/projects/*/`의 파일명이거나 `claude --resume` 목록에서 확인할 수 있습니다.

**권장 조합**: 과거 세션은 B로 벌크 아카이브 → 그중 쓸만한 것만 D로 요약 → C로 앞으로를 자동화.

---

## 5. 로그를 위키로 바꾸는 실제 워크플로

자동 변환이 끝나면 1층만 생긴 상태입니다. 여기서 멈추면 아무 의미 없습니다.

**주 1회, 30분 루틴:**

1. `90-Archive`에서 `status: raw`인 노트 중 최근 것 5개를 봅니다 (Dataview 쿼리로 목록화)
2. 각 노트를 훑고 **"6개월 뒤에도 쓸모 있는 문장"**이 있는지 봅니다
   - 없다 → 프로퍼티를 `status: triaged`로 바꾸고 끝. 다시 안 봅니다.
   - 있다 → 3번으로
3. `10-Concepts`에 **개념 이름으로** 노트를 만들거나 기존 노트에 추가합니다
   - 좋은 제목: `프롬프트 캐싱 히트율 떨어지는 조건`
   - 나쁜 제목: `2026-07-01 작업 로그`
4. 개념 노트에 출처 링크: `출처:: [[2026-07-01 임베딩 파이프라인 튜닝 (9f558c28)]]`
5. 원본 노트는 `status: distilled`로 변경

이 루틴 하나가 "파일 더미"와 "위키"를 가릅니다.

### 도움 되는 Dataview 쿼리

정제 대기열 (`50-MOC/정제 대기열.md`에 붙여넣기):

````markdown
```dataview
TABLE date AS 날짜, project AS 프로젝트, turns AS 턴수
FROM #claude-code/session
WHERE status = "raw"
SORT date DESC
LIMIT 20
```
````

고아 노트(아무도 링크 안 한 개념 노트) 찾기:

````markdown
```dataview
LIST
FROM "10-Concepts"
WHERE length(file.inlinks) = 0
```
````

---

## 6. Claude Code를 볼트 안에서 돌리기

이게 이 셋업의 가장 큰 무기입니다. 볼트가 그냥 마크다운 폴더이므로, Claude Code를 그 안에서 실행하면 **위키 전체를 읽고 쓰는 에이전트**가 됩니다.

```bash
cd ~/llm-wiki
claude
```

그러면 이런 게 됩니다:

- "90-Archive의 지난주 세션들 읽고, 반복되는 실수 패턴 찾아서 10-Concepts에 노트로 만들어줘"
- "10-Concepts 노트들 중 서로 링크가 없는데 주제가 겹치는 쌍 찾아줘"
- "50-MOC/LLM MOC.md 를 현재 노트 목록 기준으로 갱신해줘"

### 볼트에 `CLAUDE.md` 두기

Claude Code가 위키 규칙을 지키도록 볼트 루트에 규칙서를 둡니다.

```markdown
# 이 볼트에 대하여

Obsidian 기반 개인 LLM 위키입니다. 모든 파일은 마크다운.

## 규칙
- 링크는 `[[노트 제목]]` 위키링크만 사용. 마크다운 링크 금지.
- 모든 새 노트는 YAML 프로퍼티 필수: title, tags, status, created
- status 값: raw | triaged | distilled
- 노트 제목은 **명제나 개념**으로. 날짜/로그 형식 제목 금지.
- 한 노트 = 한 개념. 길어지면 쪼개고 링크로 연결.
- `90-Archive/` 는 자동 생성물. **수정하지 말 것.** 읽기만.
- 태그는 계층형: `llm/rag`, `llm/finetuning`, `tool/claude-code`

## 자주 쓰는 작업
- 정제: 90-Archive 로그 → 10-Concepts 개념 노트로 승격
- MOC 갱신: 50-MOC/*.md 의 링크 목록 최신화
```

---

## 7. 첫 주 실행 계획

| 일차 | 할 일 | 소요 |
|---|---|---|
| 1일 | 백업(`cp -r ~/.claude/projects ...`) + `cleanupPeriodDays: 3650` 설정 | 5분 |
| 1일 | Obsidian 설치, 볼트 생성, 폴더 구조 만들기, 코어 플러그인 켜기 | 20분 |
| 2일 | `cc2obsidian.py --dry-run` → 실제 변환 → 결과 훑어보기 | 20분 |
| 3일 | Dataview + Templater 설치, 정제 대기열 노트 만들기 | 20분 |
| 4~5일 | 세션 5개만 골라 손으로 개념 노트 5개 만들기 (**여기서 감을 잡습니다**) | 1시간 |
| 6일 | 볼트에 `CLAUDE.md` 작성, `cd ~/llm-wiki && claude` 로 정제 시켜보기 | 30분 |
| 7일 | SessionEnd 훅 설정, 볼트 git 초기화 | 20분 |

---

## 8. 주의점

- **비밀정보**: 세션 로그에는 API 키, 토큰, 내부 코드, 고객 데이터가 그대로 남아 있을 수 있습니다.
  볼트를 git에 올리거나 동기화하기 전에 반드시 검사하세요.
  ```bash
  rg -i "api[_-]?key|secret|password|sk-ant|Bearer " ~/llm-wiki/90-Archive/
  ```
  `.gitignore`에 `90-Archive/` 를 넣어두는 것도 방법입니다.

- **노트 폭발**: 세션 500개를 다 옮기지 마세요. `--since`, `--min-prompts`로 걸러서 시작하고, 필요하면 나중에 더 넣으면 됩니다.

- **포맷 변경 리스크**: JSONL 내부 포맷은 공식적으로 불안정합니다. 스크립트가 어느 날 이상하게 동작하면 `--debug`로 확인하고, 안 되면 `/export`로 우회하세요.

- **자동화의 함정**: LLM에게 요약을 전부 맡기면 "그럴듯한데 내 것이 아닌" 노트가 쌓입니다.
  최소한 개념 노트의 **제목만큼은 직접 정하세요.** 제목을 정하는 행위가 곧 이해입니다.

- **볼트 버전 관리**: 볼트 폴더에서 `git init`. 마크다운이라 diff가 깔끔합니다.
