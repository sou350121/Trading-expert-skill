import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import daily_update as d


class DailyTests(unittest.TestCase):
    evidence = {"1": {"path": "foundations/a.md", "excerpt": "public research evidence"}}

    def test_valid_pick(self):
        self.assertEqual(d.select('{"picks":[{"id":"1","angle":"limits"}]}', self.evidence), {"1":"limits"})

    def test_rejects_added_text_urls_invalid_ids_and_duplicates(self):
        for bad in ('{"picks":[]}',
                    '{"picks":[{"id":"7","angle":"method"}]}',
                    '{"picks":[{"id":"1","angle":"link"}]}',
                    '{"picks":[{"id":"1","angle":"method","quote":"invented"}]}',
                    '{"picks":[{"id":"1","angle":"method"},{"id":"1","angle":"method"}]}',
                    '{"picks":[],"picks":[{"id":"1","angle":"limits"}]}',
                    '{"picks":[{"id":[],"angle":"method"}]}'):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                d.select(bad, self.evidence)

    def test_bootstrap_and_noop(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            head = "a"*40
            files = {d.MANIFEST: json.dumps({"commit":head,"files":[{"path":"foundations/a.md","sha256":"A"}]}).encode(),
                     "HANDBOOK_INDEX.md": b"index"}
            for name, content in files.items():
                (folder/name).write_bytes(content)
            with patch.object(d, "snapshot", side_effect=lambda *_:files.copy()), patch.object(
                    d, "source_git", return_value=b"foundations/a.md\n"), patch.object(
                    d, "gather", return_value=self.evidence):
                with self.assertRaises(ValueError):
                    d.prepare(folder, folder, head, lambda _: "invalid")
                self.assertFalse((folder/d.GUIDE).exists())
                prepared, model = d.prepare(folder, folder, head, lambda _: '{"picks":[{"id":"1","angle":"method"}]}')
                self.assertTrue(model)
                self.assertIn(f"/blob/{head}/foundations/a.md", prepared[d.GUIDE].decode())
                self.assertIn("public research evidence", prepared[d.GUIDE].decode())
                (folder/d.GUIDE).write_bytes(prepared[d.GUIDE])
                self.assertEqual(d.prepare(folder, folder, head, lambda _: self.fail("called model")), ({},False))
                (folder/"HANDBOOK_INDEX.md").write_bytes(b"corrupt")
                with self.assertRaisesRegex(ValueError, "baseline_bundle"):
                    d.prepare(folder, folder, head, lambda _: self.fail("called model"))

    def test_code_only_change_renews_pins_without_model(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            head = "b"*40
            data = [{"path":"foundations/a.md","sha256":"A"}]
            (folder/d.MANIFEST).write_text(json.dumps({"commit":"a"*40,"files":data}))
            (folder/d.GUIDE).touch()
            files = {d.MANIFEST: json.dumps({"commit":head,"files":data}).encode()}
            with patch.object(d, "snapshot", return_value=files), patch.object(
                    d, "source_git", return_value=b""), patch.object(d, "gather", return_value={}):
                output, model = d.prepare(folder, folder, head, lambda _: self.fail("called model"))
                self.assertFalse(model)
                self.assertIn(head, output[d.GUIDE].decode())
