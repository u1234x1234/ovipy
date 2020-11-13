"""formatter returns html representation for the popular object types (np.ndarray, torch.Tensor, etc)
"""
import os

from .web_templates import EXPANDABLE_PATTERN, expandable_image


def _numpy_formatter(obj):
    type_name = str(obj.__class__)
    if "numpy.ndarray" in type_name or "numpy.memmap" in type_name:
        name = f"np.ndarray with shape={obj.shape}; dtype={obj.dtype}"
        return EXPANDABLE_PATTERN.format(name=name, content=str(obj))


def _image_path_formatter(obj):
    if isinstance(obj, str) and obj.endswith("png"):  # Looks like a path
        if os.path.exists(obj):
            return expandable_image(obj)


def _pandas_formatter(obj):
    if "DataFrame" in str(obj.__class__):
        name = f"pd.DataFrame with shape={obj.shape};"
        content = obj.iloc[list(range(5)) + list(range(-5, 0))].to_html()
        return EXPANDABLE_PATTERN.format(name=name, content=content)


def _torch_formatter(obj):
    type_name = str(obj.__class__)
    if "torch.Tensor" in type_name:
        name = f"torch.Tensor with shape={list(obj.shape)}; dtype={obj.dtype}; device={obj.device}"
        return EXPANDABLE_PATTERN.format(name=name, content=str(obj))


FORMATTERS = [
    _numpy_formatter,
    _image_path_formatter,
    _pandas_formatter,
    _torch_formatter,
]
