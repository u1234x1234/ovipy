# ipyov - Interactive visualizer of python objects.

# Installation
```
pip install git+https://github.com/u1234x1234/ipyov.git@0.0.1
```

# Usage
```python
from ipyov import show_object

import requests
response = requests.get("https://en.wikipedia.org/")
show_object(response)


# Another example
import numpy as np
import pandas as pd
import torch

complex_object = {
    "list_with_strings": ["a"*5, "b"*20, "c"*3] * 5,
    "12": np.random.uniform(size=(1000, 20)),
    "nested_dicts": {"dict_key": ["some_data"] * 10, "nested": {1: 3}, "data": [1] * 10},
    "df": pd.DataFrame(np.random.uniform(size=(1000, 20))),
    "t_t": torch.rand(20, 5),
}
show_object(complex_object)
```

<table border="0">
 <tr>
    <td><div class="tip" markdown="1">requests</div></td>
    <td><div class="tip" markdown="1">complex_object</div></td>
 </tr>
 <tr>
    <td><img src="https://user-images.githubusercontent.com/5442732/100473428-29718a80-3100-11eb-9c5a-1725d40223ec.gif" width="400" title="zeroopt"></td>
    <td><img src="https://user-images.githubusercontent.com/5442732/100473446-34c4b600-3100-11eb-80e2-0dc9c46a2af5.gif" width="400" title="zeroopt"></td>
 </tr>
</table>
