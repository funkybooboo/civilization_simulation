from typing import Dict, override, Optional

import numpy as np
from building import Building

from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location
from src.simulation.people.person.person import Person


class Mine(Building):
    _max_worker_count = 6
    _max_work_count = 4

    def __init__(self, grid: Grid, location: Location) -> None:
        super().__init__(grid, location, 3, 3, "m", "M")
        self._workers: Dict[Person, int] = {}
        mean: float = 4
        std_dev: float = 1
        self._yield = lambda: np.random.normal(loc=mean, scale=std_dev, size=10)

    @override
    def has_capacity(self) -> bool:
        return len(self._workers) < Mine._max_worker_count

    @staticmethod
    @override
    def work_time_estimate() -> int:
        return Mine._max_work_count
    
    def work(self, person) -> Optional[int]:
        if person in self._workers.keys():
            self._workers[person] += 1
        if len(self._workers) <= Mine._max_worker_count:
            self._workers[person] = 1
        if self._workers[person] > Mine._max_work_count:
            self.remove_worker(person)
            return int(self._yield())
        return None
    
    def remove_worker(self, person):
        del self._workers[person]
