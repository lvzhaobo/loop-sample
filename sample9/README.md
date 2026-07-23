# 番茄时钟-LOOP

一个基于 Flask 的单页番茄时钟交互工具，支持工作/休息时段循环计时。

## 运行方式

```bash
pip install -r requirements.txt
python app.py
```

服务默认监听 5000 端口，可通过 `PORT` 环境变量修改。

## 目录结构

```
.
├── app.py                  # Flask 入口
├── pomodoro_core.py        # 纯逻辑模块（计时状态管理、时段切换、循环计数）
├── requirements.txt        # 依赖清单
├── README.md               # 本文件
├── templates/
│   └── index.html          # 首页模板
├── static/
│   ├── css/
│   │   └── style.css       # 样式文件
│   └── js/
│       └── pomodoro.js     # 前端交互脚本
└── tests/
    └── test_pomodoro_core.py  # 单元测试
```

## 接口列表

| 路由 | 方法 | 说明 |
|------|------|------|
| `/`  | GET  | 渲染番茄时钟首页 |