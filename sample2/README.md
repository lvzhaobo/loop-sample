# 在线学习平台:课程列表 + 详情

一个基于 Flask 的在线学习平台，提供课程列表浏览和课程详情查看功能。

## 运行方式

```bash
pip install -r requirements.txt
python app.py
```

服务默认运行在 http://localhost:5000，可通过环境变量 `PORT` 修改端口。

## 目录结构

```
.
├── app.py                 # Flask 应用入口
├── requirements.txt       # 依赖清单
├── README.md              # 项目说明
├── data/
│   └── courses.json       # 课程数据文件
├── templates/
│   ├── base.html          # 基础模板
│   ├── list.html          # 课程列表页
│   └── detail.html        # 课程详情页
├── static/
│   ├── css/
│   │   └── style.css      # 样式文件
│   ├── js/
│   │   └── main.js        # JavaScript 文件
│   └── img/               # 课程封面图片
└── tests/
    └── test_app.py        # 单元测试
```

## 接口列表

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | / | 课程列表页(HTML) |
| GET | /course/<id> | 课程详情页(HTML) |
| GET | /api/courses | 课程列表(JSON) |
| GET | /api/courses/<id> | 课程详情(JSON) |