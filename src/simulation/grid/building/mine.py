from typing import override

from building import Building

from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location


class Mine(Building):
    def __init__(self, grid: Grid, location: Location) -> None:
        super().__init__(grid, location, 3, 3, "m", "M")

    @override
    def has_capacity(self) -> bool:
        pass

    @staticmethod
    @override
    def work_time_estimate() -> int:
        pass
