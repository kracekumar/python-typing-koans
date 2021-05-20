"""
Koan to learn using type-aliases to improve readability
"""
from typing import Any

# Annotate the two variables `Line` and `Words` as type aliases. Type Aliases increase the code understanding better.
# Documentation: https://docs.python.org/3/library/typing.html#type-aliases
Line = Any
Word = Any
Words = Any


def get_words():
    words = []
    for word in line.split():
        word = word.replace(",", "").replace(".", "").lower()
        words.append(word)
    return words


line: Line = (
    "It was the best of times"
    "it was the worst of times,"
    "it was the age of wisdom,"
    "it was the age of foolishness"
)
print(get_words())
