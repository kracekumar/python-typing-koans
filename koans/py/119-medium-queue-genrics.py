"""
Koan to learn generic declaration
"""
import typing as t


# Annotate the Queue class as a generic to accept
# any data type but only same data type can be queued
class Queue:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item) -> None:
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def main() -> None:
    # Annotate the variable as Queue of string
    str_queue = Queue()
    str_queue.enqueue("welcome")
    # Annotate the variable as Queue of string
    id_queue = Queue()
    id_queue.enqueue(1)
    id_queue.dequeue()


if __name__ == "__main__":
    main()
