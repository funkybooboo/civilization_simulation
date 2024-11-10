from typing import override

import numpy as np

from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location
from src.simulation.grid.structure.work.work import Work


class Farm(Work):
    def __init__(self, grid: Grid, location: Location) -> None:
        max_worker_count = 3
        max_work_count = 3
        super().__init__(grid, location, 5, 5, "F", max_worker_count, max_work_count)
    
    @override
    def _get_yield(self) -> float:
        """
        Yield logic for the Farm class, with a mean of 5 and a standard deviation of 2.
        """
        return np.random.normal(loc=5, scale=2)
