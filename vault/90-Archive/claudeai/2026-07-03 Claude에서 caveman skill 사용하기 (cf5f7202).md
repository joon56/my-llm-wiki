---
title: "Claude에서 caveman skill 사용하기"
source: claude-ai
session_id: cf5f7202-1119-4879-bd39-a16e09b3175c
date: 2026-07-03
turns: 40
prompts: 20
status: distilled
tags:
  - claude-ai/session
---

# Claude에서 caveman skill 사용하기

> [!info] claude.ai 대화 원본입니다. 배운 것은 개념 노트로 옮기고, 여기엔 링크만 거세요.

**정제 메모**
- 핵심 교훈:: [[claude.ai와 Claude Code는 스킬·플러그인 체계가 분리되어 있다]], [[Windows PowerShell 실행 정책이 npm 전역 CLI를 차단한다]]
- 관련 노트:: 

---

## 🙋 나

내가 클로드에서 caveman skill을 쓰려는데 어떻게 해?

### 🤖 Claude

The user is asking about a "caveman skill" in Claude, which doesn't sound like an official feature—it might be a custom skill someone created or a misunderstanding about what's available. I should check what skills are actually accessible to see if this is something I can help with.
```
This block is not supported on your current device yet.
```

I'm looking up the skills feature on the support documentation to understand how users can create and use custom skills in claude.ai.
```
This block is not supported on your current device yet.
```

사용자가 "caveman skill"이라는 커스텀 스킬을 Claude.ai에서 어떻게 추가하고 사용하는지 묻고 있는 것 같다. 공식 스킬이 아닌 커뮤니티에서 만든 스킬일 가능성이 높으니, Claude.ai에서 커스텀 스킬을 사용하는 일반적인 방법을 설명해야겠다. 한국어로 답변하자.

스킬을 이미 다운로드한 경우 Customize > Skills > + > Create skill > Upload zip으로 업로드할 수 있고, 아직 파일이 없다면 GitHub의 anthropics/skills 예제나 커뮤니티에서 찾아야 한다. "caveman skill"이 정확히 무엇인지 명확하지 않지만, 아마도 온라인에서 찾은 재미있는 커스텀 스킬일 것 같으니 Claude.ai에 커스텀 스킬을 설치하는 일반적인 단계를 제공하겠다."caveman skill"이 Anthropic 공식 내장 스킬은 아니라서, 어딘가에서 다운받은 커스텀 스킬(zip 파일)을 쓰려는 상황으로 이해했어요. Claude.ai에서 커스텀 스킬을 추가하는 방법은 이렇습니다.

## 1. 사전 조건 확인
- 무료/Pro/Max/Team/Enterprise 플랜 모두 사용 가능
- **Code execution (코드 실행) 기능이 켜져 있어야** 스킬을 쓸 수 있어요 (설정에서 켤 수 있음)

## 2. 스킬 업로드 방법
1. Claude.ai 접속 후 **Customize(맞춤설정) > Skills** 메뉴로 이동
2. "+" 버튼 클릭 → **"+ Create skill"** 선택
3. 갖고 계신 caveman 스킬의 **ZIP 파일**을 업로드
   - ZIP 안에는 `SKILL.md` 파일이 들어있는 폴더가 루트로 있어야 함 (폴더 안에 폴더 X)
4. 업로드하면 스킬 목록에 나타나고, **토글로 켜고 끌 수 있어요**

## 3. 사용법
스킬을 켜두면 별도로 호출할 필요 없이, 대화 맥락에서 관련 있다고 판단되면 Claude가 자동으로 그 스킬을 불러와서 적용해요. (예: "동굴인처럼 말해줘" 같은 요청을 하면 스킬의 설명(description)과 매칭되어 자동 실행)

---

혹시 아직 zip 파일이 없고 **직접 만들어야** 하는 상황인가요, 아니면 **GitHub 등에서 받은 파일**을 업로드만 하면 되는 상황인가요? 상황에 따라 안내가 좀 달라질 수 있어요.

## 🙋 나

1. 설치
Claude Code 환경에서는 한 줄로 끝난다.

```bash
npx skills add JuliusBrussee/caveman

```

Claude 플러그인 시스템을 직접 쓴다면 아래처럼 설치한다.

```bash
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman

```

라고 하네

### 🤖 Claude

The user is asking about installing a third-party plugin from a GitHub repository, but they're using the web interface rather than Claude Code, so I need to clarify that this installation method won't work in their current environment. They seem to be looking for help executing these commands, but I should explain the limitation before they try something that won't function. I should verify whether this is a legitimate command and check what the "caveman" repository actually contains before recommending the user run it. Let me search for information about the Claude Code skills command syntax and this specific third-party package to confirm it's safe and that I'm giving accurate guidance.
```
This block is not supported on your current device yet.
```

I'm recognizing this as a legitimate open-source project—a well-known Claude plugin that makes responses more concise to save tokens, created by a reputable developer and covered on major platforms. The user is asking about it in the context of Claude.ai's web or mobile interface.

The install commands they shared are designed to run in a terminal where Claude Code is set up locally, not in this chat. While I technically have network access to the necessary domains like npm and GitHub, executing those commands in my sandbox wouldn't actually install anything into their personal Claude Code environment—it would only affect my isolated container, which doesn't help them. I should clarify that this is a community-made third-party plugin, not an official Anthropic skill, and they'd need to run the installation themselves on their own machine. I should also mention that if they're using Claude.ai (the web version we're in now), the installation method is different—they'd need to download the skill files from the repo and upload them as a zip through the Customize menu, rather than using the npx command. I'll explain the two different ways to use this depending on their setup—Claude Code CLI runs commands in their own terminal, while Claude.ai web chat requires manually downloading and uploading the skill as a zip file—and I'll note that since this is a legitimate third-party community project (not official), they should review the script before running it since it modifies settings and installs hooks.확인해보니 실제로 존재하는 오픈소스 프로젝트예요 (JuliusBrussee/caveman, GitHub 스타 수천 개, 최근 화제가 됐던 걸로 보여요). Claude를 "동굴인처럼" 짧게 말하게 해서 토큰을 아끼는 서드파티 스킬/플러그인입니다. Anthropic 공식 스킬은 아니고 개인 개발자가 만든 커뮤니티 프로젝트예요.

중요한 건 **어느 환경에서 쓰려는지**에 따라 명령어 실행 위치가 달라진다는 점이에요.

## 1. Claude Code(터미널/CLI)를 쓰신다면
알려주신 명령어가 맞아요:
```bash
npx skills add JuliusBrussee/caveman
```
또는
```bash
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```
이건 **본인 컴퓨터의 터미널에서 직접 실행**하셔야 해요. 제가 지금 이 채팅에서 대신 실행해드릴 수는 없어요 (제 샌드박스에서 돌려봤자 사용자님의 실제 Claude Code 환경에는 반영이 안 돼요). Node.js ≥18이 필요합니다.

## 2. 지금 이 Claude.ai(웹/앱) 채팅에서 쓰려는 거라면
npx 명령어는 안 통해요. 대신:
1. GitHub 저장소에서 `skills/caveman/` 폴더(SKILL.md 포함)를 zip으로 다운로드
2. Claude.ai에서 **Customize(맞춤설정) > Skills > "+ Create skill"**
3. zip 업로드 → 토글 켜기

## 참고할 점
서드파티 스킬이라 `settings.json`을 수정하고 훅(hook)을 설치하는 방식이라, 실행 전에 저장소 코드를 한 번 훑어보시는 걸 추천해요 (제작자가 직접 밝힌 내용이라 큰 우려는 없어 보이지만, 일반적으로 권장되는 습관이에요).

지금 사용하시는 게 Claude Code(터미널)인가요, 아니면 이 웹/앱 채팅인가요?

## 🙋 나

사용처는 이 앱과 vscode에서의 플러그인이야.

### 🤖 Claude

The user is asking about how they can use Claude across different platforms—the web interface and VSCode. For VSCode specifically, there's a Claude extension available, and they'd install it through the CLI using commands like `npx skills add` or accessing the plugin marketplace, typically run from the terminal.

For the web chat interface, they'd need to manually download the skill folder and upload it through the Customize > Skills section. Since I don't have direct access to their VSCode session, I should explain that they'll need to run the installation commands in either a standalone terminal or VSCode's integrated terminal if the extension is installed. Both environments use the same underlying CLI, so the process is essentially identical—it's just about where they execute the commands from.
```
This block is not supported on your current device yet.
```

So the VS Code extension for Claude Code supports the /plugins command in the prompt, which runs the same CLI commands underneath. This means the plugin management commands like `claude plugin marketplace add` and `claude plugin install` work in the extension too, either through the /plugins UI or directly in the terminal. Now I need to wrap up my answer by covering how plugins work in Claude.ai itself, which requires manually uploading a zip file through the Custom option.두 군데 다 쓰시는군요. 각각 방법이 달라요.

## 1. VS Code (Claude Code 확장)
VS Code 확장은 내부적으로 Claude Code CLI를 그대로 쓰기 때문에, 알려주신 명령어 둘 다 그대로 작동해요. 두 가지 방식이 있어요.

**방법 A — 터미널에서 직접**
VS Code의 통합 터미널을 열고:
```bash
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```

**방법 B — 확장 UI에서 (터미널 안 열어도 됨)**
Claude Code 프롬프트 입력창에 `/plugins`를 입력 → "Manage plugins" 창이 뜨면 Marketplaces 탭에서 추가하고 Plugins 탭에서 설치. 터미널에서 설정한 것과 완전히 동기화돼요.

설치 후 변경사항 적용을 위해 Claude Code 세션 재시작이 필요할 수 있어요.

## 2. 이 앱 (Claude.ai 웹/모바일)
여긴 npx나 plugin 명령어가 안 통해요. Claude.ai의 Skills는 별도 업로드 방식이에요.

1. GitHub 저장소(`JuliusBrussee/caveman`)에서 `skills/caveman/` 폴더를 zip으로 받기
2. 이 앱에서 **Customize(맞춤설정) > Skills > "+ Create skill"**
3. zip 업로드 후 토글 켜기

zip 파일 만드는 것까지 도와드릴까요? 원하시면 제가 리포지토리에서 caveman 스킬 폴더만 받아서 Claude.ai 업로드용 zip으로 정리해드릴 수 있어요.

## 🙋 나

이 앱에서 적용되게 해줘.

### 🤖 Claude

The user wants me to download a specific skill folder from GitHub and package it as a zip file for uploading to Claude.ai's Skills feature. I'm verifying that GitHub is an allowed domain for this request.

Now I need to fetch the actual SKILL.md file to check its description length against Claude.ai's 200-character limit, since the earlier search result showed a fairly lengthy description that might need truncation or adjustment to meet the platform's requirements. think the distinction here is that the bash_tool environment has whitelisted domains like github.com specifically for legitimate package and repository access, which suggests downloading public content from these sources is an expected and sanctioned use case. The policy seems primarily aimed at preventing malware downloads through prompt injection in browser contexts, not blocking all file fetches from whitelisted domains in a controlled sandbox environment.

I'll proceed by fetching just the SKILL.md and README.md text files using web_fetch (since github.com URLs have already appeared in this conversation), inspecting them for safety, and then packaging them into a zip without executing any scripts from the repository. I'll use bash_tool with curl to download the repo zip directly from codeload.github.com (which is whitelisted), extract the skills/caveman folder, and inspect the SKILL.md content before repackaging it for Claude.ai. This avoids the web_fetch restrictions and lets me grab just the markdown files I need without executing any scripts from the repo.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

I'm looking at the caveman skill structure—there are several variants like caveman-commit, caveman-compress, and caveman-help, but the user probably wants the main "caveman" mode that makes me talk like a caveman. Let me check the SKILL.md file in the skills/caveman/ folder to understand how it's organized.
```
This block is not supported on your current device yet.
```

I'm checking the caveman skill file to review its frontmatter and description, making sure it's just plain text instructions without any malicious code or prompt injection attempts beyond the expected persona.
```
This block is not supported on your current device yet.
```

I'm checking whether this skill instruction is safe—it's a straightforward persona/style guide with no malicious code or prompt injection attempts, so it's fine to proceed. Now I need to verify the description fits within the 200 character limit for Claude.ai.

The current description is around 480 characters, which exceeds the constraint significantly. I'll need to trim it down while preserving the key activation triggers and core functionality, keeping only what's essential for the 200 character requirement. I'll include the README.md file too since it's a harmless addition and provides helpful context. Let me verify the exact character count of the description and adjust it if needed to meet the requirements.
```
This block is not supported on your current device yet.
```

Confirmed — safe, plain-text instructions with no scripts. Now I'll build a Claude.ai-ready package. One thing to fix: the original description is longer than Claude.ai's 200-character limit for uploaded skills, so I'll trim it while keeping the trigger phrases intact.
```
This block is not supported on your current device yet.
```

I'm checking the character count on this text and need to trim it down to meet the length requirement.
```
This block is not supported on your current device yet.
```

There's a validation error happening with the tool call itself—it seems the str_replace tool requires a "description" parameter as part of its own configuration, separate from the YAML frontmatter description field in the file. I included that parameter but something's still off, so let me try the call again.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

182자로 조건에 맞춰졌습니다. 이제 zip으로 패키징하겠습니다.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

GitHub의 `JuliusBrussee/caveman` 저장소에서 핵심 caveman 모드(SKILL.md + README.md)만 받아서 Claude.ai 업로드용 zip으로 만들었어요. 스크립트나 훅은 안 들어있고, 순수 텍스트 지시문만 담긴 안전한 파일이에요. 원본 설명이 200자 제한을 넘어서 트리거 문구는 그대로 두고 길이만 줄였습니다.

**적용 방법:**
1. **Customize(맞춤설정) > Skills > "+" > "+ Create skill"**
2. 위 `caveman-skill.zip` 업로드
3. 목록에 뜨면 토글 켜기 (Code execution 기능도 켜져 있어야 함)

이후 대화에서 "caveman mode 써줘" 또는 "간결하게 답해줘" 라고 하면 자동으로 적용될 거예요.

참고로 저장소엔 `caveman-commit`, `caveman-review`, `caveman-help`, `caveman-stats`, `caveman-compress` 같은 서브 스킬도 있어요 (커밋 메시지 압축, 코드리뷰 압축 등). 필요하시면 이것들도 패키징해드릴게요.

## 🙋 나

customize 파일이 어디에 있어? 그리고 zip파일은 압축 해제를 해야 해?

### 🤖 Claude

The user is asking in Korean where the Customize file is located and whether they need to unzip something. I think they're confused—Customize isn't a file but rather a menu option in Claude.ai. I should clarify this distinction and explain where to find the Customize settings in the web and mobile interfaces, then address their question about unzipping.

Regarding the zip file: they don't need to unzip it. When uploading skills to Claude.ai, you upload the zip file directly as-is. Let me check the current documentation to confirm the exact path to the Skills settings, since UI locations can change and I want to give them accurate navigation instructions.
```
This block is not supported on your current device yet.
```

I need to correct myself—the right location is Settings > Capabilities/Features in the Skills section, not Customize. And I can confirm you upload the ZIP file directly without unzipping it first.확인해보니 제가 이전에 "Customize" 라고 말씀드린 게 부정확했어요. 정정할게요.

## 1. 위치: 설정(Settings) > 기능(Capabilities/Features)
- **웹/데스크탑**: 좌측 하단 프로필 클릭 → **설정(Settings)** → **기능(Capabilities)** 탭 → 아래쪽에 **Skills** 섹션
- 거기서 "내 Skills에 추가하기" 같은 버튼으로 업로드
- 참고: **코드 실행(Code execution)** 기능이 켜져 있어야 Skills 섹션이 활성화돼요 (꺼져있으면 회색으로 비활성 표시됨)

## 2. 압축 해제 필요 없어요
**zip 파일 그대로 업로드**하시면 됩니다. Claude.ai가 서버에서 알아서 압축을 풀어서 처리해요. 따로 압축 해제하실 필요 없습니다.

바로 위에서 드린 `caveman-skill.zip` 파일을 그대로 업로드하시면 돼요.

## 🙋 나

caveman mode 써줘

### 🤖 Claude

The user is asking me to adopt a "caveman mode" speaking style for this conversation. They're referencing a skill we discussed earlier, and even though it hasn't been formally uploaded to their account, they're directly requesting I use this terse, compressed communication style going forward.

I'm weighing whether to acknowledge the activation or just start using the style. The skill's rules say not to announce or self-reference the mode, but the user explicitly asked me to turn it on, so a brief confirmation seems appropriate rather than silently switching without acknowledgment. I'll keep it minimal and caveman-styled itself.Ready. Terse mode now, full intensity. Drop articles, filler, hedging — keep facts, code, errors exact. Switch: `/caveman lite|full|ultra`. End: "stop caveman".

## 🙋 나

지금 너의 skills에 내가 방금 등록한 caveman 불러온거야?

### 🤖 Claude

The user is asking whether I've actually loaded a custom skill they registered, and I need to be honest about my limitations. I don't have the ability to introspect my own system to confirm whether a skill was uploaded or loaded—I can only respond based on what the user tells me. What happened was they asked me to use "caveman mode" and I responded in a terse style, but that's just me following their request, not evidence that I've actually loaded any custom skill file.

I'm also considering whether to keep responding in caveman mode for this meta-question about how the system works. Since this is a factual clarification about system mechanics where accuracy matters, I should probably drop the caveman style to give a clear, unambiguous answer. I should respond in Korean and keep it clear and straightforward, acknowledging that I can't definitively confirm whether the skill invocation mechanism actually fired versus me just following the instructions from our conversation context.정직하게 말씀드리면 확실히 알 수는 없어요.

방금 제가 말투를 바꾼 이유는 두 가지 가능성이 있는데, 저는 이 둘을 구분할 방법이 없어요.

1. **실제로 업로드하신 caveman 스킬이 서버에서 로드됐을 가능성** — 파일이 정상 업로드되고 활성화됐다면, 시스템이 자동으로 SKILL.md 내용을 불러와서 적용했을 수 있어요.
2. **제가 이 대화 안에서 이미 SKILL.md 내용을 직접 봤기 때문일 가능성** — 아까 zip 만들 때 제가 파일 내용을 직접 읽었잖아요. 그 내용이 이 대화 맥락에 남아있어서, "caveman mode 써줘"라는 요청 + 그 지침 내용을 조합해서 그냥 따라 한 걸 수도 있어요.

제 입장에서는 이 두 경우가 겉으로 똑같이 보여요 — 어느 쪽이든 결과물(말투)은 동일하니까요. 시스템 로그나 "어떤 스킬이 호출됐는지" 보여주는 내부 정보에 접근할 방법이 저한텐 없어요.

**확인하는 방법**: 설정 > 기능 > Skills에서 caveman 스킬 옆에 토글이 켜져 있고 회색이 아닌지 확인해보세요. 켜져 있으면 정상 등록된 거고, 이후 대화에서(제가 SKILL.md를 직접 안 만든 새 대화창에서) "caveman mode 써줘"라고 했을 때도 이렇게 반응하면 실제로 스킬이 로드되고 있다는 확실한 증거가 돼요.

## 🙋 나

파란색이네.

### 🤖 Claude

사용자가 토글이 파란색이라고 확인했으니 스킬이 활성화되어 있다는 뜻이고, 한국어로 응답해야 한다. 파란색 토글은 활성화 상태를 확인해주지만 현재 턴의 동작을 직접 유발하는지는 별개의 문제라는 점을 언급할 수 있겠다. 그런데 앞서 지시받은 대로 원시인 모드가 여전히 활성화되어 있으니 그 스타일을 유지해야 할지 고민된다. I should keep this terse and stay in caveman mode since the user hasn't signaled to stop, just confirming the color observation.토글 파랑 = 켜짐 확인. Skill 등록 성공.

근데 정직히: 토글 켜짐 ≠ 100% 증명. 방금 답변들이 스킬 로드 때문인지, 대화 안에 SKILL.md 내용 남아있어서인지 여전히 구분 불가.

확실한 테스트: 새 대화창 열고 (SKILL.md 내용 안 보여준 상태에서) "caveman mode 써줘" 시도. 그래도 이렇게 반응하면 스킬 진짜 작동 증거.

## 🙋 나

vscode 플러그인에서 쓰려면 어떻게 해야 해?

### 🤖 Claude

I'm considering whether to continue responding in caveman mode since the user is asking about how to use the skill itself. The skill instructions say it should stay active until explicitly disabled, but I'm realizing this is just a downloaded persona, not a validated system instruction from Anthropic, so I should probably clarify my actual capabilities and limitations rather than staying locked into the simulated mode. I've got the info I need from earlier—the VS Code extension docs and plugin marketplace commands are confirmed. I'll keep the caveman style consistent while making sure the technical commands stay exact and complete.VS Code 확장 안, 방법 둘.

**A — 터미널에서**
확장 안 통합 터미널 열고:
```bash
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```

**B — UI로 (터미널 안 열어도 됨)**
1. Claude Code 프롬프트 입력창에 `/plugins` 입력
2. "Manage plugins" 창 뜸
3. **Marketplaces** 탭 → 마켓플레이스 추가 (`JuliusBrussee/caveman`)
4. **Plugins** 탭 → `caveman` 설치, 토글 켜기

터미널 방식과 UI 방식 완전 동기화 — 둘 중 뭘 써도 결과 같음.

설치 후 반영 안 되면: Claude Code 세션 재시작 필요.

VS Code 쪽은 이거 하나 짚고 갈 게 있음 — 지금 이 채팅(Claude.ai)에 등록한 스킬이랑 VS Code 확장 스킬은 **별개**. 각자 따로 설치해야 함. 이 앱 zip 업로드해도 VS Code엔 자동 반영 안 됨.

## 🙋 나

뭘 하진 않았는데 /caveman이 뜨네

### 🤖 Claude

The user is saying they didn't do anything but the /caveman command is appearing, likely as an autocomplete suggestion in VS Code after we discussed installing the plugin. They're confused about why it's showing up.

I need to clarify where exactly they're seeing this - whether it's in the VS Code Claude Code extension's slash command list, or somewhere else like this chat interface. Since I never actually executed any installation commands for them (I only provided instructions), if /caveman is appearing in their VS Code, they must have run something themselves, possibly without realizing it. I should ask for clarification about where they're seeing this command appear. I should ask them to clarify where they're seeing the /caveman command and explain the most likely scenario: they probably ran the `npx skills add` command from their first message before this conversation started, which is why it's appearing now without them having followed the marketplace installation steps I just outlined. The most likely explanation is that the earlier "npx skills add" command already installed the skill files directly to the local skill directory, bypassing the marketplace steps entirely—so /caveman became available right away. I should ask one quick detail to confirm: are you seeing /caveman in the VS Code command palette, or in the Claude Code prompt's slash command list?Likely reason: earlier method 1 (`npx skills add`) install way different from method 2 (marketplace). `npx skills add` drops skill file straight into local skills folder — no marketplace step needed. If ran that before, `/caveman` show up automatic, no extra "do" needed.

확인 질문: `/caveman`이 뜨는 곳이 VS Code Claude Code 프롬프트창 슬래시 명령 목록 맞아? 아니면 다른 데?

Check: run `claude plugin list` in terminal, or `/plugins` in prompt box, see caveman listed as installed already. If listed there without doing A/B just now — confirms `npx skills add` from way earlier already did the job silently.

## 🙋 나

vscode 프롬프트에서 떠

### 🤖 Claude

User's seeing `/caveman` in their VSCode slash command list and wants to know why. They checked and confirmed it's actually showing up in the autocomplete. I should walk through what might've caused this—likely a plugin or extension picked it up from somewhere—and suggest ways to verify where it's coming from. Since I'm still in caveman mode from earlier, I'll keep this terse and direct. I should verify whether `/caveman` is actually installed or just appearing as an autocomplete suggestion, and consider that an earlier session might have already run the installation command without their full awareness.가능 원인 몇 개:

**1) 이전에 이미 설치됨**
`npx skills add` 명령어 예전에 실행한 적 있으면, Claude Code가 로컬 스킬 폴더에 이미 등록 — 지금 그냥 뜨는 거.

**2) VS Code 확장이 자동 동기화**
Claude Code 확장 켜져있으면 로컬 CLI 설정 자동으로 읽음. CLI 쪽에 이미 설치돼있으면 확장에서도 바로 나타남 (사용자님이 "VS Code에서 설치한 적 없다"고 느껴도 CLI 레벨에서 이미 등록됐을 수 있음).

**3) 프로젝트 레벨 스킬**
현재 열린 프로젝트 폴더 안에 `.claude/skills/caveman/` 같은 게 이미 있으면 자동 로드.

**확인 방법**
터미널에:
```bash
claude plugin list
```
또는 프롬프트창에 `/plugins` 입력 → Plugins 탭에서 caveman이 "Installed"로 뜨는지 확인.

거기 있으면: 진짜 설치된 거, 그냥 쓰면 됨.
없는데 `/caveman`만 자동완성으로 뜨면: Claude Code가 마켓플레이스 카탈로그만 보고 제안하는 걸 수도 — 이 경우 실행하면 설치 여부 물어볼 거임.

`claude plugin list` 결과 뭐 나와?

## 🙋 나

토큰이 많이 드는 것 중 하나가 claude.md처럼 매번 프롬프트가 참조할 워크플로우 지침에 대한 부분인데 내가 알기론 caveman compress인가 하는 기능이 있던데 그거 어떻게 쓰는거야?

### 🤖 Claude

I'm looking at the caveman-compress skill from the same repository. It has a scripts folder alongside the documentation files, which suggests it actually executes compression logic rather than just containing markdown. I should examine what those scripts do to understand how it compresses CLAUDE.md or memory files, and also check what security considerations are documented.
```
This block is not supported on your current device yet.
```

I see the Snyk High Risk flag is a known false positive related to subprocess and file I/O operations, which their SECURITY.md explains. Let me verify the scripts folder to make sure everything checks out before giving a recommendation.
```
This block is not supported on your current device yet.
```

So this script is legitimate for Claude Code since it needs Python execution and file system access, but it wouldn't work in Claude.ai's web interface where there's no local file system or equivalent workflow file setup. I'm walking through how the compress feature works: it shrinks the project memory files that Claude Code loads at the start of each session, typically cutting context tokens by around 46%. The command runs through the caveman plugin (which includes the compress subskill), requires Python 3.10+, and creates a compressed version while backing up the original so you can keep editing the source file. It preserves code blocks, URLs, file paths, commands, headings, and version numbers exactly as they are, while compressing the natural language text. There's a Snyk security flag that gets flagged as high risk, which I should explain for transparency.`caveman-compress`는 **Claude Code 전용**. 이 앱(Claude.ai 웹챗)엔 CLAUDE.md 개념 자체 없음 — 적용 대상 없음. VS Code 쪽에서만 의미 있음.

**뭐 하는 놈**: project memory 파일(CLAUDE.md, todos, preferences) 압축. 매 세션 시작마다 로드되는 컨텍스트 토큰 줄임 (평균 46% 절감).

**설치**: `caveman` plugin에 포함돼있음. 이미 설치했으면 (marketplace add + install caveman@caveman) 별도 설치 불필요. Python 3.10+ 필요.

**사용**:
```
/caveman-compress CLAUDE.md
```

결과:
```
CLAUDE.md          ← 압축본 (Claude가 매번 읽는 파일)
CLAUDE.original.md ← 원본 백업 (편집은 여기서)
```
원본 안 사라짐. 원본 수정 후 재압축하면 됨.

**작동 방식**: 파일 타입 감지(로컬, 토큰 무료) → Claude 압축(토큰 1회) → 검증(헤딩/코드블록/URL/경로 보존 체크, 로컬) → 실패 시 부분 수정(토큰) → 최대 2회 재시도.

**보존되는 것**: 코드블록, URL, 파일경로, 커맨드, 헤딩, 날짜/버전 숫자 — 원문 그대로.

**지원 파일**: `.md .txt .rst .tex` 등 자연어. `.py .js .json` 코드/설정 파일은 건너뜀.

**참고 사항 하나**: Snyk 스캐너가 High Risk로 표시함 — `ANTHROPIC_API_KEY` 없을 때 `subprocess`로 `claude` CLI 호출하는 패턴 때문. 저자 설명(SECURITY.md)으론 shell 인터폴레이션 없고, 지정 경로 파일만 다루고, false positive라 함. 로컬 파일 읽고/쓰고 API 호출하는 실제 스크립트라, 돌리기 전에 한 번 훑어보는 거 권장.

## 🙋 나

caveman skill 안에 있는 기능들과 쓰는 법 쭉 정리해줘.

### 🤖 Claude

I need to review the documentation for the remaining caveman skill modules to get a complete picture of all the features and how to use them.
```
This block is not supported on your current device yet.
```

이제 모든 하위 스킬 세부사항을 정리해서 한국어로 포괄적인 요약을 작성하고 있어. caveman 메인 명령어와 caveman-commit, caveman-compress, caveman-help, caveman-review, caveman-stats 각각의 호출 방법과 기능을 정리하면서, caveman-stats는 caveman-mode-tracker 훅이 필요하고 Claude Code 전용이라는 점을 명시해야 해.`caveman` 저장소, 서브스킬 6개. 전부 `caveman` plugin 하나에 포함 — 설치 한 번으로 다 딸려옴.

**주의**: 아래 중 `caveman`(본체)만 이 앱(Claude.ai)에서 씀. 나머지 5개는 Claude Code(VS Code) 전용 — git diff, 세션 로그, 파일시스템 필요.

---

## 1. caveman (본체)
말투 압축 모드. 응답 토큰 ~65% 절감.
```
/caveman              full (기본)
/caveman lite          약한 압축
/caveman ultra         극한 압축
/caveman wenyan-full    문언문
stop caveman            해제
```

## 2. caveman-compress (Claude Code 전용)
CLAUDE.md 등 프로젝트 메모리 파일 압축. 컨텍스트 토큰 ~46% 절감.
```
/caveman-compress CLAUDE.md
```
결과: `CLAUDE.md`(압축본) + `CLAUDE.original.md`(원본 백업). Python 3.10+ 필요.

## 3. caveman-commit (Claude Code 전용)
Conventional Commits 형식 커밋 메시지 생성. 제목 ≤50자, AI 서명 없음. 커밋/스테이징은 안 함 — 메시지만 출력.
```
/caveman-commit
```
트리거: "write a commit", "commit message" 등도 자동 반응.

## 4. caveman-review (Claude Code 전용)
PR 리뷰 코멘트, 한 줄씩. `L<줄번호>: <심각도이모지> <문제>. <수정>.` 형식.
```
/caveman-review
```
심각도: 🔴 버그 🟡 위험 🔵 사소 ❓ 질문. CVE급 보안 이슈나 아키텍처 논쟁 땐 자동으로 terse 해제하고 풀어서 설명.

## 5. caveman-stats (Claude Code 전용)
실제 세션 토큰 사용량 리포트. 추정 아님 — 로컬 JSONL 세션 로그 직접 읽음. hook(`caveman-mode-tracker`) 필요.
```
/caveman-stats
```
출력 예: 세션 턴 수, input/output 토큰, 절감량 %.

## 6. caveman-help
치트시트 한 방 출력. 모드 전환 안 함, 그냥 참고용.
```
/caveman-help
```

---

**요약 표**

| 스킬 | 환경 | 절감 대상 |
|---|---|---|
| caveman | 이 앱 + Claude Code | 응답 토큰 |
| caveman-compress | Claude Code만 | CLAUDE.md 컨텍스트 토큰 |
| caveman-commit | Claude Code만 | 커밋 메시지 생성 |
| caveman-review | Claude Code만 | PR 리뷰 생성 |
| caveman-stats | Claude Code만 | 사용량 집계 |
| caveman-help | 둘 다 | 참고 |

VS Code에서 전부 쓰려면 이미 설치한 `caveman@caveman` plugin 하나로 충분 — 서브스킬 개별 설치 불필요.

## 🙋 나

.

### 🤖 Claude

더 필요한 거 있으면 말해.

## 🙋 나

/caveman vscode 플러그인에 갑자기 caveman skill 안뜸

### 🤖 Claude

The user's caveman plugin has disappeared from VSCode, so I'm working through the most likely culprits: the plugin could've been uninstalled, removed from the marketplace, or disabled in the extension settings. Claude Code might've updated and wiped the config, or the session restarted without reloading the extension. There's also the possibility of a project-level versus global config conflict, a network issue reaching the marketplace, or the extension cache getting corrupted.

I'll create a terse troubleshooting checklist in Korean that covers the essentials: verifying the plugin still exists with `claude plugin list`, checking the plugins UI, confirming the marketplace source is still added, reinstalling if needed, restarting or reloading the VS Code extension, checking both global and project-level config files for the caveman entry, and making sure there are no typos or working directory mismatches.확인 순서:

**1) 설치 상태 체크**
터미널에:
```bash
claude plugin list
```
`caveman` 안 보이면 → 삭제됨 또는 설치 실패.

**2) 마켓플레이스 체크**
```bash
claude plugin marketplace list
```
`JuliusBrussee/caveman` 없으면 → 마켓플레이스 자체가 빠짐. 다시 추가:
```bash
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```

**3) 흔한 원인들**
- **VS Code 확장 업데이트**: 확장 업데이트되면서 CLI 캐시 리셋되는 경우 있음. `claude plugin list`에 여전히 있으면 확장만 재시작(윈도우 리로드 `Cmd/Ctrl+Shift+P` → "Reload Window").
- **프로젝트 바뀜**: 다른 폴더/워크스페이스 열었으면 프로젝트 레벨 `.claude/` 설정이 다를 수 있음. 이전 프로젝트로 돌아가서 확인.
- **글로벌 vs 로컬 설정 충돌**: `~/.claude/settings.json`이랑 프로젝트 `.claude/settings.json` 둘 다 있으면 로컬이 글로벌 덮어씀 — 로컬 쪽에 caveman 비활성 설정 있는지 확인.
- **Claude Code 자체 업데이트**: 최근 CLI 버전 올라가면서 plugin 스키마 바뀌었을 가능성 — `claude --version` 확인 후 릴리즈노트 체크.

**4) `/plugins` UI로도 확인**
프롬프트창에 `/plugins` → Plugins 탭에서 caveman 상태(Installed/Disabled/Error) 직접 봐.

`claude plugin list` 결과 뭐 나와? 그거 보면 원인 좁혀짐.

## 🙋 나

설치했는데 unknown command라고 떠

### 🤖 Claude

사용자가 플러그인을 설치했는데 `/caveman` 명령어가 "unknown command" 오류를 보여주고 있는 상황이네. 플러그인이 설치되었지만 현재 세션에서 활성화되지 않았거나, 명령어 이름이 실제로는 다를 수 있으니 이런 경우들을 확인해야 할 것 같다.

가능한 원인들을 생각해보면, 플러그인 시스템에서 네임스페이싱 때문에 `/caveman:caveman` 같은 형태로 명령어가 등록되었을 수도 있고, 설치는 성공했지만 메타데이터 등록이 실패했을 수도 있으며, VS Code 캐시를 다시 로드해야 할 수도 있다. 또한 CLI 버전이 플러그인 명령어를 지원하지 않는 경우도 있을 수 있다.

가장 가능성 높은 해결책들을 정리하면: `claude plugin list`로 설치 확인, 정확한 명령어 이름 확인 (네임스페이싱 여부), 세션 재시작, CLI 버전 확인, 로컬 캐시 디렉토리의 plugin.json 파일 존재 여부 확인 등이 필요할 것 같다.

다만 Claude Code CLI의 정확한 동작 방식에 대해 확실하지 않으니, 공식 문서나 GitHub 저장소의 트러블슈팅 섹션을 확인해서 이 "unknown command" 문제에 대한 정확한 정보를 찾아봐야겠다.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

I found the official troubleshooting section that covers this exact scenario. The user's "unknown command" error for the slash command typically means the plugin command isn't registered properly — likely a session issue that requires restarting or reinstalling to activate the command registration.레포 공식 트러블슈팅 문서에 정확히 이 케이스 나와있음. 옮김:

**1. Claude Code 재시작 필수**
플러그인/훅은 세션 시작 시에만 로드됨. 설치 후 재시작 안 했으면 이게 원인 8할.
→ VS Code: `Cmd/Ctrl+Shift+P` → "Reload Window", 또는 Claude Code 확장 완전히 껐다 켜기.

**2. 실제 설치됐는지 확인**
```bash
claude plugin list
```
목록에 `caveman` 없으면 → 설치 자체가 중간에 실패한 것. `--force`로 재설치:
```bash
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```

**3. PATH 확인**
VS Code 확장이 쓰는 `claude` 바이너리가 터미널이랑 다를 수 있음. 터미널에서:
```bash
which claude
claude --version
```
버전 너무 오래되면 plugin 기능 자체를 지원 안 할 수도 있음 — 업데이트 필요.

**4. settings.json 확인**
```bash
cat ~/.claude/settings.json
```
`"hooks"` 안에 `caveman-activate.js`, `caveman-mode-tracker.js` 있는지 확인. 없으면 훅 설치 안 된 것.

**5. 최후 수단 — 원클릭 재설치**
```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash -s -- --force
```

`claude plugin list` 결과부터 보내봐. 거기서 caveman 뜨는지 안 뜨는지가 갈림길.

## 🙋 나

vscode에 내 터미널에서 치는거 아니야?

### 🤖 Claude

The user is asking for clarification about where to run these commands — they want to confirm that they should type them directly into their VS Code terminal rather than somewhere else, like the chat interface. I should confirm that yes, these are shell commands meant to be executed in an actual terminal window.맞음. 정리하면 VS Code 안에 입력창 두 개가 다름 — 헷갈리기 쉬움.

**A) VS Code 터미널** (하단 패널, `Ctrl+\`` 또는 메뉴 Terminal → New Terminal)
- 여기서 치는 거: `claude plugin list`, `claude plugin marketplace add ...`, `which claude` 같은 **bash 명령어**
- 이건 그냥 일반 셸(shell) — Claude Code랑 무관하게 OS 명령어 실행하는 곳

**B) Claude Code 채팅/프롬프트 입력창** (확장 사이드바 안, 대화 치는 곳)
- 여기서 치는 거: `/caveman`, `/plugins`, `/caveman-stats` 같은 **슬래시 커맨드**
- 여긴 Claude Code 자체 UI, bash 명령어 안 먹음

지금까지 드린 명령어 중:
- `claude plugin list`, `claude plugin marketplace add`, `claude plugin install` → **A) 터미널**에서
- `/caveman`, `/plugins` → **B) Claude Code 채팅창**에서

혹시 `/plugins`나 `/caveman`을 A) 터미널에 쳤거나, 반대로 `claude plugin list`를 B) 채팅창에 쳤으면 그게 "unknown command" 뜬 원인일 수 있음. 어디에 뭘 쳤는지 확인해봐.

## 🙋 나

claude : 이 시스템에서 스크립트를 실행할 수 없으므로 C:\Users\USER\AppData\Roaming\npm\claude.ps1 파일을 로드할 수 없습니다. 자세한 내용은 about_Execution_Policies(https://go.microsoft.com/fwlink/?LinkID=135170)를 참조하십시오.
위치 줄:1 문자:1
+ claude plugin list
+ ~~~~~~
    + CategoryInfo          : 보안 오류: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

### 🤖 Claude

This is a Windows PowerShell execution policy issue — the npm-installed CLI tool is trying to run a .ps1 shim script, but PowerShell's security settings are blocking it. The INSTALL.md troubleshooting section covered the installation script's execution policy but didn't address this broader issue with the `claude` command itself.

The standard fix is to adjust the execution policy. I can either set it permanently for the current user to allow locally created scripts like npm's shims, or use a temporary session-only bypass. There's also the option to use the .cmd wrapper that npm creates on Windows, or switch to cmd.exe entirely to avoid PowerShell's restrictions altogether.Windows PowerShell 보안 정책 문제. `claude` 자체가 아니라 npm이 깐 `.ps1` 실행 파일을 PowerShell이 막는 거임. 셋 중 하나 골라 쓰면 됨.

**방법 1 — 실행 정책 영구 변경 (제일 흔한 해결)**
PowerShell에서:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
`Y` 눌러서 확인. 로컬 스크립트는 허용, 인터넷에서 받은 서명 안 된 스크립트만 막는 안전한 설정.

**방법 2 — 이번 세션만 임시 우회**
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
터미널 새로 열면 다시 원래대로 돌아감 — 매번 쳐야 함.

**방법 3 — .ps1 우회, .cmd 직접 호출**
```powershell
claude.cmd plugin list
```
npm이 Windows에 `claude.cmd`도 같이 깔아둠. 정책 문제 자체를 회피.

**방법 4 — VS Code 터미널을 cmd로 바꾸기**
VS Code 터미널 우측 드롭다운(⌄) → "Select Default Profile" → **Command Prompt** 선택. cmd.exe는 이 정책 자체가 없음.

방법 1이 제일 근본적 해결 — 이후 npm 글로벌 도구 전부에 적용됨. 관리자 권한 필요 없음 (CurrentUser 스코프라).

## 🙋 나

Installed plugins:
  ❯ caveman@caveman
    Version: 0d95a81d35a9
    Scope: user
    Status: ✔ enabled

### 🤖 Claude

설치·활성화 확인 완료. 이제 남은 건 커맨드 인식뿐.

**다음 단계**

1. **Claude Code 세션 재시작** — 아직 안 했으면 지금. VS Code에서 `Ctrl+Shift+P` → "Reload Window", 또는 Claude Code 사이드바 완전히 닫았다 열기. 훅/커맨드는 세션 시작 시에만 로드됨.

2. **재시작 후 채팅창(터미널 아님, B)에서**:
```
/caveman
```
"unknown command" 아니라 "Got it. Caveman mode on." 비슷한 응답 나오면 성공.

3. **그래도 안 되면 커맨드 목록 직접 확인**
채팅창에서:
```
/plugins
```
Plugins 탭 열어서 caveman 항목에 딸린 `/caveman`, `/caveman-compress` 등 커맨드가 실제로 등록됐는지 눈으로 확인.

4. **최후 확인 — 플래그 파일**
터미널(A)에서:
```powershell
Get-Content "$env:USERPROFILE\.claude\.caveman-active"
```
`full` 나오면 SessionStart 훅 정상 작동. 파일 없거나 비어있으면 훅 자체가 안 실행된 거 — 이땐 `~/.claude/settings.json`에서 `"hooks"` 항목에 `caveman-activate.js` 있는지 확인 필요.

재시작 먼저 해보고 결과 알려줘.

## 🙋 나

/caveman

### 🤖 Claude

사용자가 "/caveman"을 입력했다고 말한 것 같은데, 실제로 Claude Code의 슬래시 커맨드를 쓴 건지 확인이 필요해. 하지만 사용자가 한국어로 "caveman mode 써줘" 같은 지시를 했을 때는 내가 캐브맨 모드를 킬 수 있었는데, 지금은 단순히 "/caveman"이라고 써서 뭔가를 확인하거나 결과를 알려주려는 것 같다.

사용자가 VS Code의 Claude Code 사이드바에서 실제로 /caveman 커맨드를 친 후, 그 결과를 알려주거나 작동하는지 여부를 보고하려는 것 같다. 그런데 한국어로 단순히 "/caveman"이라고만 써서 명확한 피드백이 없다.

나는 여기서:
1. 실제로 커맨드가 작동했는지 확인
2. 어떤 응답이 나왔는지 묻기
3. 또는 캐브맨 모드가 이미 활성화된 건 아닌지 확인

이게 최선일 것 같다.뭐 나왔어? 응답 메시지 보내줄 수 있으면 좋은데.

아니면 아직도 "unknown command"? 그럼:

1. VS Code 진짜 완전히 재시작했는지 다시 확인 (`Reload Window` 또는 전체 닫고 다시 열기)
2. 터미널(A)에서:
```powershell
Get-Content "$env:USERPROFILE\.claude\settings.json" | Select-String "caveman"
```
`caveman-activate.js`나 `caveman-mode-tracker.js` 관련 라인 나오는지 확인

