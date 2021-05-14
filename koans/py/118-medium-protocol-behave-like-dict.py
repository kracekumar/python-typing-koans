"""
Koan to learn annotating structural typing, Protocol - dict like behavior
"""
import typing as t

import requests


class Header:
    def __init__(self) -> None:
        self._store = {}

    def __getitem__(self, key) -> str:
        try:
            return self._store[key]
        except KeyError:
            raise KeyError()

    def __setitem__(self, key, val) -> None:
        self._store[key] = val

    def items(self):
        return self._store.items()


# Python requests module accepts headers as a dictionary.
# Annotate the headers argument to accept any class which implements
# the three methods `__getitem__`, `__setitem__`, `items` as acceptable values.
def send_request(headers) -> None:
    resp = requests.get("https://httpbin.org/headers", headers=headers)
    print(resp.json())  # type: ignore


def main() -> None:
    header = Header()
    header["x-repo-name"] = "python-typing-koans"
    send_request(header)
    send_request({"x-repo-name": "python-typing-koans"})


if __name__ == "__main__":
    main()
