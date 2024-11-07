from abc import ABC

from ..grid import Grid
from ..location import Location


class Building(ABC):
    def __init__(
        self,
        grid: Grid,
        location: Location, # top left corner
        width: int,
        height: int,
        construction_char: str,
        char: str,
    ) -> None:
        self._grid: Grid = grid
        self._location = location
        self._width: int = width
        self._height: int = height
        self._construction_char: str = construction_char
        self._char: str = char
        # todo add resources or somethin' ie. wood obtained vs wood required, etc.
        self._start_construction()
        
    def get_height(self) -> int:
        return self._height

    def get_width(self) -> int:
        return self._width
    
    def is_under_construction(self):
        return self._grid.is_location_char(self._location, self._construction_char)

    def _start_construction(self) -> None:
        # TODO place construction building on the grid, make sure we aren't overlapping with anything else
        pass

    def _get_location(self) -> Location:
        return self._location