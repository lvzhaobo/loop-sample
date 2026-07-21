import os
import json
import logging
from flask import Flask, render_template, abort

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'tomatoes.json')
PORT = int(os.environ.get("PORT", 5000))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 唯一的数据加载函数
def load_tomatoes():
    """加载番茄时钟数据"""
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        logger.error("数据文件未找到: %s", DATA_PATH)
        return []
    except json.JSONDecodeError:
        logger.error("数据文件解析失败: %s", DATA_PATH)
        return []

@app.route('/')
def tomato_list():
    """列表页路由"""
    tomatoes = load_tomatoes()
    return render_template('list.html', tomatoes=tomatoes)

@app.route('/tomato/<int:tomato_id>')
def tomato_detail(tomato_id):
    """详情页路由"""
    tomatoes = load_tomatoes()
    tomato = next((t for t in tomatoes if t['id'] == tomato_id), None)
    if tomato is None:
        abort(404)
    return render_template('detail.html', tomato=tomato)

@app.route('/api/tomatoes')
def api_tomatoes():
    """JSON 列表接口"""
    tomatoes = load_tomatoes()
    return app.response_class(
        response=json.dumps(tomatoes, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )

@app.route('/api/tomatoes/<int:tomato_id>')
def api_tomato_detail(tomato_id):
    """JSON 详情接口"""
    tomatoes = load_tomatoes()
    tomato = next((t for t in tomatoes if t['id'] == tomato_id), None)
    if tomato is None:
        return app.response_class(
            response=json.dumps({"error": "Tomato not found"}, ensure_ascii=False),
            status=404,
            mimetype='application/json'
        )
    return app.response_class(
        response=json.dumps(tomato, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )

@app.errorhandler(404)
def not_found(error):
    """404 错误处理"""
    return render_template('detail.html', tomato=None), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)