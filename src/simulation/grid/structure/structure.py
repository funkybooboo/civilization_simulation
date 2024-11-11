from abc import ABC, abstractmethod

from ..grid import Grid
from ..location import Location


class Structure(ABC):
    def __init__(
        self,
        grid: Grid,
        location: Location,  # top left corner
        width: int,
        height: int,
        char: str,
    ):
        self._grid: Grid = grid
        self._location = location
        self._width: int = width
        self._height: int = height
        self._char: str = char
        self._place_structure_on_grid()

    def _place_structure_on_grid(self) -> None:
        """
        This method sets up the construction on the grid by verifying the location
        and ensuring no overlap with existing structures or trees.
        Construction can only start once all required resources are delivered.
        """
        # Construction can only start if all resources are delivered
        # Check if the construction area is valid (no overlap, within bounds)
        for dy in range(self._height):
            for dx in range(self._width):
                location = Location(self._location.x + dx, self._location.y + dy)

                # Check if the location is within bounds
                if not self._grid.is_location_in_bounds(location):
                    raise ValueError(f"Building goes out of bounds at {location}")

                # Check if the location is already occupied by another structure or a tree
                if not self._grid.is_empty(location) and not self._grid.is_tree(
                    location
                ):
                    raise ValueError(
                        f"Location {location} is already occupied by another building or tree"
                    )

        # If all checks pass, start placing the construction on the grid
        for dy in range(self._height):
            for dx in range(self._width):
                location = Location(self._location.x + dx, self._location.y + dy)
                self._grid.get_grid()[location.y][location.x] = self._char
                print(
                    f"Placing structure at {location}"
                )  # For debugging, can be removed later.

    def get_location(self):
        return self._location

    def get_height(self) -> int:
        return self._height

    def get_width(self) -> int:
        return self._width

    def _get_location(self) -> Location:
        return self._location

    @abstractmethod
    def has_capacity(self) -> bool:
        # can someone else be in or use the structure
        pass

    @staticmethod
    @abstractmethod
    def work_time_estimate() -> int:
        # how long will it take to finish work at this structure?
        pass
