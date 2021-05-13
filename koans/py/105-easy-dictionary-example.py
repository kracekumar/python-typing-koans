from collections import defaultdict

# Annotate the dictionary
# Documentation: https://docs.python.org/3/library/typing.html#typing.Dict
result = defaultdict(int)
words = ["welcome", "to", "the", "world", "world", "is", "uneven", "place"]
for word in words:
    result[word] += 1

print(result)
