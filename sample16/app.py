import os
import json
import logging
from flask import Flask, render_template, abort

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'activities.json')
PORT = int(os.environ.get("PORT", 5000))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 唯一的数据加载函数
def load_activities():
    """加载活动数据"""
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("数据格式错误，应为列表")
        return data
    except FileNotFoundError:
        logger.error("数据文件未找到: %s", DATA_PATH)
        return []
    except json.JSONDecodeError as e:
        logger.error("JSON解析失败: %s", e)
        return []
    except Exception as e:
        logger.error("加载数据时出错: %s", e)
        return []

# 首页路由 - 活动列表
@app.route('/')
def activity_list():
    """显示活动列表页"""
    activities = load_activities()
    return render_template('list.html', activities=activities)

# 活动详情页
@app.route('/activity/<int:activity_id>')
def activity_detail(activity_id):
    """显示单个活动详情"""
    activities = load_activities()
    activity = next((a for a in activities if a['id'] == activity_id), None)
    if activity is None:
        abort(404)
    return render_template('detail.html', activity=activity)

# JSON API - 活动列表
@app.route('/api/activities')
def api_activities():
    """返回活动列表JSON"""
    activities = load_activities()
    return app.response_class(
        response=json.dumps(activities, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )

# JSON API - 单个活动详情
@app.route('/api/activities/<int:activity_id>')
def api_activity_detail(activity_id):
    """返回单个活动JSON"""
    activities = load_activities()
    activity = next((a for a in activities if a['id'] == activity_id), None)
    if activity is None:
        return app.response_class(
            response=json.dumps({"error": "活动未找到"}, ensure_ascii=False),
            status=404,
            mimetype='application/json'
        )
    return app.response_class(
        response=json.dumps(activity, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )

# 404错误处理
@app.errorhandler(404)
def not_found(error):
    """处理404错误"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)