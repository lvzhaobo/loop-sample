"""
Jira 复刻版 - 纯逻辑模块
包含主题切换逻辑、用户数据管理、菜单数据管理等纯函数，无副作用，便于单测。
"""

def get_menus():
    """返回菜单列表"""
    return [
        {"id": "kanban", "label": "看板"},
        {"id": "dashboard", "label": "仪表盘"},
        {"id": "projects", "label": "项目"},
        {"id": "issues", "label": "问题"}
    ]

def get_user_info():
    """返回用户信息"""
    return {
        "name": "用户名称",
        "email": "user@example.com",
        "role": "管理员",
        "department": "技术部"
    }

def get_kanban_columns():
    """返回看板列数据"""
    return [
        {
            "title": "待处理",
            "cards": [
                {"title": "登录页面样式调整", "description": "调整登录页面的UI样式", "priority": "高"},
                {"title": "API 接口优化", "description": "优化API响应速度", "priority": "中"}
            ]
        },
        {
            "title": "进行中",
            "cards": [
                {"title": "用户权限管理", "description": "实现基于角色的权限控制", "priority": "高"},
                {"title": "数据库备份脚本", "description": "编写自动化备份脚本", "priority": "低"}
            ]
        },
        {
            "title": "已完成",
            "cards": [
                {"title": "首页重构", "description": "使用新框架重构首页", "priority": "中"},
                {"title": "单元测试覆盖", "description": "为核心模块添加单元测试", "priority": "低"}
            ]
        }
    ]

def toggle_theme(current_theme):
    """
    切换主题
    :param current_theme: 当前主题，'light' 或 'dark'
    :return: 切换后的主题
    """
    if current_theme == 'light':
        return 'dark'
    return 'light'

def validate_theme(theme):
    """
    验证主题是否有效
    :param theme: 主题名称
    :return: 布尔值
    """
    return theme in ('light', 'dark')