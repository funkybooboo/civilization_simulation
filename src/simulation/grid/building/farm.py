from typing import Dict, override

import numpy as np
from building import Building

from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location
from src.simulation.people.person.person import Person


class Farm(Building):
    _max_worker_count = 3
    _max_work_count = 3

    def __init__(self, grid: Grid, location: Location) -> None:
        super().__init__(grid, location, 5, 5, "f", "F")
        self._workers: Dict[Person, int] = {}
        mean: float = 5
        std_dev: float = 2
        self._yield = lambda: np.random.normal(loc=mean, scale=std_dev, size=10)

    @override
    def has_capacity(self) -> bool:
        return len(self._workers) < Farm._max_worker_count

    @staticmethod
    @override
    def work_time_estimate() -> int:
        return Farm._max_work_count

    def work(self, person) -> int | None:
        if person in self._workers.keys():
            self._workers[person] += 1
        if len(self._workers) <= Farm._max_worker_count:
            self._workers[person] = 1
        if self._workers[person] > Farm._max_work_count:
            return int(self._yield())
        return None

    def remove_worker(self, person):
        del self._workers[person]
