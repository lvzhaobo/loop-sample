import os
import json
import logging
from flask import Flask, render_template, abort, jsonify

# 常量定义
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'courses.json')
PORT = int(os.environ.get("PORT", 5000))

# 日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# 唯一的数据加载函数
def load_courses():
    """加载课程数据，返回课程列表"""
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            courses = json.load(f)
        logger.info(f"成功加载 {len(courses)} 门课程")
        return courses
    except FileNotFoundError:
        logger.error(f"数据文件未找到: {DATA_PATH}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"JSON 解析错误: {e}")
        return []

# 首页 - 课程列表页
@app.route('/')
def course_list():
    """渲染课程列表页"""
    courses = load_courses()
    return render_template('list.html', courses=courses)

# 课程详情页
@app.route('/course/<int:id>')
def course_detail(id):
    """渲染课程详情页，id 不存在返回 404"""
    courses = load_courses()
    course = next((c for c in courses if c['id'] == id), None)
    if course is None:
        abort(404)
    return render_template('detail.html', course=course)

# JSON 课程列表
@app.route('/api/courses')
def api_courses():
    """返回课程列表 JSON"""
    courses = load_courses()
    return jsonify(courses)

# JSON 课程详情
@app.route('/api/courses/<int:id>')
def api_course_detail(id):
    """返回单个课程 JSON，不存在返回 404"""
    courses = load_courses()
    course = next((c for c in courses if c['id'] == id), None)
    if course is None:
        return jsonify({"error": "course not found"}), 404
    return jsonify(course)

# 404 错误处理
@app.errorhandler(404)
def not_found(error):
    """处理 404 错误"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)