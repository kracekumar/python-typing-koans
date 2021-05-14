"""
Koan to learn annotating the decorator
"""
import typing as t

# annotate the dict to store only ints
cached_results = {}

# Annotate the function to receive the function and return the function
def cache(f):
    def inner(n):
        if n in cached_results:
            return cached_results[n]
        cached_results[n] = f(n)
        return cached_results[n]

    return inner


@cache
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
