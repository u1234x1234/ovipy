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

img{
    max-width: 300px;
    max-height: 300px;
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


def expandable_image(path):
    content = f'<img src="{path}" >'
    return EXPANDABLE_PATTERN.format(content=content, name=path)
