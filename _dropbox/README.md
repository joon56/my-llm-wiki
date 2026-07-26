# _dropbox — claude.ai 대화 반입함

데스크톱 앱/웹(claude.ai) 대화를 위키로 가져오는 임시 투입구.

## 사용법

1. claude.ai → 설정 → 개인정보 → **데이터 내보내기** → 이메일로 받은 zip을 **이 폴더에 넣는다** (zip 그대로 또는 압축 푼 `conversations.json`)
2. Claude Code에서 `/ingest` 실행
3. 변환 결과 확인 후 이 폴더는 자동으로 비워진다 (성공분만 삭제)

- 이 폴더 내용물은 git에 올라가지 않는다 (원본 export 보호)
- 같은 대화가 다음 export에 또 있어도 UUID로 중복 제거되므로 그냥 통째로 넣으면 됨
- 변환 결과: `vault/90-Archive/claudeai/` (`status: raw`) → 이후 `/distill` 대상
