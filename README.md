# genshin-novel-reader-api-python

A Flask application scaffold for the Genshin Impact novel reader API.

Dependencies are installed into `.venv` by `genshin-novel-reader-scripts/scripts/init.sh`. Start the development server from the scripts repository:

```bash
bash scripts/start-python-api.sh
```

The Flask app factory is `app:create_app`. The server listens on `127.0.0.1:5000` by default; set `FLASK_HOST` and `PYTHON_PORT` to override these values.
