import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

from readers import read_obj
from web_templates import (BASE_CSS, BASE_JAVASCRIPT, EXPANDABLE_PATTERN,
                           HTML_TEMPLATE, expandable_image)


def to_html(obj, indent=1):
    if isinstance(obj, list):
        htmls = []
        for k in obj:
            htmls.append(to_html(k, indent + 1))

        return '[<div style="margin-left: %dem">%s</div>]' % (
            indent,
            ",<br>".join(htmls),
        )

    if isinstance(obj, dict):
        htmls = []
        for k, v in obj.items():
            htmls.append(
                "<span style='font-style: italic; color: #888'>%s</span>: %s"
                % (k, to_html(v, indent + 1))
            )

        return '{<div style="margin-left: %dem">%s</div>}' % (
            indent,
            ",<br>".join(htmls),
        )

    type_name = str(obj.__class__)
    if "numpy.ndarray" in type_name or "numpy.memmap" in type_name:
        name = f"np.ndarray with shape={obj.shape}; dtype={obj.dtype}"
        return EXPANDABLE_PATTERN.format(name=name, content=str(obj))

    if isinstance(obj, str) and obj.endswith("png"):  # Looks like a path
        if os.path.exists(obj):
            return expandable_image(obj)

    return str(obj)


def obj_to_html(obj, style="colorful"):
    """Convert arbitrary python object to the human readable html representation"""
    body = to_html(obj)
    html = HTML_TEMPLATE.format(css=BASE_CSS, body=body, javascript=BASE_JAVASCRIPT)

    return html


def _init_text_browser(html, font_size=12, sizes=(800, 600)):
    browser = QWebEngineView()
    browser.setHtml(html, baseUrl=QUrl.fromLocalFile(os.path.abspath(__file__)))

    font = QFont()
    font.setPointSize(font_size)
    browser.setFont(font)
    browser.resize(*sizes)

    return browser


def show_object(obj):
    html = obj_to_html(obj)

    app = QApplication(sys.argv)
    browser = _init_text_browser(html)
    browser.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    py_obj = read_obj(sys.argv[1])
    show_object(py_obj)
