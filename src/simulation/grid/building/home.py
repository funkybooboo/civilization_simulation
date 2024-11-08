from typing import override

from building import Building
from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location


class Home(Building):
    def __init__(self, grid: Grid, location: Location) -> None:
        super().__init__(grid, location, 2, 2, "h", "H")

    @override
    def has_capacity(self) -> bool:
        pass

    @staticmethod
    @override
    def work_time_estimate() -> int:
        pass
