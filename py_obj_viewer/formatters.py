"""formatter returns html representation for the popular object types (np.ndarray, torch.Tensor, etc)
"""
import os

from .web_templates import expandable_image, get_expandable_html

LIST_LEN_LIMIT = 2
DICT_LEN_LIMIT = 30


def _list_formatter(obj, to_html, indent=1):

    if isinstance(obj, list):
        items = []
        for k in obj:
            items.append(to_html(k, indent + 1))

        list_str = '[<div style="margin-left: %dem">%s</div>]' % (
            indent,
            ",<br>".join(items),
        )
        if len(items) > LIST_LEN_LIMIT:
            list_str = get_expandable_html(
                f"python list with {len(items)} elements", list_str
            )

        return list_str


def _dict_formatter(obj, to_html, indent=1):
    if isinstance(obj, dict):
        items = []
        for k, v in obj.items():
            items.append(
                "<span style='font-style: italic; color: #888'>%s</span>: %s"
                % (k, to_html(v, indent + 1))
            )

        dict_str = '{<div style="margin-left: %dem">%s</div>}' % (
            indent,
            ",<br>".join(items),
        )
        if len(items) > DICT_LEN_LIMIT:
            dict_str = get_expandable_html(
                f"python dict with {len(items)} elements", dict_str
            )

        return dict_str


def _numpy_formatter(obj, to_html=None, indent=1):
    type_name = str(obj.__class__)
    if "numpy.ndarray" in type_name or "numpy.memmap" in type_name:
        name = f"np.ndarray with shape={obj.shape}; dtype={obj.dtype}"
        return get_expandable_html(name=name, content=str(obj), color="eaa")


def _image_path_formatter(obj, to_html=None, indent=1):
    if isinstance(obj, str) and obj.endswith("png"):  # Looks like a path
        if os.path.exists(obj):
            return expandable_image(obj)


def _pandas_formatter(obj, to_html=None, indent=1):
    if "DataFrame" in str(obj.__class__):
        name = f"pd.DataFrame with shape={obj.shape};"
        content = obj.iloc[list(range(5)) + list(range(-5, 0))].to_html()
        return get_expandable_html(name=name, content=content)


def _torch_formatter(obj, to_html=None, indent=1):
    type_name = str(obj.__class__)
    if "torch.Tensor" in type_name:
        name = f"torch.Tensor with shape={list(obj.shape)}; dtype={obj.dtype}; device={obj.device}"
        return get_expandable_html(name=name, content=str(obj), color="aae")


def _large_obj_formatter(obj, to_html=None, indent=1, n_lines_limit=15):
    s_obj = str(obj)
    n_lines = s_obj.count("\n")
    if n_lines > n_lines_limit:
        name = f"{type(obj)}"
        return get_expandable_html(name=name, content=s_obj)


def _attribute_formatter(obj, to_html, indent=1):
    if hasattr(obj, "__dict__"):
        attrs = obj.__dict__
        content = _dict_formatter(attrs, to_html, indent)
        name = f'Instance of "{obj.__class__.__name__}"'
        return get_expandable_html(name=name, content=content)


def _bytes_formatter(obj, to_html, indent=1):
    if isinstance(obj, bytes):
        try:
            if obj[:15].decode().lower() == "<!doctype html>":
                return get_expandable_html(name="bytes containing html", content=obj)
        except Exception:
            pass


FORMATTERS = [
    _list_formatter,
    _dict_formatter,
    _numpy_formatter,
    _image_path_formatter,
    _pandas_formatter,
    _torch_formatter,
    _large_obj_formatter,
    _attribute_formatter,
    _bytes_formatter,
]
