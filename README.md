# ovipy - Interactive visualizer of python objects.

# Usage
```python
from ovipy import show_gui
import requests
show_gui(requests.get("https://en.wikipedia.org/"))

import numpy as np # Another example
import pandas as pd
import torch

complex_object = {
    "list_with_strings": ["a"*5, "b"*20, "c"*3] * 5,
    "12": np.random.uniform(size=(1000, 20)),
    "nested_dicts": {"dict_key": ["some_data"] * 10, "nested": {1: 3}, "data": [1] * 10},
    "df": pd.DataFrame(np.random.uniform(size=(1000, 20))),
    "t_t": torch.rand(20, 5),
}
show_gui(complex_object)
```

<table border="0">
 <tr>
    <td><img src="https://user-images.githubusercontent.com/5442732/100473428-29718a80-3100-11eb-9c5a-1725d40223ec.gif" width="400" title="zeroopt"></td>
    <td><img src="https://user-images.githubusercontent.com/5442732/100473446-34c4b600-3100-11eb-80e2-0dc9c46a2af5.gif" width="400" title="zeroopt"></td>
 </tr>
</table>

# Installation
```
pip install PyQt5 PyQtWebEngine
pip install git+https://github.com/u1234x1234/ovipy.git@0.0.3
```
