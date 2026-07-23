# 沐然沐橦暑假生活学习平台

本项目是一个展示沐然沐橦暑假生活学习活动的 Web 平台，提供活动列表浏览、详情查看及 JSON API 接口。

## 运行方式

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 启动服务：
   ```bash
   python app.py
   ```

   服务默认运行在 `http://localhost:5000`，可通过环境变量 `PORT` 修改端口。

## 目录结构

```
.
├── app.py                  # Flask 应用入口
├── requirements.txt        # 依赖清单
├── README.md               # 项目说明
├── data/
│   └── fs_006s.json        # 活动数据文件
├── templates/
│   ├── base.html           # 基础模板
│   ├── list.html           # 列表页模板
│   ├── detail.html         # 详情页模板
│   └── 404.html            # 404 错误页模板
├── static/
│   ├── css/style.css       # 样式文件
│   └── js/main.js          # JavaScript 文件
└── tests/
    └── test_app.py         # 单元测试
```

## 接口列表

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/` | 首页，显示活动列表 |
| GET | `/fs_006/<id>` | 活动详情页 |
| GET | `/api/fs_006s` | JSON 格式的活动列表 |
| GET | `/api/fs_006s/<id>` | JSON 格式的活动详情 |