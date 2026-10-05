import tempfile
import unittest
from pathlib import Path

from cc2obsidian import convert_one, parse_session, render_note

FIXTURE = Path(__file__).parent / "fixtures" / "sample.jsonl"


class TestParseSession(unittest.TestCase):
    def test_parses_fixture(self):
        sess = parse_session(FIXTURE)
        self.assertIsNotNone(sess)
        self.assertEqual(sess["title"], "RAG 파이프라인 디버깅")
        self.assertEqual(sess["n_user"], 2)  # tool_result-only 턴은 제외
        self.assertIn("Bash", sess["tools"])

    def test_render_note_frontmatter(self):
        note = render_note(parse_session(FIXTURE), max_chars=40000)
        self.assertIn("status: raw", note)
        self.assertIn("claude-code/session", note)
        self.assertIn("임베딩이 왜 느리지?", note)


class TestConvertOne(unittest.TestCase):
    def test_writes_note(self):
        with tempfile.TemporaryDirectory() as td:
            out = convert_one(FIXTURE, Path(td))
            self.assertIsNotNone(out)
            self.assertTrue(out.is_file())
            self.assertIn("status: raw", out.read_text(encoding="utf-8"))

    def test_min_prompts_filter(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertIsNone(convert_one(FIXTURE, Path(td), min_prompts=5))

    def test_raw_note_is_refreshed(self):
        with tempfile.TemporaryDirectory() as td:
            out = convert_one(FIXTURE, Path(td))
            out.write_text("---\nstatus: raw\n---\nstale", encoding="utf-8")
            self.assertEqual(convert_one(FIXTURE, Path(td)), out)
            self.assertNotIn("stale", out.read_text(encoding="utf-8"))

    def test_curated_note_is_preserved(self):
        with tempfile.TemporaryDirectory() as td:
            out = convert_one(FIXTURE, Path(td))
            curated = "---\nstatus: distilled\n---\n- 핵심 교훈:: [[Some Note]]"
            out.write_text(curated, encoding="utf-8")
            self.assertIsNone(convert_one(FIXTURE, Path(td)))
            self.assertEqual(out.read_text(encoding="utf-8"), curated)


if __name__ == "__main__":
    unittest.main()
