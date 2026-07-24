import os
import sys
import logging
from flask import Flask, render_template, jsonify

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# 从环境变量读取端口
PORT = int(os.environ.get("PORT", 5000))

# 生产环境关闭 debug
DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"

# 导入纯逻辑模块
from jira_core import get_menus, get_user_info, get_kanban_columns

@app.route("/")
def index():
    """渲染首页"""
    return render_template("index.html")

@app.route("/api/menus")
def api_menus():
    """返回菜单数据 JSON"""
    try:
        menus = get_menus()
        return jsonify(menus)
    except Exception as e:
        logger.error(f"获取菜单数据失败: {e}")
        return jsonify({"error": "获取菜单数据失败"}), 500

@app.route("/api/user")
def api_user():
    """返回用户信息 JSON"""
    try:
        user = get_user_info()
        return jsonify(user)
    except Exception as e:
        logger.error(f"获取用户信息失败: {e}")
        return jsonify({"error": "获取用户信息失败"}), 500

@app.route("/api/kanban")
def api_kanban():
    """返回看板数据 JSON"""
    try:
        columns = get_kanban_columns()
        return jsonify(columns)
    except Exception as e:
        logger.error(f"获取看板数据失败: {e}")
        return jsonify({"error": "获取看板数据失败"}), 500

@app.errorhandler(404)
def not_found(e):
    """404 错误处理"""
    return jsonify({"error": "资源不存在"}), 404

if __name__ == "__main__":
    logger.info(f"启动服务，端口: {PORT}")
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)