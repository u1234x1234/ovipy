import sys

from py_obj_viewer import read_obj, show_object

if __name__ == "__main__":
    py_obj = read_obj(sys.argv[1])
    show_object(py_obj)
