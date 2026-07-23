import os
import sys
import logging
from flask import Flask, render_template

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# 从环境变量读取端口，默认5000
PORT = int(os.environ.get("PORT", 5000))

# 生产环境禁止debug模式
DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"

@app.route('/')
def index():
    """渲染番茄时钟首页"""
    return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
    """404错误处理"""
    return render_template('index.html'), 404

if __name__ == '__main__':
    logger.info(f"Starting Pomodoro Timer on port {PORT}, debug={DEBUG}")
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)