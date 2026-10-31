import unittest
from unittest.mock import patch

from app import create_app
from tags import CUSTOM_TAGS, generate_tags


class TagApiTests(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_rejects_missing_text(self):
        response = self.client.post("/api/tags", json={})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["error"], "A text string is required")

    def test_returns_generated_tags(self):
        with patch("tags.jieba.cut", return_value=["旅行", "旅行", "故事"]):
            response = self.client.post("/api/tags", json={"text": "芭芭拉 旅行"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"tags": "芭芭拉,旅行,故事"})

    def test_custom_tags_are_prioritized_and_result_is_limited(self):
        with patch("tags.jieba.cut", return_value=["长关键词"] * 20):
            result = generate_tags("芭芭拉 " + "长关键词 " * 20)

        self.assertTrue(result.startswith("芭芭拉,"))
        self.assertLessEqual(len(result), 50)

    def test_custom_tag_list_matches_existing_supported_characters(self):
        self.assertEqual(len(CUSTOM_TAGS), 37)
        self.assertIn("芭芭拉", CUSTOM_TAGS)
        self.assertIn("三月七", CUSTOM_TAGS)


if __name__ == "__main__":
    unittest.main()
