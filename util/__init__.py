import functools

# class lazy(object):
#
#     def __init__(self, wrapped):
#         self.wrapped = wrapped
#
#         update_wrapper(self, wrapped)
#
#     def __get__(self, instance, obj_type=None):
#
#         if instance is None:
#             return self
#         value = self.wrapped(instance)
#         setattr(instance, self.wrapped.__name__, value)
#         return value

# from typing import Dict, Any
#
# cache = dict()
#
#
# def lazy(fn):
#
#     cached = cache[fn]
#
#     if not cached:
#         result = fn()
#         cache[fn] = result
#         return result
#     else:
#         return cached


def lazy(fn):
    if fn.__name__ == fn.__qualname__:
        # not a property
        result = fn()
        return result
    else:
        return LazyProperty(fn)


class LazyProperty(object):
    """lazy descriptor
    Used as a decorator to create lazy attributes. Lazy attributes
    are evaluated on first use.
    """

    def __init__(self, func):
        self.__func = func
        functools.wraps(self.__func)(self)

    def __get__(self, inst, inst_cls):
        if inst is None:
            return self

        if not hasattr(inst, '__dict__'):
            raise AttributeError("'%s' object has no attribute '__dict__'" % (inst_cls.__name__,))

        name = self.__name__
        if name.startswith('__') and not name.endswith('__'):
            name = '_%s%s' % (inst_cls.__name__, name)

        value = self.__func(inst)
        inst.__dict__[name] = value
        return value
