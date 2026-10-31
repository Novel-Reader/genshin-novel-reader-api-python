"""Entry point for the Python API service."""

from flask import Flask, jsonify, request

from tags import generate_tags


def create_app():
    app = Flask(__name__)

    @app.post("/api/tags")
    def create_tags():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict) or not isinstance(payload.get("text"), str):
            return jsonify(error="A text string is required"), 400

        return jsonify(tags=generate_tags(payload["text"]))

    return app
