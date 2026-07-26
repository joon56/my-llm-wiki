# LLM WIKI

개인 LLM 지식 위키. [Obsidian](https://obsidian.md)으로 작성·관리하고, [Quartz 4](https://quartz.jzhao.xyz)로 정적 사이트를 빌드해 GitHub Pages에 공개 발행한다. Claude Code 세션 로그는 자동 아카이브되고, 주간 `/distill` 루틴으로 재사용 가능한 교훈만 개념 노트로 승격된다.

사이트: https://joon56.github.io/my-llm-wiki/ (Pages 활성화 후)

## 구조

```
LLM_WIKI/                        ← git 루트 (모노레포)
├── vault/                       ← Obsidian 볼트. 콘텐츠 전부
│   ├── 00-Inbox/                # 미정제 메모. 주 1회 비움
│   ├── 10-Concepts/             # 핵심 위키. 개념 1 = 노트 1
│   ├── 20-Techniques/           # 재사용 레시피/패턴
│   ├── 30-Tools/                # Claude Code, vLLM 등 도구별 노트
│   ├── 40-Projects/             # 진행 중 프로젝트 노트
│   ├── 50-MOC/                  # 주제별 지도 노트 (사이트 홈 역할)
│   ├── 90-Archive/claude-sessions/  # 세션 로그 md. 로컬 전용, 읽기 전용, 발행 금지
│   ├── 99-Meta/                 # 위키 사용법·가이드
│   ├── _templates/              # Templater 템플릿
│   └── CLAUDE.md                # 볼트 규칙서 (필독)
├── site/                        ← Quartz 4. vault/를 콘텐츠 소스로 빌드
├── scripts/                     ← Python 도구
│   ├── cc2obsidian.py           # JSONL → md 변환
│   ├── archive_session.py       # SessionEnd 훅 진입점
│   ├── secret_scan.py           # 비밀정보 스캔 (CI 게이트 겸용)
│   └── tests/                   # unittest 11개
├── .claude/commands/distill.md  # 주간 정제 루틴 커맨드
├── .github/workflows/deploy.yml # 스캔 → 빌드 → Pages 배포
└── docs/superpowers/            # 설계 스펙·구현 계획
```

## 셋업

### 1. Obsidian

1. Obsidian 실행 → **폴더를 볼트로 열기(Open folder as vault)** → `vault/` 선택
2. 설정 → 코어 플러그인: **백링크**, **그래프 뷰**, **템플릿** 켜기
3. 설정 → 커뮤니티 플러그인 → 제한 모드 해제 → 아래 3개만 설치·활성화
   - **Dataview**
   - **Templater**
   - **Omnisearch**
4. 설정 → 템플릿(또는 Templater) → 템플릿 폴더를 `_templates` 로 지정
5. 설정 → 파일 및 링크 → "새 링크 형식"을 **짧은 경로**로, "위키링크 사용" 켜기
6. `vault/.obsidian/`이 생성되면 워크스페이스 파일(`workspace*.json`, `cache`)은 이미 `.gitignore`에 제외되어 있음 — 설정 파일만 커밋

플러그인이 3개뿐인 이유: LLM 관련 플러그인은 의도적으로 배제한다. 볼트 안에서 Claude Code를 직접 실행하는 쪽이 대체 수단이다.

### 2. Node (사이트 빌드)

```bash
cd site
npm install
npx quartz build -d ../vault -o public          # 정적 사이트를 site/public 에 생성
npx quartz build -d ../vault -o public --serve   # 로컬 프리뷰: http://localhost:8080
```

`site/package.json`의 `engines`는 `node >= 22`, `npm >= 10.9.2`를 요구한다.

> **Quartz는 upstream `v4` 브랜치를 `git clone --branch v4`로 고정 vendoring한 버전(4.5.2)이다.** upstream 기본 브랜치는 이미 v5로 넘어갔으므로, 나중에 재설치·업그레이드할 때는 `git clone --branch v4 https://github.com/jackyzha0/quartz.git` 처럼 브랜치를 명시해야 한다. 그냥 clone하면 v5가 받아지고 이 저장소의 커스텀 컴포넌트(브루탈리즘 테마, 폰트 self-host)와 호환되지 않을 수 있다.

### 3. Python (도구)

표준 라이브러리만 사용, 외부 의존성 없음. Windows에서는 `python` 대신 `py` 런처 사용을 권장(이 저장소 스크립트는 UTF-8 stdio를 명시적으로 강제하므로 어느 쪽이든 동작한다).

```bash
cd scripts
py -m unittest      # 테스트 11개
```

## 일상 워크플로

```
노트 작성/편집 (Obsidian)
  → 공개하고 싶은 노트에 publish: true 설정
  → git add & commit & push
  → GitHub Actions: secret_scan → quartz build → Pages 배포 (자동)
```

- **발행 여부는 `publish: true` 프로퍼티로만 결정한다.** 기본값은 미발행(Quartz `ExplicitPublish` 필터).
- `vault/90-Archive/`는 Quartz `ignorePatterns`에도 들어있어 `publish: true`를 걸어도 발행되지 않는다. 이 폴더 자체가 `.gitignore` 대상(로컬 전용)이라 git에도 올라가지 않는다.
- 새 노트는 `_templates/`의 형식(YAML: `title`, `tags`, `status`, `created`)을 따른다. 링크는 `[[위키링크]]`만 사용 — 마크다운 링크 금지. 자세한 규칙은 `vault/CLAUDE.md` 참고.

### 세션 자동 아카이브

`SessionEnd` 훅이 전역 설정에 등록되어 있어, Claude Code 세션이 끝날 때마다 `scripts/archive_session.py`가 실행되어 해당 세션을 `vault/90-Archive/claude-sessions/`에 `status: raw`로 저장한다. 훅은 best-effort — 실패해도 세션 종료를 막지 않고 `_hook-errors.log`에만 기록한다.

기존 세션을 한 번에 가져오고 싶을 때(수동 일괄 import):

```bash
py scripts/cc2obsidian.py --out vault/90-Archive/claude-sessions --min-prompts 3 --index
```

`--min-prompts`로 발화 수가 적은 세션(테스트성 대화 등)을 걸러낸다. `--index`는 MOC 인덱스 노트를 함께 생성한다. 전체 옵션은 `py scripts/cc2obsidian.py --help`.

### /distill — 주간 정제

`.claude/commands/distill.md`. `vault/90-Archive/claude-sessions/`에서 `status: raw`인 최근 노트를 읽고, 재사용 가능한 교훈이 있는지 분류한다.

1. 분류표만 먼저 제시 (이 단계에서 파일 생성 금지)
2. 교훈 없음 → 프로퍼티만 `status: triaged`
3. 교훈 있음 → 개념 노트 제목 후보 3개 제안 → **사용자가 제목을 확정** (자동화가 제목을 임의로 정하지 않도록 하는 안전장치)
4. 확정된 것만 `vault/10-Concepts/`에 `_templates/개념 노트.md` 형식으로 생성 (`publish`는 항상 `false`로 시작, 발행 여부는 사용자가 별도 결정)
5. 원본 노트는 `status: distilled`로 변경 + 역링크 남김

한 번에 개념 노트 5개 초과 생성하지 않음.

### secret 스캔 (로컬 실행)

```bash
py scripts/secret_scan.py vault
```

`sk-ant-…`, `AKIA…`, GitHub 토큰, PEM 프라이빗 키 등은 HIGH — 발견 시 exit 1. `Bearer …` 토큰, `api_key = "..."` 형태의 제네릭 시크릿은 MEDIUM(경고만, exit 0). CI(`.github/workflows/deploy.yml`)에서는 빌드 전 `python3 scripts/secret_scan.py vault`가 실행되어 HIGH 발견 시 배포 자체를 막는다.

HIGH가 나오면: 파일을 임의로 고치거나 지우지 말고, 해당 키를 먼저 폐기(rotate)한 뒤 노트에서 제거한다.

## 트러블슈팅

| 증상 | 원인/조치 |
|---|---|
| Dataview 표/쿼리가 사이트에 안 보임 | **정상 동작.** Dataview는 Obsidian 전용 플러그인이며 Quartz 빌드에는 관여하지 않는다. 렌더된 결과를 보고 싶으면 Obsidian에서 확인 |
| cc2obsidian 변환 중 파싱 에러 다수 | Claude Code의 JSONL 트랜스크립트 포맷은 **비공식**이며 버전마다 바뀔 수 있다. `--debug`로 원인 확인 후, 다수 실패 시 `/export` 명령으로 세션을 내보내 우회 |
| 노트 제목이 UUID로만 나옴 | 세션에 요약이 없는 경우. 정상이며, `/distill` 단계에서 사람이 제목을 다시 붙인다 |
| 노트가 너무 김 | `cc2obsidian.py --max-chars 15000` 처럼 줄여서 재변환 |
| Quartz 빌드 후 90-Archive 콘텐츠가 사이트에 보임 | 있어선 안 됨. `site/quartz.config.ts`의 `ignorePatterns`에 `"90-Archive"`가 포함돼 있는지 확인하고, `grep -ril "90-Archive" site/public/`으로 검증 |
| `secret_scan.py`가 개인 키를 못 잡음 | `PATTERNS`는 알려진 형식(Anthropic/OpenAI/AWS/GitHub/PEM)만 커버하는 휴리스틱이다. 완전한 보증이 아니므로 커밋 전 육안 확인 습관화 |
| Windows에서 한글 깨짐 | 이 저장소 스크립트는 stdout/stderr를 UTF-8로 강제 재설정한다. 그래도 깨지면 터미널 코드페이지(`chcp 65001`) 확인 |

## 테스트

```bash
cd scripts && py -m unittest
```
