import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "link_candidates.py"
SPEC = importlib.util.spec_from_file_location("link_candidates", SCRIPT)
LINK_CANDIDATES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(LINK_CANDIDATES)


class ChapterReferenceTests(unittest.TestCase):
    def test_j1939_identifier_followed_by_section_noun_is_not_a_reference(self):
        self.assertEqual(LINK_CANDIDATES.chref_spans("J1939 节点"), [])

    def test_chinese_chapter_reference_is_still_detected(self):
        spans = LINK_CANDIDATES.chref_spans("参见第9.2.2章。")
        self.assertEqual([num for _, _, num in spans], ["9.2.2"])

    def test_dotted_chapter_reference_after_ascii_word_is_detected(self):
        spans = LINK_CANDIDATES.chref_spans("BswM 9.2.2章")
        self.assertEqual([num for _, _, num in spans], ["9.2.2"])


if __name__ == "__main__":
    unittest.main()
