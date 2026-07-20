# 在线学习平台

一个基于 Flask 的在线学习平台，提供课程浏览与查询功能。

## 运行方式

```bash
pip install -r requirements.txt
python app.py
```

服务默认运行在 5000 端口，可通过环境变量 `PORT` 修改。

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
│   └── detail.html         # 课程详情页
├── static/
│   ├── css/style.css       # 样式文件
│   ├── js/main.js          # JavaScript 文件
│   └── img/                # 图片资源
└── tests/
    └── test_app.py         # 单元测试
```

## 接口列表

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | / | 课程列表页 |
| GET | /course/<id> | 课程详情页 |
| GET | /api/courses | 课程列表 API |
| GET | /api/courses/<id> | 课程详情 API |