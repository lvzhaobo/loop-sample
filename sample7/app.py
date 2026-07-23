import os
import json
import logging
from flask import Flask, render_template, abort

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'tomatoes.json')
PORT = int(os.environ.get("PORT", 5000))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_tomatoes():
    """加载番茄时钟数据"""
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error("数据文件加载失败: %s", e)
        return []

@app.route('/')
def tomato_list():
    """列表页"""
    tomatoes = load_tomatoes()
    return render_template('list.html', tomatoes=tomatoes)

@app.route('/tomato/<int:tomato_id>')
def tomato_detail(tomato_id):
    """详情页"""
    tomatoes = load_tomatoes()
    tomato = next((t for t in tomatoes if t['id'] == tomato_id), None)
    if tomato is None:
        abort(404)
    return render_template('detail.html', tomato=tomato)

@app.route('/api/tomatoes')
def api_tomatoes():
    """JSON 列表"""
    tomatoes = load_tomatoes()
    return tomatoes

@app.route('/api/tomatoes/<int:tomato_id>')
def api_tomato_detail(tomato_id):
    """JSON 详情"""
    tomatoes = load_tomatoes()
    tomato = next((t for t in tomatoes if t['id'] == tomato_id), None)
    if tomato is None:
        return {"error": "Tomato not found"}, 404
    return tomato

@app.errorhandler(404)
def not_found(e):
    """404 页面"""
    return render_template('detail.html', tomato=None), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)