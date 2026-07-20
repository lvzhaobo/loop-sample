import os
import json
from flask import Flask, render_template, jsonify, abort

app = Flask(__name__)
DATA_PATH = os.path.join(os.path.dirname(__file__), "data/courses.json")
PORT = int(os.environ.get("PORT", 5000))

def load_courses():
    """唯一数据读取入口。"""
    try:
        with open(DATA_PATH, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        app.logger.error("数据加载失败: %s", e)
        return []

def _find(items, id):
    """按 id 查找单条。"""
    for it in items:
        if it.get("id") == id:
            return it
    return None

@app.route("/")
def course_list():
    """列表页。"""
    return render_template("list.html", items=load_courses())

@app.route("/course/<int:id>")
def course_detail(id):
    """详情页,不存在返回 404。"""
    item = _find(load_courses(), id)
    if item is None:
        abort(404)
    return render_template("detail.html", item=item)

@app.route("/api/courses")
def api_courses():
    """JSON 列表。"""
    return jsonify(load_courses())

@app.route("/api/courses/<int:id>")
def api_course_detail(id):
    """JSON 详情,不存在返回 404。"""
    item = _find(load_courses(), id)
    if item is None:
        return jsonify({"error": "course not found"}), 404
    return jsonify(item)

@app.errorhandler(404)
def not_found(e):
    """统一 404 页。"""
    return render_template("base.html", not_found=True), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
