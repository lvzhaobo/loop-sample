import sys
import os
import unittest

# 将项目根目录加入sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_list_page(self):
        """测试首页返回200"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_activities_list(self):
        """测试JSON活动列表返回200且为数组"""
        response = self.app.get('/api/activities')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 8)

    def test_api_activity_detail_ok(self):
        """测试存在的活动详情返回200"""
        response = self.app.get('/api/activities/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertEqual(data['id'], 1)

    def test_api_activity_detail_missing(self):
        """测试不存在的活动详情返回404"""
        response = self.app.get('/api/activities/9999')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn('error', data)

    def test_detail_page_ok(self):
        """测试存在的活动详情页返回200"""
        response = self.app.get('/activity/1')
        self.assertEqual(response.status_code, 200)

    def test_detail_page_missing(self):
        """测试不存在的活动详情页返回404"""
        response = self.app.get('/activity/9999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()