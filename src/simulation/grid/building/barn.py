from typing import override

from building import Building

from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location


class Barn(Building):
    def __init__(self, grid: Grid, location: Location) -> None:
        super().__init__(grid, location, 3, 3, "b", "B")
        self._food_cap = 100
        self._food = 0
        self._stone_cap = 35
        self._stone = 0

    @override
    def has_capacity(self) -> bool:
        pass

    @staticmethod
    @override
    def work_time_estimate() -> int:
        pass

    def add_food(self, food) -> None:
        self._food = min(self._food_cap, self._food + food)

    def add_stone(self, stone) -> None:
        self._stone = min(self._stone_cap, self._stone + stone)