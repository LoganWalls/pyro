import torch
from torch.autograd import Variable
from torch.nn import Parameter


def _dict_to_tuple(d):
    """
    Recursively converts a dictionary to a list of key-value tuples
    Only intended for use as a helper function inside memoize!!
    May break when keys cant be sorted, but that is not an expected use-case
    """
    if isinstance(d, dict):
        return tuple([(k, _dict_to_tuple(d[k])) for k in sorted(d.keys())])
    else:
        return d


def memoize(fn):
    """
    https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python
    unbounded memoize
    alternate in py3: https://docs.python.org/3/library/functools.html
    lru_cache
    """
    _mem = {}

    def _fn(*args, **kwargs):
        kwargs_tuple = _dict_to_tuple(kwargs)
        if (args, kwargs_tuple) not in _mem:
            _mem[(args, kwargs_tuple)] = fn(*args, **kwargs)
        return _mem[(args, kwargs_tuple)]
    return _fn


def ones(*args, **kwargs):
    return Parameter(torch.ones(*args, **kwargs))
    # return pyro.device(Parameter(torch.ones(*args, **kwargs)))


def zeros(*args, **kwargs):
    return Parameter(torch.zeros(*args, **kwargs))
    # return pyro.device(Parameter(torch.zeros(*args, **kwargs)))


def ng_ones(*args, **kwargs):
    return Variable(torch.ones(*args, **kwargs), requires_grad=False)


def ng_zeros(*args, **kwargs):
    return Variable(torch.zeros(*args, **kwargs), requires_grad=False)
