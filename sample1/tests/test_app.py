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
        """测试课程列表 JSON 接口返回 200 且为数组"""
        response = self.app.get('/api/courses')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 6)

    def test_api_course_detail_ok(self):
        """测试存在的课程详情 JSON 接口返回 200 且包含 id"""
        response = self.app.get('/api/courses/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertEqual(data['id'], 1)

    def test_api_course_detail_missing(self):
        """测试不存在的课程详情 JSON 接口返回 404"""
        response = self.app.get('/api/courses/9999')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn('error', data)

    def test_detail_page_ok(self):
        """测试存在的课程详情页返回 200"""
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200)

    def test_detail_page_missing(self):
        """测试不存在的课程详情页返回 404"""
        response = self.app.get('/course/9999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()