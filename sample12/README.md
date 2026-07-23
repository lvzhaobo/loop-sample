# 排序算法可视化展示

一个浅色背景的HTML网页，动态展示排序算法的可视化效果，页面固定显示标题"Loop-20260723"。

## 运行方式

```bash
pip install -r requirements.txt
python app.py
```

服务启动后，访问 http://localhost:5000 即可查看。

## 目录结构

```
.
├── app.py                  # Flask 入口
├── sorting_core.py         # 排序算法核心逻辑（纯函数）
├── requirements.txt        # 依赖列表
├── README.md               # 本文件
├── templates/
│   └── index.html          # 首页模板
├── static/
│   ├── css/
│   │   └── style.css       # 样式文件
│   └── js/
│       └── main.js         # 前端排序可视化逻辑
└── tests/
    └── test_sorting_core.py # 单元测试
```

## 接口列表

- `GET /`：返回排序可视化首页