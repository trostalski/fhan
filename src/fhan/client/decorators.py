from functools import wraps

import cachetools


def conditional_cache(func):
    """
    Decorator for conditionally applying cache based on `use_cache` flag.

    Args:
        func (Function): The function to be decorated.

    Returns:
        Function: Original function or cached function based on `use_cache`.
    """

    cached_func = None

    @wraps(func)
    def wrapper(*args, **kwargs):
        use_cache = kwargs.pop("use_cache", False)
        cache = kwargs.pop("cache", None)
        headers = kwargs.pop("headers", None)
        if use_cache:
            nonlocal cached_func
            if cached_func is None:
                cached_func = cachetools.cached(cache)(func)
            return cached_func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


from functools import wraps
import cachetools
