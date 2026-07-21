# 番茄时钟-LOOP

一个基于 Flask 的番茄时钟管理 Web 应用，提供番茄时钟的列表展示、详情查看和 JSON API 接口。

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
│   └── tomatoes.json       # 番茄时钟数据文件
├── templates/
│   ├── base.html           # 基础模板
│   ├── list.html           # 列表页模板
│   └── detail.html         # 详情页模板
├── static/
│   ├── css/
│   │   └── style.css       # 样式文件
│   ├── js/
│   │   └── main.js         # JavaScript 文件
│   └── img/                # 图片目录
└── tests/
    └── test_app.py         # 单元测试
```

## 接口列表

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | / | 列表页 |
| GET | /tomato/<id> | 详情页 |
| GET | /api/tomatoes | JSON 列表接口 |
| GET | /api/tomatoes/<id> | JSON 详情接口 |