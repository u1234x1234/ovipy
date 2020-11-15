from py_obj_viewer import show_object

import numpy as np
import pandas as pd


class MyClass:
    def __init__(self, x):
        self.field1 = x


if __name__ == "__main__":
    np_2d = np.random.uniform(size=(10000, 3))
    d = {
        "12": np_2d
    }
    # df = pd.DataFrame(np_2d)
    # df = MyClass(MyClass(d))

    import requests
    df = requests.get("http://google.com")
    # func(df)
    # df = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4]]
    show_object(df)
