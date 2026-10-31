"""Flask application entry point."""

from flask import Flask


def create_app():
    return Flask(__name__)
