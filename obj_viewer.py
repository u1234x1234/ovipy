import json
import os
import pickle
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QTextBrowser


def _format(obj):
    if isinstance(obj, dict):
        text = json.dumps(obj, indent=2, default=str)
    else:
        text = str(obj)
    
    return text


def _prepare_text(path):
    with open(path, "rb") as in_file:
        data = pickle.load(in_file)

    text = _format(data)
    return text


def _init_text_browser(font_size=12, sizes=(600, 400)):
    text_browser = QTextBrowser()
    text_browser.setText(text)

    font = QFont()
    font.setPointSize(font_size)
    text_browser.setFont(font)

    text_browser.resize(*sizes)

    return text_browser


if __name__ == "__main__":
    text = _prepare_text(sys.argv[1])

    app = QApplication(sys.argv)
    text_browser = _init_text_browser()
    text_browser.show()
    sys.exit(app.exec_())
