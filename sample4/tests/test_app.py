import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_list_page(self):
        """测试首页返回 200"""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_api_list(self):
        """测试课程列表 API 返回 200 且为数组"""
        resp = self.client.get("/api/courses")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 8)

    def test_api_detail_ok(self):
        """测试课程详情 API 返回 200 且包含 id"""
        resp = self.client.get("/api/courses/1")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn("id", data)

    def test_api_detail_missing(self):
        """测试不存在的课程返回 404"""
        resp = self.client.get("/api/courses/9999")
        self.assertEqual(resp.status_code, 404)

    def test_detail_page_ok(self):
        """测试课程详情页返回 200"""
        resp = self.client.get("/course/1")
        self.assertEqual(resp.status_code, 200)

    def test_detail_page_missing(self):
        """测试不存在的课程详情页返回 404"""
        resp = self.client.get("/course/9999")
        self.assertEqual(resp.status_code, 404)


if __name__ == "__main__":
    unittest.main()