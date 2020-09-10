import json
import pickle
import sys

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QTextBrowser

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My HTML Document</title>
    <style>
        {css_code}
    </style>
</head>
<body>
    {body}
</body>
</html>
"""


def _format(obj, style="colorful"):
    if isinstance(obj, (dict, list)):
        text = json.dumps(obj, indent=2, default=str)
    else:
        text = str(obj)

    formatter = HtmlFormatter(style=style)
    text = highlight(text, PythonLexer(), formatter)
    css = formatter.get_style_defs()
    html = HTML_TEMPLATE.format(css_code=css, body=text)

    return html


def _prepare_text(path):
    if path.endswith(".pkl"):
        with open(path, "rb") as in_file:
            data = pickle.load(in_file)
    elif path.endswith(".json"):
        with open(path, "rb") as in_file:
            data = json.load(in_file)
    else:
        raise ValueError("Unknown file type")

    return data


def _init_text_browser(html, font_size=12, sizes=(800, 600)):
    text_browser = QTextBrowser()
    text_browser.setHtml(html)

    font = QFont()
    font.setPointSize(font_size)
    text_browser.setFont(font)

    text_browser.resize(*sizes)

    return text_browser


if __name__ == "__main__":
    text = _prepare_text(sys.argv[1])
    html = _format(text)

    app = QApplication(sys.argv)
    text_browser = _init_text_browser(html)
    text_browser.show()
    sys.exit(app.exec_())
