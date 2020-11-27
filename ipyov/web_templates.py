HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>pyov</title>
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

img {
    max-width: 300px;
    max-height: 300px;
}

body {
    background-color: rgb(250, 250, 250);
}

.active, .collapsible:hover {
    background-color: #ccc;
}

.content {
    padding: 0 18px;
    display: none;
    overflow: hidden;
    background-color: #ffffff;
}

.styled-table {
    border-collapse: collapse;
    margin: 5px 0;
    font-size: 0.9em;
    font-family: sans-serif;
    min-width: 400px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

"""

EXPANDABLE_PATTERN = """
<button type="button" class="collapsible" style='background-color: #{color}'>{name}</button>
<div class="content">
    {content}
</div>
"""

BASE_JAVASCRIPT = """
var items = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < items.length; i++) {
    items[i].addEventListener("click", function() {
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


def get_expandable_html(name, content, color="eee"):
    return EXPANDABLE_PATTERN.format(name=name, content=content, color=color)


def expandable_image(path):
    content = f'<img src="{path}" >'
    return EXPANDABLE_PATTERN.format(content=content, name=path)
