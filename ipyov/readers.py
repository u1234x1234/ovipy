import json
import pickle


class DummyClass:
    pass


class PartialUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        try:
            return super().find_class(module, name)
        except Exception as e:
            x = DummyClass
            setattr(x, "__module__", module)
            setattr(x, "__name__", "{} unpickling error: {}".format(name, e))
            return x


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


def load_torch(path):
    import torch
    return torch.load(path)


def load_cloudpickle(path):
    import cloudpickle
    with open(path, "rb") as in_file:
        data = cloudpickle.load(in_file)

    return data


def load_dill(path):
    import dill
    with open(path, "rb") as in_file:
        return dill.load(in_file)


LOADERS = {
    "pkl": load_pickle,
    "json": load_json,
    "npy": load_npy,
    "npz": load_npz,
    "pkll": load_pkll,
    "pt": load_torch,
    "cloudpickle": load_cloudpickle,
    "dill": load_dill,
}


def read_obj(path: str):
    ext = path.split(".")[-1]
    if ext in LOADERS:
        data = LOADERS[ext](path)
    else:
        raise ValueError("Unknown file type")

    return data
