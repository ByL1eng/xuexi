from inspect import isfunction


def curry_partial(f, *initial_args):
    if not isfunction(f):
        return f
    if len(initial_args) < f.__code__.co_argcount:
        return lambda *a: curry_partial(f, *(initial_args + a))
    return f(*initial_args[:f.__code__.co_argcount or None])