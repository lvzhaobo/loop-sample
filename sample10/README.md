# 在线学习平台课程管理

一个基于 Flask 的在线学习平台课程管理 Web 应用，提供课程列表浏览、详情查看及 JSON API 接口。

## 运行方式

1. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

2. 启动应用：
   ```
   python app.py
   ```

   默认监听端口 5000，可通过环境变量 `PORT` 修改。

## 目录结构

```
.
├── app.py                  # Flask 应用入口
├── requirements.txt        # 依赖清单
├── README.md               # 项目说明
├── data/
│   └── courses.json        # 课程数据文件
├── templates/
│   ├── base.html           # 基础模板
│   ├── list.html           # 课程列表页
│   ├── detail.html         # 课程详情页
│   └── 404.html            # 404 页面
├── static/
│   ├── css/
│   │   └── style.css       # 样式文件
│   └── js/
│       └── main.js         # JavaScript 文件
└── tests/
    └── test_app.py         # 单元测试
```

## 接口列表

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | / | 课程列表页 |
| GET | /course/<id> | 课程详情页 |
| GET | /api/courses | 返回所有课程 JSON 数组 |
| GET | /api/courses/<id> | 返回单个课程 JSON 对象 |