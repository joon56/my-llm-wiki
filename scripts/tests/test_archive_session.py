import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "archive_session.py"
FIXTURE = Path(__file__).parent / "fixtures" / "sample.jsonl"


class TestHook(unittest.TestCase):
    def _run(self, payload: dict, out_dir: str):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--out", out_dir],
            input=json.dumps(payload), capture_output=True, text=True, timeout=30,
        )

    def test_archives_transcript(self):
        with tempfile.TemporaryDirectory() as td:
            r = self._run({"transcript_path": str(FIXTURE)}, td)
            self.assertEqual(r.returncode, 0)
            notes = list(Path(td).rglob("*.md"))
            self.assertEqual(len(notes), 1)

    def test_missing_path_is_noop(self):
        with tempfile.TemporaryDirectory() as td:
            r = self._run({}, td)
            self.assertEqual(r.returncode, 0)
            self.assertEqual(list(Path(td).rglob("*.md")), [])

    def test_broken_stdin_never_fails(self):
        with tempfile.TemporaryDirectory() as td:
            r = subprocess.run(
                [sys.executable, str(SCRIPT), "--out", td],
                input="not json", capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
