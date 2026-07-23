"""
Flask 应用路由测试
"""
import sys
import os
import unittest

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
        """测试首页返回200状态码"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_contains_loop_label(self):
        """测试首页包含指定文案"""
        response = self.app.get('/')
        self.assertIn(b'Loop-20260721', response.data)

    def test_index_contains_timer_display(self):
        """测试首页包含计时器显示元素"""
        response = self.app.get('/')
        self.assertIn(b'timerDisplay', response.data)

    def test_index_contains_start_button(self):
        """测试首页包含开始按钮"""
        response = self.app.get('/')
        self.assertIn(b'startBtn', response.data)

    def test_index_contains_pause_button(self):
        """测试首页包含暂停按钮"""
        response = self.app.get('/')
        self.assertIn(b'pauseBtn', response.data)

    def test_index_contains_reset_button(self):
        """测试首页包含重置按钮"""
        response = self.app.get('/')
        self.assertIn(b'resetBtn', response.data)

    def test_index_html_content_type(self):
        """测试首页返回HTML内容类型"""
        response = self.app.get('/')
        self.assertIn('text/html', response.content_type)

    def test_static_css_exists(self):
        """测试静态CSS文件可访问"""
        response = self.app.get('/static/css/style.css')
        self.assertEqual(response.status_code, 200)

    def test_static_js_exists(self):
        """测试静态JS文件可访问"""
        response = self.app.get('/static/js/pomodoro.js')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()