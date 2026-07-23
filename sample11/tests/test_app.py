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
        """测试列表页返回200"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_list(self):
        """测试JSON列表接口返回200且为数组"""
        response = self.app.get('/api/sort_visuals')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 8)

    def test_api_detail_ok(self):
        """测试JSON详情接口返回200且包含id"""
        response = self.app.get('/api/sort_visuals/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertEqual(data['id'], 1)

    def test_api_detail_missing(self):
        """测试不存在的资源返回404"""
        response = self.app.get('/api/sort_visuals/9999')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn('error', data)


if __name__ == '__main__':
    unittest.main()