"""
单元测试 - 测试 course_core 模块的核心功能
"""
import unittest
import json
import os
import sys
import tempfile

# 将项目根目录加入 sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from course_core import load_courses, get_course_by_id, update_progress, get_course_progress


class TestCourseCore(unittest.TestCase):
    """测试课程核心逻辑模块"""

    def setUp(self):
        """创建临时数据文件用于测试"""
        self.test_data = {
            "courses": [
                {
                    "id": 1,
                    "title": "测试课程1",
                    "description": "描述1",
                    "chapters": [
                        {"id": "ch1", "title": "章节1"},
                        {"id": "ch2", "title": "章节2"}
                    ],
                    "progress": {}
                },
                {
                    "id": 2,
                    "title": "测试课程2",
                    "description": "描述2",
                    "chapters": [
                        {"id": "ch1", "title": "章节A"}
                    ],
                    "progress": {"ch1": True}
                }
            ]
        }
        # 创建临时文件
        self.temp_file = tempfile.NamedTemporaryFile(
            mode='w', encoding='utf-8', delete=False, suffix='.json'
        )
        json.dump(self.test_data, self.temp_file, ensure_ascii=False, indent=2)
        self.temp_file.close()
        self.data_file = self.temp_file.name

    def tearDown(self):
        """清理临时文件"""
        if os.path.exists(self.data_file):
            os.unlink(self.data_file)

    def test_load_courses_returns_list(self):
        """测试 load_courses 返回列表"""
        courses = load_courses(self.data_file)
        self.assertIsInstance(courses, list)
        self.assertEqual(len(courses), 2)

    def test_load_courses_returns_correct_data(self):
        """测试 load_courses 返回正确的课程数据"""
        courses = load_courses(self.data_file)
        self.assertEqual(courses[0]['title'], '测试课程1')
        self.assertEqual(courses[1]['title'], '测试课程2')

    def test_load_courses_file_not_found(self):
        """测试文件不存在时返回空列表"""
        courses = load_courses('/nonexistent/path.json')
        self.assertEqual(courses, [])

    def test_get_course_by_id_exists(self):
        """测试 get_course_by_id 返回存在的课程"""
        course = get_course_by_id(self.data_file, 1)
        self.assertIsNotNone(course)
        self.assertEqual(course['id'], 1)
        self.assertEqual(course['title'], '测试课程1')

    def test_get_course_by_id_not_exists(self):
        """测试 get_course_by_id 返回 None（课程不存在）"""
        course = get_course_by_id(self.data_file, 999)
        self.assertIsNone(course)

    def test_update_progress_success(self):
        """测试 update_progress 成功更新进度"""
        result = update_progress(self.data_file, 1, 'ch1', True)
        self.assertTrue(result)
        # 验证数据已更新
        course = get_course_by_id(self.data_file, 1)
        self.assertEqual(course['progress']['ch1'], True)

    def test_update_progress_course_not_found(self):
        """测试 update_progress 课程不存在时返回 False"""
        result = update_progress(self.data_file, 999, 'ch1', True)
        self.assertFalse(result)

    def test_update_progress_chapter_not_found(self):
        """测试 update_progress 章节不存在时返回 False"""
        result = update_progress(self.data_file, 1, 'nonexistent', True)
        self.assertFalse(result)

    def test_get_course_progress_exists(self):
        """测试 get_course_progress 返回正确的进度"""
        progress = get_course_progress(self.data_file, 2)
        self.assertEqual(progress, {'ch1': True})

    def test_get_course_progress_not_exists(self):
        """测试 get_course_progress 课程不存在时返回 None"""
        progress = get_course_progress(self.data_file, 999)
        self.assertIsNone(progress)

    def test_get_course_progress_empty(self):
        """测试 get_course_progress 返回空进度"""
        progress = get_course_progress(self.data_file, 1)
        self.assertEqual(progress, {})


if __name__ == '__main__':
    unittest.main()