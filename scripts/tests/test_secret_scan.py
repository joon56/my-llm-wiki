import tempfile
import unittest
from pathlib import Path

from secret_scan import scan_paths

FAKE_ANT = "sk-ant-" + "api03-abcdefghij1234567890"  # 연결 조합 — 스캐너 자기검출 방지
FAKE_AWS = "AKIA" + "IOSFODNN7EXAMPLE"


class TestScan(unittest.TestCase):
    def _write(self, td, name, text):
        p = Path(td) / name
        p.write_text(text, encoding="utf-8")
        return p

    def test_detects_high(self):
        with tempfile.TemporaryDirectory() as td:
            self._write(td, "a.md", f"key = {FAKE_ANT}\n")
            self._write(td, "b.md", f"aws: {FAKE_AWS}\n")
            findings = scan_paths([Path(td)])
            self.assertEqual(len([f for f in findings if f[0] == "HIGH"]), 2)

    def test_masks_secret(self):
        with tempfile.TemporaryDirectory() as td:
            self._write(td, "a.md", f"{FAKE_ANT}\n")
            (_, _, _, _, masked) = scan_paths([Path(td)])[0]
            self.assertNotIn(FAKE_ANT, masked)
            self.assertTrue(masked.endswith("…"))

    def test_clean_dir(self):
        with tempfile.TemporaryDirectory() as td:
            self._write(td, "a.md", "평범한 노트입니다.\n")
            self.assertEqual(scan_paths([Path(td)]), [])

    def test_medium_only_no_high(self):
        with tempfile.TemporaryDirectory() as td:
            self._write(td, "a.md", 'password: "correct-horse-battery"\n')
            findings = scan_paths([Path(td)])
            self.assertTrue(findings)
            self.assertTrue(all(f[0] == "MEDIUM" for f in findings))


if __name__ == "__main__":
    unittest.main()
