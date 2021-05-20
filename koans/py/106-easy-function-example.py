"""
Koan to learn annotating the function
"""
# Annotate the function arguments to accept integer and return value as integer
# Documentation: https://docs.python.org/3/library/typing.html#module-typing
def square(x):
    return x * x


squares = [square(val) for val in range(1, 10)]
