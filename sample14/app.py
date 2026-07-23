import os
import json
import logging
from flask import Flask, render_template, abort, jsonify

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 常量定义
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'fs_006s.json')
PORT = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

# 唯一的数据加载函数
def load_fs_006s():
    """加载 fs_006s.json 数据文件"""
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logger.info("成功加载数据文件，共 %d 条记录", len(data))
        return data
    except FileNotFoundError:
        logger.error("数据文件未找到: %s", DATA_PATH)
        return []
    except json.JSONDecodeError as e:
        logger.error("数据文件解析失败: %s", e)
        return []

# 首页路由 - 列表页
@app.route('/')
def fs_006_list():
    """渲染暑假生活学习活动列表页"""
    items = load_fs_006s()
    return render_template('list.html', items=items)

# 详情页路由
@app.route('/fs_006/<int:item_id>')
def fs_006_detail(item_id):
    """渲染单个活动详情页"""
    items = load_fs_006s()
    item = next((i for i in items if i['id'] == item_id), None)
    if item is None:
        abort(404)
    return render_template('detail.html', item=item)

# JSON API - 列表
@app.route('/api/fs_006s')
def api_fs_006s():
    """返回所有活动的 JSON 数组"""
    items = load_fs_006s()
    return jsonify(items)

# JSON API - 详情
@app.route('/api/fs_006s/<int:item_id>')
def api_fs_006_detail(item_id):
    """返回单个活动的 JSON 对象"""
    items = load_fs_006s()
    item = next((i for i in items if i['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "活动不存在"}), 404
    return jsonify(item)

# 404 错误处理
@app.errorhandler(404)
def not_found(error):
    """处理 404 错误"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)