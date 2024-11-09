from typing import override

from building import Building

from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location


class Home(Building):

    def __init__(self, grid: Grid, location: Location) -> None:
        super().__init__(grid, location, 2, 2, "h", "H")

        self._occupied: bool = False
        self._food: int = 0
        self._food_capacity: int = 36
    
    def has_owner(self) -> bool:
        return self._occupied
    
    def assign_owner(self) -> None:
        self._occupied = True

    def remove_owner(self) -> None:
        self._occupied = False

    def has_food(self) -> bool:
        return self._food > 0
    
    def add_food(self, food: int) -> None:
        self._food = min(self._food_capacity, self._food + food)

    def remove_food(self, food: int) -> int:
        if self._food >= food:
            self._food -= food
            return food
        else:
            removed_food = self._food
            self._food = 0
            return removed_food

    def get_food_capacity(self) -> int:
        return self._food_capacity

    @override
    def has_capacity(self) -> bool:
        pass

    @staticmethod
    @override
    def work_time_estimate() -> int:
        pass
