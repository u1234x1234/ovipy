"""formatter returns html representation for the popular object types (np.ndarray, torch.Tensor, etc)
"""
import os

from .web_templates import get_expandable_html, expandable_image


def _numpy_formatter(obj):
    type_name = str(obj.__class__)
    if "numpy.ndarray" in type_name or "numpy.memmap" in type_name:
        name = f"np.ndarray with shape={obj.shape}; dtype={obj.dtype}"
        return get_expandable_html(name=name, content=str(obj), color="eaa")


def _image_path_formatter(obj):
    if isinstance(obj, str) and obj.endswith("png"):  # Looks like a path
        if os.path.exists(obj):
            return expandable_image(obj)


def _pandas_formatter(obj):
    if "DataFrame" in str(obj.__class__):
        name = f"pd.DataFrame with shape={obj.shape};"
        content = obj.iloc[list(range(5)) + list(range(-5, 0))].to_html()
        return get_expandable_html(name=name, content=content)


def _torch_formatter(obj):
    type_name = str(obj.__class__)
    if "torch.Tensor" in type_name:
        name = f"torch.Tensor with shape={list(obj.shape)}; dtype={obj.dtype}; device={obj.device}"
        return get_expandable_html(name=name, content=str(obj), color="aae")


def _large_obj_formatter(obj, n_lines_limit=15):
    s_obj = str(obj)
    n_lines = s_obj.count("\n")
    if n_lines > n_lines_limit:
        name = f"{type(obj)}"
        return get_expandable_html(name=name, content=s_obj)


FORMATTERS = [
    _numpy_formatter,
    _image_path_formatter,
    _pandas_formatter,
    _torch_formatter,
    _large_obj_formatter,
]
