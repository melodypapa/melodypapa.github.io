import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).with_name("check_api_sync.py")
SPEC = importlib.util.spec_from_file_location("check_api_sync", SCRIPT)
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class SourceEntriesTest(unittest.TestCase):
    def test_leaf_heading_with_extraction_space_after_escaped_underscore(self):
        source = r"## 8.3.2.5 Dcm\_ SetActiveDiagnostic"

        self.assertEqual(
            ["Dcm_SetActiveDiagnostic"],
            CHECKER.source_entries(source, "3"),
        )


if __name__ == "__main__":
    unittest.main()
