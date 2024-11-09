from typing import override

from task import Task

from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation


class Explore(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)
        self._max_how_far: int = 5
        self._how_far: int = 0

    @override
    def execute(self) -> None:
        self._how_far += 1
        self._person.explore()
        if self._how_far >= self._max_how_far:
            self._finished()

    @override
    def _clean_up_task(self) -> None:
        pass

    @override
    def get_remaining_time(self) -> int:
        pass
