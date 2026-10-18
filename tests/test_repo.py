"""Consistency checks for the skill pack: manifests, data files and SKILL.md headers."""

import glob
import json
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md")))


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


class RepoTest(unittest.TestCase):
    def test_json_files_parse(self):
        paths = glob.glob(os.path.join(ROOT, "**", "*.json"), recursive=True)
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=os.path.relpath(path, ROOT)):
                json.loads(read(path))

    def test_every_skill_has_matching_frontmatter(self):
        for path in SKILLS:
            folder = os.path.basename(os.path.dirname(path))
            with self.subTest(skill=folder):
                text = read(path)
                self.assertTrue(text.startswith("---\n"))
                self.assertIn(f"\nname: {folder}\n", text)
                self.assertIn("\ndescription:", text)

    def test_readme_lists_every_skill(self):
        readme = read(os.path.join(ROOT, "README.md"))
        for path in SKILLS:
            folder = os.path.basename(os.path.dirname(path))
            with self.subTest(skill=folder):
                self.assertIn(f"`/{folder}`", readme)

    def test_skill_count_matches_badge(self):
        readme = read(os.path.join(ROOT, "README.md"))
        badge = re.search(r"badge/skills-(\d+)-", readme)
        self.assertIsNotNone(badge)
        self.assertEqual(int(badge.group(1)), len(SKILLS))

    def test_lexicon_regexes_compile(self):
        lex = json.loads(read(os.path.join(ROOT, "skills", "li-human", "slop.json")))
        for structure in lex["structures"]:
            with self.subTest(structure=structure["id"]):
                re.compile(structure["regex"], re.MULTILINE)


if __name__ == "__main__":
    unittest.main()
