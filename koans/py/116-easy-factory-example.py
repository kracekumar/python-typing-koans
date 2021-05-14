"""
Koan to learn annotating the factory method and return types
"""
# Example: https://en.wikipedia.org/wiki/Factory_method_pattern#Python

from abc import ABC, abstractmethod


class MazeGame(ABC):
    def __init__(self) -> None:
        # Annotate rooms
        self.rooms = []
        self._prepare_rooms()

    def _prepare_rooms(self) -> None:
        # Annotate room1 and room2
        room1 = self.make_room()
        room2 = self.make_room()

        room1.connect(room2)
        self.rooms.append(room1)
        self.rooms.append(room2)

    def play(self) -> None:
        print('Playing using "{}"'.format(self.rooms[0]))

    @abstractmethod
    # Annotate the return type
    def make_room(self) -> Room:
        raise NotImplementedError("You should implement this!")


class MagicMazeGame(MazeGame):
    # Annotate the return type
    def make_room(self):
        return MagicRoom()


class OrdinaryMazeGame(MazeGame):
    # Annotate the return type
    def make_room(self):
        return OrdinaryRoom()


class Room(ABC):
    def __init__(self) -> None:
        # Annotate the variable
        self.connected_rooms = []

    # Annotate the room argument
    def connect(self, room) -> None:
        self.connected_rooms.append(room)


class MagicRoom(Room):
    def __str__(self) -> str:
        return "Magic room"


class OrdinaryRoom(Room):
    def __str__(self) -> str:
        return "Ordinary room"


def main() -> None:
    ordinary_game = OrdinaryMazeGame()
    ordinary_game.play()

    magic_game = MagicMazeGame()
    magic_game.play()


if __name__ == "__main__":
    main()
