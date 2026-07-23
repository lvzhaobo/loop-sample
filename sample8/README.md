# 番茄时钟-LOOP

一个基于 Flask 的番茄时钟（Pomodoro Timer）单页交互工具，白色背景、番茄红色调，页面固定显示 "Loop-20260721" 字样。

## 功能

- 启动/暂停/重置番茄时钟计时（默认25分钟工作时段，5分钟休息时段）
- 实时显示剩余时间（分钟:秒格式）
- 计时结束时触发视觉提示

## 运行方式

```bash
pip install -r requirements.txt
python app.py
```

服务默认监听 5000 端口，可通过环境变量 `PORT` 修改。

## 目录结构

```
.
├── app.py                  # Flask 入口
├── pomodoro_core.py        # 纯逻辑模块（计时状态管理、时间计算）
├── requirements.txt        # 依赖列表
├── README.md               # 本文件
├── templates/
│   └── index.html          # 首页模板
├── static/
│   ├── css/
│   │   └── style.css       # 样式文件
│   └── js/
│       └── pomodoro.js     # 前端交互脚本
└── tests/
    └── test_pomodoro.py    # 单元测试
```

## 接口列表

- `GET /` - 渲染番茄时钟首页