import sys
import os
import unittest

# 将项目根目录加入sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app


class TestApp(unittest.TestCase):
    """测试Flask应用的核心路由"""

    def setUp(self):
        self.client = app.test_client()

    def test_list_page(self):
        """测试首页返回200"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_list(self):
        """测试JSON列表接口返回200且为数组，长度>=8"""
        response = self.client.get('/api/fs_009_items')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 8)

    def test_api_detail_ok(self):
        """测试存在的详情接口返回200且包含id"""
        response = self.client.get('/api/fs_009_items/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertEqual(data['id'], 1)

    def test_api_detail_missing(self):
        """测试不存在的详情接口返回404"""
        response = self.client.get('/api/fs_009_items/9999')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn('error', data)

    def test_detail_page_ok(self):
        """测试存在的详情页返回200"""
        response = self.client.get('/fs_009_item/1')
        self.assertEqual(response.status_code, 200)

    def test_detail_page_missing(self):
        """测试不存在的详情页返回404"""
        response = self.client.get('/fs_009_item/9999')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()