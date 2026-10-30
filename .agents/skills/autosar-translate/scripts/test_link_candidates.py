import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).with_name("link_candidates.py")
SPEC = importlib.util.spec_from_file_location("link_candidates", SCRIPT)
LINK_CANDIDATES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(LINK_CANDIDATES)


class RegistryEntriesTest(unittest.TestCase):
    def test_bullet_prefixed_registry_entry_is_parsed_and_linked(self):
        article = """### 3.1. 输入文件和相关标准与规范

- [1] General Specification of Basic Software Modules AUTOSAR_CP_SWS_BSWGeneral

### 3.2. 相关规范

参见参考文档[1]。
"""

        self.assertEqual(
            {
                "1": (
                    "General Specification of Basic Software Modules AUTOSAR_CP_SWS_BSWGeneral",
                    "AUTOSAR_CP_SWS_BSWGeneral",
                )
            },
            LINK_CANDIDATES.parse_entries31(article),
        )

        linked = LINK_CANDIDATES.apply_links(article)
        self.assertIn(
            '<a id="ref-1"></a>- [1] General Specification of Basic Software Modules',
            linked,
        )
        self.assertIn(r"[\[1\]](#ref-1)", linked)

    def test_citation_with_display_title_links_and_keeps_its_label(self):
        article = "\n".join(
            [
                "## 3. 相关文档",
                "",
                "### 3.1. 输入文件和相关标准与规范",
                "",
                "- [1] Glossary AUTOSAR_FO_TR_Glossary",
                "",
                "### 3.2. 相关规范",
                "",
                "术语说明见 [1, AUTOSAR 术语表]。",
                "",
            ]
        )

        first_pass = LINK_CANDIDATES.apply_links(article)
        second_pass = LINK_CANDIDATES.apply_links(first_pass)

        self.assertIn(r"[\[1, AUTOSAR 术语表\]](#ref-1)", first_pass)
        self.assertEqual(first_pass, second_pass)

    def test_apply_is_idempotent_when_identifier_link_follows_other_document(self):
        article = "\n".join(
            [
                "## 1. 功能",
                "",
                "### 1.1. 内部功能",
                "",
                "## 3. 相关文档",
                "",
                "### 3.1. 输入文件和相关标准与规范",
                "",
                "- [1] External standard AUTOSAR_CP_SWS_ExternalStandard",
                "",
                "### 3.2. 相关规范",
                "",
                "## 6. 约束",
                "",
                "见 AUTOSAR_CP_SWS_BSWGeneral 中 DcmDspData 的第 1.1 节。",
                "",
                "## 7. API",
                "",
                "### 7.2. 类型定义",
                "",
                "#### 7.2.1. DcmDspData",
                "",
            ]
        )

        first_pass = LINK_CANDIDATES.apply_links(article)
        second_pass = LINK_CANDIDATES.apply_links(first_pass)

        self.assertIn("的第 1.1 节。", first_pass)
        self.assertEqual(first_pass, second_pass)

    def test_citation_link_expansion_does_not_hide_later_sentence_reference(self):
        article = "\n".join(
            [
                "## 1. 功能",
                "",
                "### 1.1. 内部功能",
                "",
                "## 3. 相关文档",
                "",
                "### 3.1. 输入文件和相关标准与规范",
                "",
                "- [1] External standard AUTOSAR_CP_SWS_ExternalStandard",
                "",
                "### 3.2. 相关规范",
                "",
                "**ISO14229-1** [1] 为该服务定义的 **NRC** 顺序将需要更多的 **API**，"
                "这会使整体服务处理更加复杂。详情见第 1.1 节。",
                "",
            ]
        )

        first_pass = LINK_CANDIDATES.apply_links(article)
        second_pass = LINK_CANDIDATES.apply_links(first_pass)

        self.assertIn("详情见第 [1.1](#11-内部功能) 节。", first_pass)
        self.assertEqual(first_pass, second_pass)

    def test_internal_section_reference_after_cited_sentence_is_linked(self):
        article = "\n".join(
            [
                "## 1. 功能",
                "",
                "### 1.1. 内部功能",
                "",
                "## 3. 相关文档",
                "",
                "### 3.1. 输入文件和相关标准与规范",
                "",
                "- [1] External standard AUTOSAR_CP_SWS_ExternalStandard",
                "",
                "### 3.2. 相关规范",
                "",
                "依据外部标准[1]，此处内容较为复杂。详情见第 1.1 节。",
                "",
            ]
        )

        first_pass = LINK_CANDIDATES.apply_links(article)
        second_pass = LINK_CANDIDATES.apply_links(first_pass)

        self.assertIn("详情见第 [1.1](#11-内部功能) 节。", first_pass)
        self.assertEqual(first_pass, second_pass)


class SlugGenerationTest(unittest.TestCase):
    def test_slug_collapses_hyphens_around_punctuation(self):
        self.assertEqual(
            "66221-服务-0x36-transferdata",
            LINK_CANDIDATES.slug_of("6.6.2.21", "服务 0x36 - TransferData"),
        )


if __name__ == "__main__":
    unittest.main()
