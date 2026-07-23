import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_list_page(self):
        """测试首页返回 200"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_list(self):
        """测试 JSON 列表返回 200 且为数组"""
        response = self.client.get('/api/tomatoes')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 8)

    def test_api_detail_ok(self):
        """测试 JSON 详情返回 200 且包含 id"""
        response = self.client.get('/api/tomatoes/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('id', data)

    def test_api_detail_missing(self):
        """测试不存在的 JSON 详情返回 404"""
        response = self.client.get('/api/tomatoes/9999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()