"""
暑假生活学习平台 - 纯逻辑模块
包含暑假活动数据与日期计算的纯函数，无副作用，便于单元测试。
"""

from datetime import date, timedelta

# 暑假活动数据（2026年暑假）
_ACTIVITIES = [
    {
        "id": 1,
        "title": "语文阅读",
        "type": "学习",
        "date": "2026-07-01",
        "description": "阅读《西游记》儿童版，写一篇读后感",
        "icon": "📖"
    },
    {
        "id": 2,
        "title": "数学练习",
        "type": "学习",
        "date": "2026-07-03",
        "description": "完成20道加减乘除混合运算",
        "icon": "🧮"
    },
    {
        "id": 3,
        "title": "游泳课",
        "type": "运动",
        "date": "2026-07-05",
        "description": "学习蛙泳基本动作，练习换气",
        "icon": "🏊"
    },
    {
        "id": 4,
        "title": "公园游玩",
        "type": "游玩",
        "date": "2026-07-08",
        "description": "去植物园看荷花，认识不同植物",
        "icon": "🌳"
    },
    {
        "id": 5,
        "title": "踢足球",
        "type": "运动",
        "date": "2026-07-10",
        "description": "和小伙伴在小区球场踢球",
        "icon": "⚽"
    },
    {
        "id": 6,
        "title": "打羽毛球",
        "type": "运动",
        "date": "2026-07-12",
        "description": "和爸爸一起打羽毛球，练习发球",
        "icon": "🏸"
    },
    {
        "id": 7,
        "title": "英语绘本",
        "type": "学习",
        "date": "2026-07-15",
        "description": "阅读英语绘本《The Very Hungry Caterpillar》",
        "icon": "📚"
    },
    {
        "id": 8,
        "title": "游泳进阶",
        "type": "运动",
        "date": "2026-07-18",
        "description": "练习自由泳打腿，游完25米",
        "icon": "🏊"
    },
    {
        "id": 9,
        "title": "科技馆之旅",
        "type": "游玩",
        "date": "2026-07-20",
        "description": "参观科技馆，体验互动展品",
        "icon": "🔬"
    },
    {
        "id": 10,
        "title": "画画时间",
        "type": "学习",
        "date": "2026-07-22",
        "description": "用水彩画一幅夏天的风景画",
        "icon": "🎨"
    }
]


def get_activities():
    """
    返回所有暑假活动列表。
    返回一个列表，每个元素是包含 id、title、type、date、description、icon 的字典。
    """
    return _ACTIVITIES.copy()


def get_activity_by_id(activity_id):
    """
    根据活动 ID 返回单个活动字典，如果不存在则返回 None。
    """
    for activity in _ACTIVITIES:
        if activity["id"] == activity_id:
            return activity.copy()
    return None


def get_summer_dates(year=2026):
    """
    返回指定年份暑假的起止日期。
    暑假定义为 7月1日 到 8月31日。
    返回 (start_date, end_date) 元组，均为 date 对象。
    """
    start_date = date(year, 7, 1)
    end_date = date(year, 8, 31)
    return start_date, end_date


def get_activities_by_type(activity_type):
    """
    根据活动类型（如"学习"、"运动"、"游玩"）筛选活动列表。
    返回匹配的活动列表。
    """
    return [a.copy() for a in _ACTIVITIES if a["type"] == activity_type]


def get_activities_count():
    """
    返回活动总数。
    """
    return len(_ACTIVITIES)