from abc import ABC


class Building(ABC):
    def __init__(self, grid, x, y, width, height, construction_char, char):
        self._grid = grid
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._construction_char = construction_char
        self._char = char
        self._start_construction()

    def _start_construction(self):
        # TODO place construction building on the grid, make sure we arent overlapping with anything else
        pass
