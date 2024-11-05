from memory import Memory
from src.simulation.grid.grid import Grid
from typing import List, Tuple
from src.simulation.people.person.person import Person
from typing import Callable, Dict

class Vision:
    def __init__(self, person: Person, grid: Grid, visibility: int) -> None:
        self._person: Person = person
        self._grid: Grid = grid
        self._visibility: int = visibility

    def look_around(self) -> Memory:
        what_is_around: Memory = Memory()
        self._search(self._person.get_location(), self._visibility, what_is_around, [])
        return what_is_around

    def _search(self, location: Tuple[int, int], visibility: int, what_is_around: Memory, blocked: List[Tuple[int, int]]) -> None:
        if visibility <= 0:
            return
        if location in blocked:
            return
        x, y = location
        blocked.append((x, y))
        for i in range(-1, 2):
            for j in range(-1, 2):
                a = x + i
                b = y + j
                if self._is_out_of_bounds(a, b) or self._is_blocked(blocked, a, b):
                    continue
                self._add_to_memory(what_is_around, blocked, i, j, a, b)
                self._search((a, b), visibility - 1, what_is_around, blocked)

    def _add_to_memory(self, what_is_around: Memory, blocked: List[Tuple[int, int]], i: int, j: int, a: int, b: int) -> None:
        location: Tuple[int, int] = (a, b)
        if not self._grid.is_location_in_bounds(location):
            return

        # Create a map of objects that block vision with correct typing for check_fn
        blocking_objects: Dict[str, Callable[[Tuple[int, int]], bool]] = {
            "barn": self._grid.is_barn,
            "construction_barn": self._grid.is_construction_barn,
            "home": self._grid.is_home,
            "construction_home": self._grid.is_construction_home,
            "farm": self._grid.is_farm,
            "construction_farm": self._grid.is_construction_farm,
            "mine": self._grid.is_mine,
            "construction_mine": self._grid.is_construction_mine,
            "tree": self._grid.is_tree
        }

        # Handle blocking objects
        for object_type, check_fn in blocking_objects.items():
            if check_fn(location):
                what_is_around.add(f"{object_type}s", location)
                self._block(blocked, i, j, a, b)
                return  # Block vision and stop further checks for this location

        # Non-blocking objects (don't call _block)
        if self._grid.is_empty(location):
            what_is_around.add("empties", location)
        else:
            raise Exception(f"I see a char you didn't tell me about: {location}")

    def _is_out_of_bounds(self, x: int, y: int) -> bool:
        return (
                x < 0
                or y < 0
                or x >= self._grid.get_width()
                or y >= self._grid.get_height()
        )

    def _block(self, blocked: List[Tuple[int, int]], i: int, j: int, a: int, b: int) -> None:
        blocked.append((a, b))
        if not self._is_diagonal(i, j):
            direction: str = self._get_direction(i, j)
            if direction == "l":
                for k in range(a, 0, -1):
                    blocked.append((a + k, b))
            elif direction == "r":
                for k in range(a, self._grid.get_width()):
                    blocked.append((a + k, b))
            elif direction == "d":
                for k in range(b, self._grid.get_height()):
                    blocked.append((a, b + k))
            elif direction == "u":
                for k in range(b, 0, -1):
                    blocked.append((a, b + k))

    @staticmethod
    def _is_blocked(blocked: List[Tuple[int, int]], x: int, y: int) -> bool:
        return (x, y) in blocked

    @staticmethod
    def _is_diagonal(i: int, j: int) -> bool:
        return i < 0 < j or j < 0 < i or (i < 0 and j < 0) or (i > 0 and j > 0)

    @staticmethod
    def _get_direction(i: int, j: int) -> str:
        if i == 0 and j == 1:
            return "r"
        if i == 0 and j == -1:
            return "l"
        if i == 1 and j == 0:
            return "u"
        if i == -1 and j == 0:
            return "d"
        else:
            raise Exception("invalid coordinates")
