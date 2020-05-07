import importlib


def get_class_for_name(full_cls_name):
    parts = full_cls_name.split(".")
    module_name = '.'.join(parts[:len(parts) - 1])
    class_name = parts[-1]
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(module_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c
