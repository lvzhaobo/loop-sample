# 暑假生活学习平台

一个漫画风格、童年风格的暑假生活学习平台，为两个小朋友（四年级和二年级）展示2026年暑假的活动安排，包含学习、游泳、游玩、踢球、打羽毛球等活动的交互页面。

## 运行方式

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 启动服务：
   ```bash
   python app.py
   ```

3. 访问 http://localhost:5000 查看页面。

## 目录结构

```
.
├── app.py                  # Flask 入口，渲染首页
├── requirements.txt        # 依赖列表
├── README.md               # 本文件
├── summer_core.py          # 纯逻辑模块：暑假活动数据与日期计算
├── templates/
│   └── index.html          # 首页模板（漫画风格）
├── static/
│   ├── css/
│   │   └── style.css       # 漫画风格样式
│   └── js/
│       └── main.js         # 前端交互脚本
└── tests/
    └── test_summer_core.py # 单元测试
```

## 接口列表

- `GET /`：返回暑假生活学习平台首页（HTML）。