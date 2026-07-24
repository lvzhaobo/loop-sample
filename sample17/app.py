import os
import json
import logging
from flask import Flask, render_template, abort

# 常量定义
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'fs_009_items.json')
PORT = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

# 日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def load_fs_009_items():
    """加载数据文件中的fs_009_item列表"""
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            logger.error("数据文件格式错误：应为JSON数组")
            return []
        logger.info("成功加载 %d 条fs_009_item", len(data))
        return data
    except FileNotFoundError:
        logger.error("数据文件未找到: %s", DATA_PATH)
        return []
    except json.JSONDecodeError:
        logger.error("数据文件JSON解析失败: %s", DATA_PATH)
        return []


@app.route('/')
def fs_009_item_list():
    """列表页路由：渲染所有fs_009_item的卡片列表"""
    items = load_fs_009_items()
    return render_template('list.html', items=items)


@app.route('/fs_009_item/<int:item_id>')
def fs_009_item_detail(item_id):
    """详情页路由：根据id渲染单个fs_009_item详情"""
    items = load_fs_009_items()
    item = next((i for i in items if i['id'] == item_id), None)
    if item is None:
        abort(404)
    return render_template('detail.html', item=item)


@app.route('/api/fs_009_items')
def api_fs_009_items():
    """JSON接口：返回所有fs_009_item的列表（裸数组）"""
    items = load_fs_009_items()
    return app.response_class(
        response=json.dumps(items, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )


@app.route('/api/fs_009_items/<int:item_id>')
def api_fs_009_item_detail(item_id):
    """JSON接口：根据id返回单个fs_009_item"""
    items = load_fs_009_items()
    item = next((i for i in items if i['id'] == item_id), None)
    if item is None:
        return app.response_class(
            response=json.dumps({"error": "Item not found"}, ensure_ascii=False),
            status=404,
            mimetype='application/json'
        )
    return app.response_class(
        response=json.dumps(item, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )


@app.errorhandler(404)
def not_found(error):
    """404错误处理：返回404页面"""
    return render_template('detail.html', item=None), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)