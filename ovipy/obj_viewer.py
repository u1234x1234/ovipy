import os
import sys
from tempfile import NamedTemporaryFile

from flask import Flask, send_from_directory
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

from .formatters import FORMATTERS
from .web_templates import BASE_CSS, BASE_JAVASCRIPT, HTML_TEMPLATE


def to_html(obj, indent=1):

    for formatter in FORMATTERS:
        f_obj = formatter(obj, to_html, indent)
        if f_obj is not None:
            return f_obj

    return str(obj)


def obj_to_html(obj, style="colorful"):
    """Convert arbitrary python object to the human readable html representation"""
    body = to_html(obj)
    html = HTML_TEMPLATE.format(css=BASE_CSS, body=body, javascript=BASE_JAVASCRIPT)

    return html


def _init_text_browser(path, font_size=12, sizes=(800, 600)):
    browser = QWebEngineView()
    browser.load(QUrl.fromLocalFile(os.path.abspath(path)))

    font = QFont()
    font.setPointSize(font_size)
    browser.setFont(font)
    browser.resize(*sizes)

    return browser


def show_gui(obj):
    html = obj_to_html(obj)

    app = QApplication(sys.argv)

    with NamedTemporaryFile("wb", buffering=0, suffix=".html") as out_file:
        out_file.write(html.encode("utf-8"))
        out_file.flush()

        browser = _init_text_browser(out_file.name)
        browser.show()
        sys.exit(app.exec_())


def create_flask_static_serving_app(path):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return send_from_directory(os.path.dirname(path), os.path.basename(path))

    return app


def show_web(obj, host="localhost", port=8090):
    "Save obj to html and serve it with Flask"
    html = obj_to_html(obj)

    with NamedTemporaryFile("wb", buffering=0, suffix=".html") as out_file:
        out_file.write(html.encode("utf-8"))
        out_file.flush()

        app = create_flask_static_serving_app(out_file.name)
        app.run(port=port, host=host, debug=False)


def save_to_html(obj, path):
    html = obj_to_html(obj)
    with open(path, "w") as out_file:
        print(html, file=out_file)
