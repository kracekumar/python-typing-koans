# Union says the value can be one of the annotated types.
# Documentation: https://docs.python.org/3/library/typing.html#typing.Union
vals: list[int] = [1, 2.6, "23"]

# Annotate the twice variable to be union of types
twice: list[int] = [val * 2 for val in vals]
