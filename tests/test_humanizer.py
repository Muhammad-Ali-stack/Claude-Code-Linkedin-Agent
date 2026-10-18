"""Tests for the li-human scripts. Standard library only: python -m unittest"""

import importlib.util
import json
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HUMAN = os.path.join(ROOT, "skills", "li-human")


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HUMAN, name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


humanize = load("humanize")
detect = load("detect")
LEX = humanize.load_lexicon()

SLOPPY = (
    "In today’s fast-paced world, we must leverage robust tools — "
    "it’s not just a trend, it’s a revolution.​ "
    "Let that sink in. Moreover, this is a testament to seamless innovation… "
    "What are your thoughts?\n#ai #growth #leadership #future #tech"
)


def clean(text):
    return humanize.humanize(text, LEX)[0]


class HumanizeTest(unittest.TestCase):
    def test_removes_invisible_characters(self):
        out = clean("zero​width⁠joined﻿ text")
        self.assertEqual(out, "zerowidthjoined text\n")

    def test_em_dash_becomes_comma(self):
        self.assertEqual(clean("Fast — and cheap."), "Fast, and cheap.\n")
        self.assertEqual(clean("Fast—and cheap."), "Fast, and cheap.\n")

    def test_en_dash_in_range_becomes_hyphen(self):
        self.assertEqual(clean("Pages 5–10."), "Pages 5-10.\n")

    def test_curly_quotes_and_ellipsis(self):
        self.assertEqual(clean("“It’s fine…”"), "\"It's fine...\"\n")

    def test_lexicon_preserves_capitalisation(self):
        out = clean("Leverage the data. We leverage it daily.")
        self.assertNotIn("everage", out)
        self.assertTrue(out[0].isupper())

    def test_phrase_matches_across_line_break(self):
        report = humanize.humanize("In today's fast-paced\nworld, it changes.", LEX)[1]
        found = [h["find"] for h in report["lexical"]]
        self.assertIn("in today's fast-paced world", found)

    def test_term_ending_in_punctuation_matches(self):
        pattern = humanize.term_pattern("what are your thoughts?")
        self.assertTrue(pattern.search("Great.\nWhat are your thoughts?"))

    def test_urls_are_untouched(self):
        url = "https://example.com/leverage—robust"
        self.assertIn(url, clean(f"See {url} today."))

    def test_structures_are_flagged_not_rewritten(self):
        text = "It's not just a tool, it's a mindset."
        out, report = humanize.humanize(text, LEX)
        self.assertIn("not just", out)
        self.assertTrue(report["structures"])

    def test_clean_text_is_stable(self):
        once = clean(SLOPPY)
        self.assertEqual(clean(once), once)


class DetectTest(unittest.TestCase):
    def test_humanize_raises_the_score(self):
        _, before, _ = detect.run(SLOPPY, LEX)
        _, after, _ = detect.run(clean(SLOPPY), LEX)
        self.assertGreater(after, before)

    def test_fingerprint_counts_em_dash_and_invisible(self):
        score, detail = detect.check_fingerprint("a — b​ c")
        self.assertLess(score, 100)
        self.assertIn("1 invisible", detail)
        self.assertIn("1 em dash", detail)

    def test_scores_stay_in_range(self):
        results, overall, verdict = detect.run(SLOPPY, LEX)
        for score, _ in results.values():
            self.assertTrue(0 <= score <= 100)
        self.assertIn(verdict, {"PASS", "REVIEW", "FLAGGED"})


class CliTest(unittest.TestCase):
    """The scripts must print Unicode without crashing on any console."""

    def run_script(self, name, *args, stdin=""):
        env = dict(os.environ, PYTHONIOENCODING="cp1252")
        return subprocess.run(
            [sys.executable, os.path.join(HUMAN, name), *args],
            input=stdin.encode("utf-8"), capture_output=True, env=env,
        )

    def test_humanize_cli_on_legacy_console(self):
        proc = self.run_script("humanize.py", "-", "--report", stdin=SLOPPY)
        self.assertEqual(proc.returncode, 0, proc.stderr.decode("utf-8", "replace"))
        self.assertNotIn("—", proc.stdout.decode("utf-8"))

    def test_detect_cli_json(self):
        proc = self.run_script("detect.py", "-", "--json", stdin=SLOPPY)
        self.assertEqual(proc.returncode, 0, proc.stderr.decode("utf-8", "replace"))
        self.assertIn("human_score", json.loads(proc.stdout))

    def test_missing_file_is_a_clean_error(self):
        proc = self.run_script("detect.py", "no-such-file.txt")
        self.assertNotEqual(proc.returncode, 0)
        self.assertNotIn(b"Traceback", proc.stderr)


if __name__ == "__main__":
    unittest.main()
