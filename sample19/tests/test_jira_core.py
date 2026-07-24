"""
Jira 复刻版 - 纯逻辑模块单元测试
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from jira_core import get_menus, get_user_info, get_kanban_columns, toggle_theme, validate_theme


class TestJiraCore(unittest.TestCase):
    """测试 jira_core 模块的纯函数"""

    def test_get_menus_returns_list(self):
        """get_menus 返回列表"""
        menus = get_menus()
        self.assertIsInstance(menus, list)
        self.assertGreaterEqual(len(menus), 3)

    def test_get_menus_contains_kanban(self):
        """get_menus 包含看板菜单"""
        menus = get_menus()
        ids = [m["id"] for m in menus]
        self.assertIn("kanban", ids)

    def test_get_menus_contains_dashboard(self):
        """get_menus 包含仪表盘菜单"""
        menus = get_menus()
        ids = [m["id"] for m in menus]
        self.assertIn("dashboard", ids)

    def test_get_menus_contains_projects(self):
        """get_menus 包含项目菜单"""
        menus = get_menus()
        ids = [m["id"] for m in menus]
        self.assertIn("projects", ids)

    def test_get_menus_contains_issues(self):
        """get_menus 包含问题菜单"""
        menus = get_menus()
        ids = [m["id"] for m in menus]
        self.assertIn("issues", ids)

    def test_get_user_info_has_name(self):
        """get_user_info 返回包含 name 字段"""
        user = get_user_info()
        self.assertIn("name", user)
        self.assertIsInstance(user["name"], str)

    def test_get_user_info_has_email(self):
        """get_user_info 返回包含 email 字段"""
        user = get_user_info()
        self.assertIn("email", user)
        self.assertIsInstance(user["email"], str)

    def test_get_user_info_has_role(self):
        """get_user_info 返回包含 role 字段"""
        user = get_user_info()
        self.assertIn("role", user)
        self.assertIsInstance(user["role"], str)

    def test_get_user_info_has_department(self):
        """get_user_info 返回包含 department 字段"""
        user = get_user_info()
        self.assertIn("department", user)
        self.assertIsInstance(user["department"], str)

    def test_get_kanban_columns_returns_list(self):
        """get_kanban_columns 返回列表"""
        columns = get_kanban_columns()
        self.assertIsInstance(columns, list)
        self.assertGreaterEqual(len(columns), 2)

    def test_get_kanban_columns_has_title(self):
        """get_kanban_columns 每列有 title"""
        columns = get_kanban_columns()
        for col in columns:
            self.assertIn("title", col)

    def test_get_kanban_columns_has_cards(self):
        """get_kanban_columns 每列有 cards 列表"""
        columns = get_kanban_columns()
        for col in columns:
            self.assertIn("cards", col)
            self.assertIsInstance(col["cards"], list)

    def test_toggle_theme_light_to_dark(self):
        """toggle_theme 从 light 切换到 dark"""
        result = toggle_theme('light')
        self.assertEqual(result, 'dark')

    def test_toggle_theme_dark_to_light(self):
        """toggle_theme 从 dark 切换到 light"""
        result = toggle_theme('dark')
        self.assertEqual(result, 'light')

    def test_validate_theme_light(self):
        """validate_theme 验证 light 返回 True"""
        self.assertTrue(validate_theme('light'))

    def test_validate_theme_dark(self):
        """validate_theme 验证 dark 返回 True"""
        self.assertTrue(validate_theme('dark'))

    def test_validate_theme_invalid(self):
        """validate_theme 验证无效主题返回 False"""
        self.assertFalse(validate_theme('invalid'))
        self.assertFalse(validate_theme(''))
        self.assertFalse(validate_theme(None))


if __name__ == '__main__':
    unittest.main()