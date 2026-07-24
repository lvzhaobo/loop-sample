# 在线学习平台

一个基于 Flask 的在线学习平台，提供课程内容浏览与学习进度管理功能。

## 运行方式

```bash
pip install -r requirements.txt
python app.py
```

服务启动后，访问 http://localhost:5000 即可使用。

## 目录结构

```
.
├── app.py                 # Flask 应用入口
├── course_core.py         # 核心业务逻辑模块
├── data.json              # 课程与进度数据文件
├── requirements.txt       # Python 依赖
├── README.md              # 本文件
├── templates/
│   └── index.html         # 首页模板
├── static/
│   ├── css/
│   │   └── style.css      # 样式文件
│   └── js/
│       └── main.js        # 前端交互脚本
└── tests/
    └── test_course_core.py # 单元测试
```

## 接口列表

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/` | 首页，渲染课程列表页面 |
| GET | `/api/courses` | 获取所有课程列表（JSON 数组） |
| GET | `/api/courses/<id>` | 获取单个课程详情 |
| POST | `/api/progress` | 更新学习进度（需传入 course_id, chapter_id, completed） |