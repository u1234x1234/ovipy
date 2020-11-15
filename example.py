from py_obj_viewer import show_object

import numpy as np
import pandas as pd
import torch


class MyClass:
    def __init__(self, x):
        self.field1 = x


if __name__ == "__main__":
    df = {
        "12": np.random.uniform(size=(1000, 20)),
        # "t_t": torch.rand(10, 20),
    }
    # df = pd.DataFrame(np_2d)
    # df = MyClass(MyClass(d))

    # import requests
    # df = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
    # func(df)
    # df = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4]]
    show_object(df)
