import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

from readers import read_obj

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>py_obj_viewer</title>
    <style>
        {css}
    </style>
</head>
<body>
    {body}

<script>
{javascript}
</script>

</body>
</html>
"""

BASE_CSS = """
.collapsible {
  background-color: #eee;
  color: #444;
  cursor: pointer;
  padding: 3px;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

/* Add a background color to the button if it is clicked on (add the .active class with JS), and when you move the mouse over it (hover) */
.active, .collapsible:hover {
  background-color: #ccc;
}

/* Style the collapsible content. Note: hidden by default */
.content {
  padding: 0 18px;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
}
"""

EXPANDABLE_PATTERN = """
<button type="button" class="collapsible">{name}</button>
<div class="content">
  <p>{content}</p>
</div>
"""

BASE_JAVASCRIPT = """
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
"""


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

    return str(obj)


def obj_to_html(obj, style="colorful"):
    """Convert arbitrary python object to the human readable html representation"""
    body = to_html(obj)
    html = HTML_TEMPLATE.format(css=BASE_CSS, body=body, javascript=BASE_JAVASCRIPT)

    return html


def _init_text_browser(html, font_size=12, sizes=(800, 600)):
    text_browser = QWebEngineView()
    text_browser.setHtml(html)

    font = QFont()
    font.setPointSize(font_size)
    text_browser.setFont(font)

    text_browser.resize(*sizes)

    return text_browser


if __name__ == "__main__":
    py_obj = read_obj(sys.argv[1])
    html = obj_to_html(py_obj)

    app = QApplication(sys.argv)
    text_browser = _init_text_browser(html)
    text_browser.show()
    sys.exit(app.exec_())
