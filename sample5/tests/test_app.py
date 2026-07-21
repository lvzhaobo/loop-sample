import sys
import os
import unittest

# 将项目根目录加入 sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_list_page(self):
        """测试列表页返回200"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_list(self):
        """测试JSON列表接口返回200且为数组"""
        response = self.app.get('/api/tomatoes')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 8)

    def test_api_detail_ok(self):
        """测试JSON详情接口返回200且包含id"""
        response = self.app.get('/api/tomatoes/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertEqual(data['id'], 1)

    def test_api_detail_missing(self):
        """测试不存在的JSON详情接口返回404"""
        response = self.app.get('/api/tomatoes/9999')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn('error', data)

    def test_detail_page_ok(self):
        """测试详情页返回200"""
        response = self.app.get('/tomato/1')
        self.assertEqual(response.status_code, 200)

    def test_detail_page_missing(self):
        """测试不存在的详情页返回404"""
        response = self.app.get('/tomato/9999')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()