# genshin-novel-reader-api-python

A Flask API for text analysis used by the Genshin Impact novel reader.

Dependencies are installed into `.venv` by `genshin-novel-reader-scripts/scripts/init.sh`. Start the development server from the scripts repository:

```bash
bash scripts/start-python-api.sh
```

The Flask app factory is `app:create_app`. `POST /api/tags` accepts `{"text": "..."}` and returns generated tags. The Node API calls this endpoint from its scheduled job and remains responsible for updating the database. The server listens on `127.0.0.1:5000` by default; set `FLASK_HOST` and `PYTHON_PORT` to override these values.
