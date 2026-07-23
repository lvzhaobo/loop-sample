# 排序算法可视化工具

一个单页交互式Web工具，用于动态展示排序算法的执行过程，以蓝色#0066FF为主视觉。

## 运行方式

```bash
pip install -r requirements.txt
python app.py
```

服务默认监听5000端口，可通过环境变量`PORT`修改。

## 目录结构

```
.
├── app.py                  # Flask入口
├── sort_core.py            # 排序算法纯逻辑模块
├── requirements.txt        # 依赖清单
├── README.md               # 本文件
├── templates/
│   └── index.html          # 主页面模板
├── static/
│   ├── css/
│   │   └── style.css       # 样式文件
│   └── js/
│       └── sort_visualizer.js  # 前端排序动画逻辑
└── tests/
    └── test_sort_core.py   # 单元测试
```

## 接口列表

- `GET /` — 返回排序可视化主页面