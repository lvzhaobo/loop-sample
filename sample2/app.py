import os
import json
import logging
from flask import Flask, render_template, abort

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 常量定义
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'courses.json')
PORT = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

def load_courses():
    """加载课程数据"""
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            courses = json.load(f)
        logger.info(f"成功加载 {len(courses)} 门课程")
        return courses
    except FileNotFoundError:
        logger.error(f"数据文件未找到: {DATA_PATH}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"JSON 解析失败: {e}")
        return []

@app.route('/')
def course_list():
    """课程列表页"""
    courses = load_courses()
    return render_template('list.html', courses=courses)

@app.route('/course/<int:id>')
def course_detail(id):
    """课程详情页"""
    courses = load_courses()
    course = next((c for c in courses if c['id'] == id), None)
    if course is None:
        abort(404)
    return render_template('detail.html', course=course)

@app.route('/api/courses')
def api_courses():
    """课程列表 JSON 接口"""
    courses = load_courses()
    return courses

@app.route('/api/courses/<int:id>')
def api_course_detail(id):
    """课程详情 JSON 接口"""
    courses = load_courses()
    course = next((c for c in courses if c['id'] == id), None)
    if course is None:
        return {"error": "course not found"}, 404
    return course

@app.errorhandler(404)
def not_found(error):
    """404 错误处理"""
    return render_template('detail.html', course=None), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)