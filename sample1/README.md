# 在线学习平台:课程列表 + 详情(Harness-4 参考实现)

> 由离线参考生成器产出,严格满足本用例契约。数据为占位内容。

## 运行
```bash
pip install -r requirements.txt
python app.py
```

## 目录
- `app.py` Flask 入口(全部路由)
- `data/courses.json` 数据源
- `templates/` 页面
- `static/` 样式与脚本
- `tests/` 单元测试

## 接口
- `GET /` 列表页
- `GET /course/<int:id>` 详情页
- `GET /api/courses` JSON 列表
- `GET /api/courses/<int:id>` JSON 详情(缺失 404)
