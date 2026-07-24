# 复刻Jira系统

本项目是一个轻量级的Jira任务管理系统复刻，基于Flask框架，使用JSON文件存储数据，提供任务列表展示、详情查看及JSON API接口。

## 运行方式

1. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

2. 启动服务：
   ```
   python app.py
   ```
   服务默认运行在5000端口，可通过环境变量`PORT`自定义端口。

## 目录结构

```
.
├── app.py                  # Flask应用入口，包含所有路由
├── requirements.txt        # Python依赖
├── README.md               # 项目说明文档
├── data/
│   └── fs_009_items.json   # 任务数据文件
├── templates/
│   ├── base.html           # 基础模板
│   ├── list.html           # 列表页模板
│   └── detail.html         # 详情页模板
├── static/
│   ├── css/style.css       # 样式文件
│   └── js/main.js          # JavaScript文件
└── tests/
    └── test_app.py         # 单元测试
```

## 提供的接口

| 名称 | 路径 | 说明 |
| --- | --- | --- |
| 首页 | `/` | 渲染任务列表页面 |
| 详情页 | `/fs_009_item/<id>` | 渲染单个任务详情页面 |
| JSON列表 | `/api/fs_009_items` | 返回所有任务的JSON数组 |
| JSON详情 | `/api/fs_009_items/<id>` | 返回单个任务的JSON对象 |