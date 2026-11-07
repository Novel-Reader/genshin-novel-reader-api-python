# genshin-novel-reader-api-python

A Flask API for text analysis used by the Genshin Impact novel reader.

## 项目声明与许可证

本项目是粉丝制作项目，与米哈游及《原神》官方无关，也未获其认可或赞助。本项目没有商业推广的需求。仓库中的 MIT License 仅适用于作者有权授权的项目原创代码和文档，不涵盖米哈游或第三方拥有的商标、素材、代码及其他内容；这些内容仍受各自权利和许可约束。MIT License 允许他人在遵守许可证条件的前提下商业使用受其覆盖的内容；本项目没有商业推广需求的说明，不会限制该许可证授予的权利。详见仓库根目录的 `LICENSE` 文件。

Dependencies are installed into `.venv` by `genshin-novel-reader-scripts/scripts/init.sh`. Start the development server from the scripts repository:

```bash
bash scripts/start-python-api.sh
```

The Flask app factory is `app:create_app`. `POST /api/tags` accepts `{"text": "..."}` and returns generated tags. The Node API calls this endpoint from its scheduled job and remains responsible for updating the database. The server listens on `127.0.0.1:5000` by default; set `FLASK_HOST` and `PYTHON_PORT` to override these values.
