import json
import tempfile
import unittest
from pathlib import Path

from claudeai2obsidian import convert

SAMPLE = [
    {
        "uuid": "aaaa1111-2222-3333-4444-555566667777",
        "name": "RAG 파이프라인 질문",
        "created_at": "2026-07-20T10:00:00Z",
        "chat_messages": [
            {"sender": "human", "text": "임베딩 모델 어떻게 골라?", "created_at": "2026-07-20T10:00:00Z"},
            {"sender": "assistant", "text": "용도에 따라 다릅니다.", "created_at": "2026-07-20T10:00:05Z"},
            {"sender": "human", "text": "한국어 기준으로.", "created_at": "2026-07-20T10:01:00Z"},
        ],
    },
    {
        "uuid": "bbbb1111-2222-3333-4444-555566667777",
        "name": "짧은 인사",
        "created_at": "2026-07-21T10:00:00Z",
        "chat_messages": [
            {"sender": "human", "text": "안녕", "created_at": "2026-07-21T10:00:00Z"},
        ],
    },
]


class TestConvert(unittest.TestCase):
    def _src(self, td: str) -> Path:
        p = Path(td) / "conversations.json"
        p.write_text(json.dumps(SAMPLE, ensure_ascii=False), encoding="utf-8")
        return p

    def test_converts_and_filters(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            written, skipped = convert(self._src(td), out)
            self.assertEqual(written, 1)   # 짧은 인사는 min_prompts=2 미달
            self.assertEqual(skipped, 1)
            note = next(out.rglob("*.md")).read_text(encoding="utf-8")
            self.assertIn("status: raw", note)
            self.assertIn("source: claude-ai", note)
            self.assertIn("임베딩 모델 어떻게 골라?", note)

    def test_dedup_by_uuid(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            convert(self._src(td), out)
            written2, skipped2 = convert(self._src(td), out)  # 같은 export 재실행
            self.assertEqual(written2, 0)
            self.assertEqual(skipped2, 2)


if __name__ == "__main__":
    unittest.main()
