from typing import override

from building import Building

from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location


class Barn(Building):
    def __init__(self, grid: Grid, location: Location) -> None:
        super().__init__(grid, location, 3, 3, "b", "B")
        self._cap = 500
        self._food = 0
        self._stone_cap = 35
        self._stone = 0
        self._wood = 0
        self._wood_cap = 75

    @override
    def has_capacity(self) -> bool:
        return self._food + self._stone + self._wood < self._cap

    @staticmethod
    @override
    def work_time_estimate() -> int:
        return 1

    def add_food(self, food: int) -> None:
        self._food = min(self._cap, self._food + food)

    def remove_food(self, food: int) -> int:
        if self._food >= food:
            self._food -= food
            return food
        else:
            removed_food = self._food
            self._food = 0
            return removed_food

    def add_stone(self, stone: int) -> None:
        self._stone = min(self._cap - self._food - self._wood, self._stone + stone)

    def remove_stone(self, stone: int) -> int:
        if self._stone >= stone:
            self._stone -= stone
            return stone
        else:
            removed_stone = self._stone
            self._stone = 0
            return removed_stone

    def add_wood(self, wood: int) -> None:
        self._wood = min(self._cap - self._food - self._stone, self._wood + wood)

    def remove_wood(self, wood: int) -> int:
        if self._wood >= wood:
            self._wood -= wood
            return wood
        else:
            removed_wood = self._wood
            self._wood = 0
            return removed_wood

    def get_food_stored(self) -> int:
        return self._food

    def get_stone_stored(self) -> int:
        return self._stone

    def get_wood_stored(self) -> int:
        return self._wood

    def get_capacity(self) -> int:
        return self._cap

    def get_remaining_capacity(self) -> int:
        return self._cap - (self._food + self._stone + self._wood)
