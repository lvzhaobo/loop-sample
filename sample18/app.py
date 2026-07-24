import os
import sys
import json
import logging
from flask import Flask, render_template, jsonify, request

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 将项目根目录加入 sys.path，确保导入模块正常
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from course_core import load_courses, get_course_by_id, update_progress

app = Flask(__name__)

# 数据文件路径
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.json')

@app.route('/')
def index():
    """渲染首页"""
    return render_template('index.html')

@app.route('/api/courses')
def api_courses():
    """获取课程列表（JSON 数组）"""
    try:
        courses = load_courses(DATA_FILE)
        return jsonify(courses)
    except Exception as e:
        logger.error(f"加载课程列表失败: {e}")
        return jsonify({"error": "无法加载课程数据"}), 500

@app.route('/api/courses/<int:course_id>')
def api_course_detail(course_id):
    """获取单个课程详情"""
    try:
        course = get_course_by_id(DATA_FILE, course_id)
        if course is None:
            return jsonify({"error": "课程不存在"}), 404
        return jsonify(course)
    except Exception as e:
        logger.error(f"获取课程详情失败: {e}")
        return jsonify({"error": "无法加载课程数据"}), 500

@app.route('/api/progress', methods=['POST'])
def api_update_progress():
    """更新学习进度"""
    try:
        data = request.get_json()
        if not data or 'course_id' not in data or 'chapter_id' not in data:
            return jsonify({"error": "缺少必要参数"}), 400
        course_id = int(data['course_id'])
        chapter_id = data['chapter_id']
        completed = data.get('completed', True)
        result = update_progress(DATA_FILE, course_id, chapter_id, completed)
        if result:
            return jsonify({"status": "ok"})
        else:
            return jsonify({"error": "课程或章节不存在"}), 404
    except (ValueError, TypeError):
        return jsonify({"error": "参数格式错误"}), 400
    except Exception as e:
        logger.error(f"更新进度失败: {e}")
        return jsonify({"error": "更新进度失败"}), 500

@app.errorhandler(404)
def not_found(e):
    """404 错误处理"""
    return jsonify({"error": "资源不存在"}), 404

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(host='0.0.0.0', port=PORT, debug=debug_mode)