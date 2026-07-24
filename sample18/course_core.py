"""
课程核心逻辑模块 - 纯函数实现，便于单元测试
"""
import json
import os
import logging

logger = logging.getLogger(__name__)


def load_courses(data_file):
    """
    从 JSON 文件加载课程列表。
    返回课程列表（list），失败时返回空列表。
    """
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('courses', [])
    except (FileNotFoundError, json.JSONDecodeError, IOError) as e:
        logger.error(f"加载课程数据失败: {e}")
        return []


def get_course_by_id(data_file, course_id):
    """
    根据课程 ID 获取单个课程详情。
    返回课程对象（dict），不存在时返回 None。
    """
    courses = load_courses(data_file)
    for course in courses:
        if course.get('id') == course_id:
            return course
    return None


def update_progress(data_file, course_id, chapter_id, completed=True):
    """
    更新指定课程中某个章节的学习进度。
    返回 True 表示更新成功，False 表示课程或章节不存在。
    """
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, IOError) as e:
        logger.error(f"读取数据文件失败: {e}")
        return False

    courses = data.get('courses', [])
    for course in courses:
        if course.get('id') == course_id:
            chapters = course.get('chapters', [])
            # 检查章节是否存在
            chapter_ids = [ch.get('id') for ch in chapters]
            if chapter_id not in chapter_ids:
                return False
            # 初始化进度字典
            if 'progress' not in course:
                course['progress'] = {}
            course['progress'][chapter_id] = completed
            # 写回文件
            try:
                with open(data_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                return True
            except IOError as e:
                logger.error(f"写入数据文件失败: {e}")
                return False

    return False


def get_course_progress(data_file, course_id):
    """
    获取指定课程的学习进度字典。
    返回进度字典，课程不存在时返回 None。
    """
    course = get_course_by_id(data_file, course_id)
    if course is None:
        return None
    return course.get('progress', {})