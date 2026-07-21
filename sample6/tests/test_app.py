import sys
import os
import unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_list_page(self):
        """测试列表页返回 200"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_tomatoes(self):
        """测试 JSON 列表接口返回 200 且为数组"""
        response = self.app.get('/api/tomatoes')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 8)

    def test_api_tomato_detail_ok(self):
        """测试 JSON 详情接口返回 200 且包含 id"""
        response = self.app.get('/api/tomatoes/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertEqual(data['id'], 1)

    def test_api_tomato_detail_missing(self):
        """测试不存在的番茄时钟返回 404"""
        response = self.app.get('/api/tomatoes/9999')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()