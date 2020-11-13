import json
import pickle


def create_dummy_class(name):
    x = type(name, (), {})
    setattr(x, "__setstate__", lambda x: None)
    setattr(x, "__module__", None)
    return x


class PartialUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        try:
            return super().find_class(module, name)
        except ImportError:
            return lambda *args: create_dummy_class(module)


def load_pickle(path):
    with open(path, "rb") as in_file:
        return PartialUnpickler(in_file).load()


def load_json(path):
    with open(path, "rb") as in_file:
        return json.load(in_file)


def load_npy(path):
    import numpy as np

    return np.load(path, mmap_mode="r")


def load_npz(path):
    import numpy as np

    d = np.load(path)
    return [d[name] for name in d.keys()]


def load_pkll(path):
    results = []
    with open(path, "rb") as in_file:
        while True:
            try:
                item = pickle.load(in_file)
                results.append(item)
            except EOFError:
                break

    return results


LOADERS = {
    "pkl": load_pickle,
    "json": load_json,
    "npy": load_npy,
    "npz": load_npz,
    "pkll": load_pkll,
}


def read_obj(path: str):
    ext = path.split(".")[-1]
    if ext in LOADERS:
        data = LOADERS[ext](path)
    else:
        raise ValueError("Unknown file type")

    return data
