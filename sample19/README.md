# 复刻Jira系统

## 项目简介
一个模仿Jira风格的单页交互式Web工具，包含Landing Page、控制台（左侧菜单+右侧Kanban看板）及用户头像详情，支持深色/浅色主题切换。

## 运行方式
```bash
pip install -r requirements.txt
python app.py
```
服务默认运行在 http://localhost:5000

## 目录结构
```
.
├── app.py                  # Flask 入口
├── jira_core.py            # 纯逻辑模块（主题、菜单、用户数据管理）
├── requirements.txt        # 依赖列表
├── README.md               # 本文件
├── templates/
│   └── index.html          # 首页模板
├── static/
│   ├── css/
│   │   └── style.css       # 样式文件（含浅色/深色主题）
│   └── js/
│       └── jira.js         # 前端交互逻辑
└── tests/
    └── test_jira_core.py   # 单元测试
```

## 接口列表
| 路由 | 方法 | 说明 |
|------|------|------|
| `/` | GET | 渲染首页 |
| `/api/menus` | GET | 返回菜单数据 JSON |
| `/api/user` | GET | 返回用户信息 JSON |
| `/api/kanban` | GET | 返回看板数据 JSON |