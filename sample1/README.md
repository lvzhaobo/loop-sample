# 在线学习平台：课程列表 + 详情

一个基于 Flask 的在线学习平台，提供课程列表和详情展示功能。

## 运行方式

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 启动服务：
   ```bash
   python app.py
   ```

   服务默认运行在端口 5000，可通过环境变量 `PORT` 修改。

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
│   └── 404.html            # 404 错误页
├── static/
│   ├── css/
│   │   └── style.css       # 样式文件
│   ├── js/
│   │   └── main.js         # JavaScript 文件
│   └── img/                # 图片资源目录
└── tests/
    └── test_app.py         # 单元测试
```

## 接口列表

| 名称               | 路径                | 说明               |
|--------------------|---------------------|--------------------|
| 课程列表页         | GET /               | 返回 HTML 页面     |
| 课程详情页         | GET /course/<id>    | 返回 HTML 页面     |
| 课程列表 JSON      | GET /api/courses    | 返回 JSON 数组     |
| 课程详情 JSON      | GET /api/courses/<id> | 返回 JSON 对象   |