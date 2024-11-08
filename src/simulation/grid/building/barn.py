from building import Building
from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location


class Barn(Building):
    def __init__(self, grid: Grid, location: Location) -> None:
        super().__init__(grid, location, 3, 3, "b", "B")
        self._food_cap = 100
        self._food = 0
    
    def add_food(self, food) -> None:
        self._food = min(self._food_cap, self._food + food)
