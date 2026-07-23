import os
import json
import logging
from flask import Flask, render_template, abort, jsonify

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'sort_visuals.json')
PORT = int(os.environ.get("PORT", 5000))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_sort_visuals():
    """加载排序算法数据"""
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error("数据文件加载失败: %s", e)
        return []


@app.route('/')
def sort_visual_list():
    """列表页路由"""
    visuals = load_sort_visuals()
    return render_template('list.html', visuals=visuals)


@app.route('/sort_visual/<int:visual_id>')
def sort_visual_detail(visual_id):
    """详情页路由"""
    visuals = load_sort_visuals()
    visual = next((v for v in visuals if v['id'] == visual_id), None)
    if visual is None:
        abort(404)
    return render_template('detail.html', visual=visual)


@app.route('/api/sort_visuals')
def api_sort_visuals():
    """JSON列表接口"""
    visuals = load_sort_visuals()
    return jsonify(visuals)


@app.route('/api/sort_visuals/<int:visual_id>')
def api_sort_visual_detail(visual_id):
    """JSON详情接口"""
    visuals = load_sort_visuals()
    visual = next((v for v in visuals if v['id'] == visual_id), None)
    if visual is None:
        return jsonify({"error": "资源不存在"}), 404
    return jsonify(visual)


@app.errorhandler(404)
def not_found(error):
    """404错误处理"""
    return render_template('base.html', error="页面未找到"), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)