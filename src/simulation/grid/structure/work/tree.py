from typing import override

import numpy as np

from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location
from src.simulation.grid.structure.work.work import Work


class Tree(Work):
    def __init__(self, grid: Grid, location: Location) -> None:
        max_worker_count = 1
        max_work_count = 2
        super().__init__(grid, location, 1, 1, "*", max_worker_count, max_work_count)
    
    @override
    def _get_yield(self) -> float:
        """
        Yield logic for the Tree class, with a mean of 3 and a standard deviation of 1.
        """
        return np.random.normal(loc=3, scale=1)

    def __del__(self):
        self._grid.remove_tree(self._location)
