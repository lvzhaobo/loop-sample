# 暑假快乐MumuLab - 小朋友学习与活动平台

本项目是一个面向小朋友的学习与活动展示平台，提供活动浏览和详情查看功能。

## 运行方式

1. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

2. 启动服务：
   ```
   python app.py
   ```

   服务默认运行在端口5000，可通过环境变量 `PORT` 修改。

## 目录结构

```
.
├── app.py                  # Flask应用入口
├── requirements.txt        # 依赖清单
├── README.md               # 项目说明
├── data/
│   └── activities.json     # 活动数据文件
├── templates/
│   ├── base.html           # 基础模板
│   ├── list.html           # 活动列表页
│   ├── detail.html         # 活动详情页
│   └── 404.html            # 404错误页
├── static/
│   ├── css/style.css       # 样式文件
│   └── js/main.js          # JavaScript文件
└── tests/
    └── test_app.py         # 单元测试
```

## 接口列表

| 路径 | 方法 | 说明 |
|------|------|------|
| `/` | GET | 活动列表页 |
| `/activity/<id>` | GET | 活动详情页 |
| `/api/activities` | GET | 活动列表JSON |
| `/api/activities/<id>` | GET | 单个活动JSON |