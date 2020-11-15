"""formatter returns html representation for the popular object types (np.ndarray, torch.Tensor, etc)
"""
import os

import pandas as pd

from .web_templates import expandable_image, get_expandable_html

LIST_LEN_LIMIT = 2
DICT_LEN_LIMIT = 30
NUMPY_2D_LIMIT = 10


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


def get_pandas_preview(df, max_rows=10, max_cols=10):
    assert isinstance(df, pd.DataFrame)
    return df.to_html(max_rows=max_rows, max_cols=max_cols, classes="styled-table")


def _numpy_formatter(obj, to_html=None, indent=1):
    type_name = str(obj.__class__)
    if "numpy.ndarray" in type_name or "numpy.memmap" in type_name:
        name = f"np.ndarray with shape={obj.shape}; dtype={obj.dtype}"
        if len(obj.shape) == 2:
            s_obj = get_pandas_preview(pd.DataFrame(obj))
        else:
            s_obj = str(obj)

        return get_expandable_html(name=name, content=s_obj, color="eaa")


def _image_path_formatter(obj, to_html=None, indent=1):
    if isinstance(obj, str) and obj.endswith("png"):  # Looks like a path
        if os.path.exists(obj):
            return expandable_image(obj)


def _pandas_formatter(obj, to_html=None, indent=1):
    if "DataFrame" in str(obj.__class__):
        name = f"pd.DataFrame with shape={obj.shape};"
        content = get_pandas_preview(obj)
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


def full_object_name(o):
    # derived from https://stackoverflow.com/a/2020083 CC BY-SA 4.0; Greg Bacon
    # o.__module__ + "." + o.__class__.__qualname__ is an example in
    # this context of H.L. Mencken's "neat, plausible, and wrong."
    # Python makes no guarantees as to whether the __module__ special
    # attribute is defined, so we take a more circumspect approach.
    # Alas, the module name is explicitly excluded from __qualname__
    # in Python 3.
    module = o.__class__.__module__
    if module is None or module == str.__class__.__module__:
        return o.__class__.__name__  # Avoid reporting __builtin__
    else:
        return module + "." + o.__class__.__name__


def _attribute_formatter(obj, to_html, indent=1):
    if hasattr(obj, "__dict__"):
        attrs = obj.__dict__
        name = f"Instance of {full_object_name(obj)}"
        content = _dict_formatter(attrs, to_html, indent)
        return get_expandable_html(name=name, content=content)


def _bytes_formatter(obj, to_html, indent=1):
    if isinstance(obj, bytes):
        try:
            if obj[:15].decode().lower() == "<!doctype html>":
                return get_expandable_html(
                    name="bytes containing html", content=obj.decode().replace("\n", "")
                )
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
