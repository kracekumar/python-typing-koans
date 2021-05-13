import operator
from collections.abc import Callable, Iterable
from typing import TypedDict


class UserData(TypedDict):
    user_id: int
    is_active: bool


# Annotate the function arguments
# Documentation: https://docs.python.org/3/library/typing.html?highlight=typing#callable
# Documentation: https://docs.python.org/3/library/typing.html?highlight=typing#typing.Iterable
def user_sort(
    data: Iterable[UserData], func: Callable[[UserData], int]
) -> Iterable[UserData]:
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
