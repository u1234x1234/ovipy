from obj_viewer import show_object

import numpy as np
import pandas as pd


if __name__ == "__main__":
    np_2d = np.random.uniform(size=(10000, 3))
    d = {
        "12": np_2d
    }
    df = pd.DataFrame(np_2d)

    show_object(df)
