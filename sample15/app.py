import os
import logging
from flask import Flask, render_template

app = Flask(__name__)

# 日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    """渲染暑假生活学习平台首页"""
    logger.info("访问首页 /")
    return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
    """404 错误处理"""
    return render_template('index.html'), 404

if __name__ == '__main__':
    PORT = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=PORT, debug=debug_mode)