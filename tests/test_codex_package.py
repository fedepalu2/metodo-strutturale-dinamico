from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'codex/metodo-strutturale-dinamico'


class PackageTests(unittest.TestCase):
    def test_package_exposes_one_definition_without_the_claude_variant(self):
        self.assertEqual(list(PACKAGE.rglob('SKILL.md')), [PACKAGE/'SKILL.md'])
        self.assertFalse((PACKAGE/'claude').exists())

    def test_compatibility_files_match_the_installable_package(self):
        expected = [ROOT/'SKILL.md', *sorted((ROOT/'agents').rglob('*')), *sorted((ROOT/'references').rglob('*'))]
        expected = [file for file in expected if file.is_file()]
        self.assertEqual(len(expected), len([file for file in PACKAGE.rglob('*') if file.is_file()]))
        for file in expected:
            self.assertEqual(file.read_bytes(), (PACKAGE/file.relative_to(ROOT)).read_bytes())

    def test_entrypoint_links_resolve_in_package(self):
        body = (PACKAGE/'SKILL.md').read_text(encoding='utf-8')
        for link in re.findall(r'`(references/[^`]+\.md)`', body):
            self.assertTrue((PACKAGE/link).is_file(), link)


if __name__ == '__main__':
    unittest.main()
