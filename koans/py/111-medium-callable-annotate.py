"""
Koan to learn annotating the callables or functions.
"""

# Annotate the function arguments
# Documentation: https://docs.python.org/3/library/typing.html?highlight=typing#callable
# Documentation: https://docs.python.org/3/library/typing.html?highlight=typing#typing.Iterable
def user_sort(data, func):
    return sorted(data, key=func)


def key_func(item):
    return item["user_id"]


def main():
    # Annotate the data
    data = [
        {"user_id": 1, "is_active": True},
        {"user_id": 34, "is_active": True},
        {"user_id": 3, "is_active": False},
    ]

    assert user_sort(data, key_func)


if __name__ == "__main__":
    main()
