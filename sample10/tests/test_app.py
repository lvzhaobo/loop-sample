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
        """测试首页返回 200"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_courses_list(self):
        """测试 GET /api/courses 返回 200 且为 JSON 数组，长度 >= 8"""
        response = self.app.get('/api/courses')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 8)

    def test_api_course_detail_ok(self):
        """测试 GET /api/courses/1 返回 200 且为包含 id 的对象"""
        response = self.app.get('/api/courses/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertIn('id', data)
        self.assertEqual(data['id'], 1)

    def test_api_course_detail_missing(self):
        """测试 GET /api/courses/9999 返回 404"""
        response = self.app.get('/api/courses/9999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()