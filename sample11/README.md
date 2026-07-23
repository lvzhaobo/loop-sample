# 排序算法可视化展示页面

本项目是一个排序算法可视化展示页面，提供排序算法的列表浏览和详情查看功能。

## 运行方式

1. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

2. 启动服务：
   ```
   python app.py
   ```

3. 访问 http://localhost:5000

## 目录结构

```
.
├── app.py                  # Flask 入口，包含全部路由
├── requirements.txt        # 依赖清单
├── README.md               # 项目说明
├── data/
│   └── sort_visuals.json   # 排序算法数据文件
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
| GET | / | 列表页 |
| GET | /sort_visual/<id> | 详情页 |
| GET | /api/sort_visuals | JSON 列表接口 |
| GET | /api/sort_visuals/<id> | JSON 详情接口 |