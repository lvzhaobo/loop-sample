# 在线学习平台

一个基于 Flask 的在线学习平台，提供课程浏览和详情查看功能。

## 运行方式

1. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

2. 启动服务：
   ```
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
│   └── js/main.js          # JavaScript 文件
└── tests/
    └── test_app.py         # 单元测试
```

## 接口列表

| 路径 | 方法 | 说明 |
|------|------|------|
| `/` | GET | 课程列表页 |
| `/course/<id>` | GET | 课程详情页 |
| `/api/courses` | GET | 课程列表 JSON 接口 |
| `/api/courses/<id>` | GET | 课程详情 JSON 接口 |