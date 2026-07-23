"""
单元测试 - 测试 Flask 应用路由
"""
import sys
import os
import unittest

# 将项目根目录加入 sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app


class TestApp(unittest.TestCase):
    """测试 Flask 应用"""

    def setUp(self):
        self.client = app.test_client()

    def test_index_returns_200(self):
        """GET / 返回 200"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_index_contains_title(self):
        """GET / 包含标题 'Loop-20260723'"""
        response = self.client.get("/")
        self.assertIn(b"Loop-20260723", response.data)

    def test_index_html(self):
        """GET / 返回 HTML"""
        response = self.client.get("/")
        self.assertIn(b"text/html", response.content_type)


if __name__ == "__main__":
    unittest.main()