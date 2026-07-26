# LLM WIKI 설계 스펙

날짜: 2026-07-26
상태: 사용자 승인 대기 → 승인 시 구현 계획(writing-plans)으로 이행

## 1. 목표

개인 LLM 지식 위키. Obsidian으로 작성·관리하고, Quartz 4로 빌드한 정적 사이트를 GitHub Pages에 공개 발행한다. Claude Code 세션 로그를 자동 아카이브하고, 주기적 정제 루틴으로 개념 노트로 승격시킨다. 콘텐츠는 세션 교훈 + LLM 지식 전반(논문, 개념, 기법).

## 2. 확정된 결정

| 항목 | 결정 |
|---|---|
| 사용 형태 | Obsidian 편집 + Quartz 4 웹 퍼블리시 |
| 콘텐츠 범위 | Claude Code 세션 정제 + LLM 지식 전반 |
| 공개 범위 | 공개 사이트, 단 `publish: true` 노트만 선별 발행 |
| 호스팅 | GitHub Pages (GitHub Actions 자동 배포) |
| 프로젝트 루트 | `c:\Users\USER\Desktop\LLM_WIKI` (모노레포, git 하나) |
| 디자인 | 순정 네오 브루탈리즘 (시안 C-1, 소프트 버전과 비교 후 확정) |
| 자동화 | SessionEnd 훅 아카이브 + push 자동 배포 + /distill 커맨드 |

## 3. 저장소 구조

```
LLM_WIKI/                        ← git 루트
├── vault/                       ← Obsidian 볼트 (콘텐츠 전부)
│   ├── 00-Inbox/                # 미정제 메모. 주 1회 비움
│   ├── 10-Concepts/             # 핵심 위키. 개념 1 = 노트 1
│   ├── 20-Techniques/           # 재사용 레시피/패턴
│   ├── 30-Tools/                # Claude Code, vLLM 등 도구별 노트
│   ├── 40-Projects/             # 진행 중 프로젝트 노트
│   ├── 50-MOC/                  # 주제별 지도 노트 (사이트 홈 역할)
│   ├── 90-Archive/
│   │   └── claude-sessions/     # 세션 로그 md. 읽기 전용. 발행 금지
│   ├── 99-Meta/                 # 위키 사용법·가이드 (기존 files/ 문서 이동)
│   ├── _templates/              # Templater 템플릿
│   ├── .obsidian/               # 앱 설정 커밋 (플러그인 구성 재현용)
│   └── CLAUDE.md                # 볼트 규칙서
├── site/                        ← Quartz 4. vault/를 콘텐츠 소스로 빌드
├── scripts/                     ← Python 도구 (Windows 우선, 셸 의존 제거)
│   ├── cc2obsidian.py           # JSONL→md 변환 (기존 개선)
│   ├── archive_session.py       # SessionEnd 훅 진입점
│   └── secret_scan.py           # 비밀정보 스캔 (CI 게이트 겸용)
├── .claude/
│   ├── commands/distill.md      # 주간 정제 루틴 커맨드
│   └── settings.json            # SessionEnd 훅 등록
├── .github/workflows/deploy.yml # 스캔 → 빌드 → Pages 배포
├── docs/superpowers/specs/      # 설계 문서 (본 파일)
└── README.md
```

기존 `files/`는 재료로 흡수: 가이드 문서 → `vault/99-Meta/`, 스크립트 → `scripts/` 개선판. 흡수 후 `files/` 정리는 사용자 승인 후.

## 4. 데이터 흐름

```
Claude Code 세션 종료
  → SessionEnd 훅 (archive_session.py, Python — jq/xargs 의존 없음)
  → cc2obsidian 변환 → vault/90-Archive/claude-sessions/ (status: raw)
  → 주 1회 /distill: raw 분류 → 교훈 있는 것만 10-Concepts 승격 (status: distilled)
  → 공개할 노트에 publish: true
  → git push → Actions: secret_scan (HIGH 발견 시 실패) → Quartz 빌드 → Pages 배포
```

### 노트 라이프사이클

`status: raw`(자동 생성) → `triaged`(교훈 없음, 종료) 또는 `distilled`(개념 노트로 승격됨). 개념 노트는 `publish: true/false`로 발행 여부 제어. 기본값 미발행.

## 5. 발행 안전장치 (3중)

1. Quartz `ExplicitPublish` 필터 — `publish: true` 프로퍼티 노트만 사이트 포함. 기본 미발행.
2. `vault/90-Archive/`는 Quartz `ignorePatterns`로 원천 제외 (프로퍼티와 무관하게 차단).
3. CI 배포 전 `secret_scan.py` 실행 — API 키 패턴(sk-ant, Bearer, api_key 등) HIGH 매치 시 빌드 실패. 로컬 수동 실행도 지원.

## 6. 디자인: 순정 네오 브루탈리즘

시안 C-1 (`.superpowers/brainstorm/*/content/brutalist-compare.html` 좌측) 기준.

### 토큰

| 토큰 | 라이트 | 다크 |
|---|---|---|
| 배경 | `#f0efe9` | `#111111` |
| 잉크(텍스트/보더) | `#111111` | `#f0efe9` |
| 액센트 1 (라임) | `#d6ff3f` | `#d6ff3f` (유지) |
| 액센트 2 (바이올렛) | `#7c5cff` | `#9d85ff` |
| 보더 | `2px solid` 잉크색 | 동일 |
| 섀도 | `4px 4px 0` 잉크색 | `4px 4px 0 #d6ff3f` |

### 타이포

- 본문: **Pretendard Variable** (한글 최적화, self-host woff2)
- 제목: Pretendard 900, 대문자(영문), 자간 타이트
- 코드: **JetBrains Mono**
- 위키링크: 라임 하이라이트 박스 + 1px 잉크 보더

### 컴포넌트 (Quartz 커스텀 대상)

- 헤더: 잉크색 바탕 + 라임 로고 `█ LLM WIKI`
- 사이드바 탐색: 현재 섹션 라임 하이라이트
- 코드 블록·콜아웃·카드: 2px 보더 + 하드 섀도
- 태그: 바이올렛 배경 칩
- 그래프 뷰: 잉크 노드 + 라임/바이올렛 강조 노드
- 검색(⌘K), 백링크 패널, 목차: 동일 보더/섀도 문법 적용
- 다크모드 토글 유지. 다크는 보더·잉크 반전 + 라임 섀도로 정체성 유지

## 7. 도구 스택

| 역할 | 도구 | 비고 |
|---|---|---|
| 편집 | Obsidian + Dataview, Templater, Omnisearch | 플러그인 3개만. LLM 플러그인 금지(볼트에서 Claude Code 직접 실행이 대체) |
| 발행 | Quartz 4 + GitHub Pages | Node 18+. `npx quartz build -d ../vault` |
| 수집 | cc2obsidian.py | Windows 경로/인코딩(cp949 주의) 대응 개선 |
| 자동화 | Claude Code 훅 + 커맨드, GitHub Actions | 훅은 Python 호출로 셸 의존 제거 |
| 버전관리 | git 루트 하나 | `.superpowers/`, `site/public/` 등 gitignore |

## 8. /distill 커맨드 동작

1. `90-Archive`에서 `status: raw` 최근 10개 읽기
2. 교훈 유/무 분류표 제시 (파일 생성 금지 단계)
3. 무: `status: triaged`로만 변경
4. 유: 개념 노트 제목 후보 3개씩 제안 → 사용자 선택 대기 (제목은 사용자가 정함 — 자동화 함정 방지)
5. 선택된 것만 `10-Concepts/`에 템플릿 형식으로 생성, 원본에 `status: distilled` + 역링크
6. 한 번에 5개 초과 생성 금지

## 9. 구현 순서

- **Phase 1 — 볼트**: 스캐폴드, CLAUDE.md 규칙서, 템플릿, 시드 MOC, cc2obsidian 개선, dry-run → 기존 세션 import, 비밀정보 스캔
- **Phase 2 — 사이트**: Quartz 셋업, 브루탈리즘 테마 (토큰→SCSS, 컴포넌트 커스텀), 로컬 프리뷰로 사용자 확인, 폰트 self-host
- **Phase 3 — 자동화**: GitHub 저장소·Pages·Actions 배포 파이프라인, SessionEnd 훅, /distill 커맨드, README

각 Phase 끝에 사용자 확인 게이트.

## 10. 에러 처리·리스크

- **JSONL 포맷 비공식**: 방어적 파싱(모르는 필드 무시, 깨진 줄 스킵). 다수 실패 시 `/export` 우회 안내.
- **Windows**: 스크립트 전부 Python 3 표준 라이브러리, UTF-8 명시. bash 의존 제거. 경로는 `pathlib`.
- **세션 폭발**: import 시 `--since`/`--min-prompts` 필터 필수. 전량 import 금지.
- **비밀정보 유출**: 3중 안전장치(§5). `90-Archive/`는 git 포함하되 발행만 차단 — 단 스캔 HIGH 발견 시 커밋 전 사용자 보고.
- **훅 실패**: 아카이브 실패해도 세션 종료 블로킹 없음 (훅은 best-effort, 로그만 남김).
- **자동화 함정**: 개념 노트 제목은 항상 사용자가 확정 (§8).

## 11. 테스트 계획

- cc2obsidian: 실제 `~/.claude/projects` 대상 dry-run 출력 검증, 가짜 JSONL(깨진 줄 포함) 단위 테스트
- secret_scan: 가짜 API 키 심은 픽스처로 HIGH 검출·종료코드 검증
- 사이트: 로컬 `quartz build` + 프리뷰, `publish: true` 필터 동작 확인 (미발행 노트가 산출물에 없는지 grep)
- 배포: Actions 첫 실행 로그 확인, 스캔 게이트에 가짜 키로 실패 재현 후 제거
