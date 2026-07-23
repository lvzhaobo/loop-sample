# 番茄时钟-LOOP

一个基于 Flask 的番茄时钟管理 Web 应用，提供番茄时钟的列表展示、详情查看及 JSON API 接口。

## 运行方式

1. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

2. 启动应用：
   ```
   python app.py
   ```

   默认端口为 5000，可通过环境变量 `PORT` 修改。

## 目录结构

```
.
├── app.py                  # Flask 入口，包含全部路由
├── requirements.txt        # 依赖清单
├── README.md               # 项目说明
├── data/
│   └── tomatoes.json       # 番茄时钟数据文件
├── templates/
│   ├── base.html           # 基础模板
│   ├── list.html           # 列表页
│   └── detail.html         # 详情页
├── static/
│   ├── css/style.css       # 样式文件
│   └── js/main.js          # JavaScript 文件
└── tests/
    └── test_app.py         # 单元测试
```

## 接口列表

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | / | 番茄时钟列表页 |
| GET | /tomato/<id> | 番茄时钟详情页 |
| GET | /api/tomatoes | JSON 番茄时钟列表 |
| GET | /api/tomatoes/<id> | JSON 番茄时钟详情 |