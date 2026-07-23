import os
import json
import logging
from flask import Flask, render_template, abort

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'courses.json')
PORT = int(os.environ.get("PORT", 5000))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_courses():
    """加载课程数据，返回课程列表"""
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            courses = json.load(f)
        return courses
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"数据文件加载失败: {e}")
        return []

@app.route('/')
def course_list():
    """课程列表页"""
    courses = load_courses()
    return render_template('list.html', courses=courses)

@app.route('/course/<int:course_id>')
def course_detail(course_id):
    """课程详情页"""
    courses = load_courses()
    course = next((c for c in courses if c['id'] == course_id), None)
    if course is None:
        abort(404)
    return render_template('detail.html', course=course)

@app.route('/api/courses')
def api_courses():
    """返回所有课程 JSON 列表"""
    courses = load_courses()
    return courses

@app.route('/api/courses/<int:course_id>')
def api_course_detail(course_id):
    """返回单个课程 JSON 详情"""
    courses = load_courses()
    course = next((c for c in courses if c['id'] == course_id), None)
    if course is None:
        return {"error": "课程不存在"}, 404
    return course

@app.errorhandler(404)
def not_found(error):
    """404 错误处理"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)