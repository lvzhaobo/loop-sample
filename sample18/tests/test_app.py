"""
单元测试 - 测试 Flask 应用路由
"""
import unittest
import json
import os
import sys

# 将项目根目录加入 sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app


class TestAppRoutes(unittest.TestCase):
    """测试 Flask 应用路由"""

    def setUp(self):
        """创建测试客户端"""
        self.app = app.test_client()
        self.app.testing = True

    def test_index_returns_200(self):
        """测试首页返回 200"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_contains_title(self):
        """测试首页包含标题文案"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('在线学习平台', response.data.decode('utf-8'))

    def test_api_courses_returns_200(self):
        """测试课程列表 API 返回 200"""
        response = self.app.get('/api/courses')
        self.assertEqual(response.status_code, 200)

    def test_api_courses_returns_json_array(self):
        """测试课程列表 API 返回 JSON 数组"""
        response = self.app.get('/api/courses')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)

    def test_api_courses_detail_exists(self):
        """测试存在的课程详情返回 200 且包含 id"""
        response = self.app.get('/api/courses/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, dict)
        self.assertIn('id', data)
        self.assertEqual(data['id'], 1)

    def test_api_courses_detail_not_found(self):
        """测试不存在的课程详情返回 404"""
        response = self.app.get('/api/courses/999')
        self.assertEqual(response.status_code, 404)

    def test_api_progress_missing_params(self):
        """测试进度更新缺少参数返回 400"""
        response = self.app.post('/api/progress',
                                 content_type='application/json',
                                 data=json.dumps({}))
        self.assertEqual(response.status_code, 400)

    def test_api_progress_success(self):
        """测试进度更新成功"""
        response = self.app.post('/api/progress',
                                 content_type='application/json',
                                 data=json.dumps({
                                     'course_id': 1,
                                     'chapter_id': 'ch1',
                                     'completed': True
                                 }))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'ok')


if __name__ == '__main__':
    unittest.main()