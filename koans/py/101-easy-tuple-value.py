"""
Koan to learn annotating the Python tuple
"""
from typing import Any

# result is annotated as Any, annotate it as tuple
# How to annotate tuple: https://docs.python.org/3/library/typing.html#typing.Tuple
result: Any = ("stdin", "stdout", 2)

# annotate the variable as tuple of integers
values: Any = tuple(range(10))
