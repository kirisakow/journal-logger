import inspect


def this_func_name():
    return inspect.stack()[1].function


def caller_func_name():
    return inspect.stack()[2].function
