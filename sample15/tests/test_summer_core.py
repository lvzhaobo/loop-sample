"""
暑假生活学习平台 - 纯逻辑模块单元测试
"""
import sys
import os
import unittest

# 将项目根目录加入 sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from summer_core import (
    get_activities,
    get_activity_by_id,
    get_summer_dates,
    get_activities_by_type,
    get_activities_count
)
from datetime import date


class TestSummerCore(unittest.TestCase):
    """测试 summer_core 模块的纯函数"""

    def test_get_activities_returns_list(self):
        """get_activities() 返回列表"""
        activities = get_activities()
        self.assertIsInstance(activities, list)

    def test_get_activities_has_items(self):
        """get_activities() 返回非空列表"""
        activities = get_activities()
        self.assertGreater(len(activities), 0)

    def test_get_activities_items_have_id(self):
        """每个活动都有 id 字段"""
        activities = get_activities()
        for activity in activities:
            self.assertIn("id", activity)

    def test_get_activity_by_id_exists(self):
        """get_activity_by_id(1) 返回包含 id 的字典"""
        activity = get_activity_by_id(1)
        self.assertIsNotNone(activity)
        self.assertIn("id", activity)
        self.assertEqual(activity["id"], 1)

    def test_get_activity_by_id_not_exists(self):
        """get_activity_by_id(999) 返回 None"""
        activity = get_activity_by_id(999)
        self.assertIsNone(activity)

    def test_get_summer_dates(self):
        """get_summer_dates() 返回 (7月1日, 8月31日)"""
        start, end = get_summer_dates(2026)
        self.assertEqual(start, date(2026, 7, 1))
        self.assertEqual(end, date(2026, 8, 31))

    def test_get_activities_by_type(self):
        """get_activities_by_type('学习') 返回学习类活动"""
        activities = get_activities_by_type("学习")
        for activity in activities:
            self.assertEqual(activity["type"], "学习")

    def test_get_activities_count(self):
        """get_activities_count() 返回正确数量"""
        count = get_activities_count()
        self.assertEqual(count, len(get_activities()))


if __name__ == '__main__':
    unittest.main()