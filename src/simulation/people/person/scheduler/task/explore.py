from typing import override

from task import Task

from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation


class Explore(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)

    @override
    def execute(self) -> None:
        self._person.explore()
        self._finished()

    @override
    def _clean_up_task(self) -> None:
        pass

    @override
    def get_remaining_time(self) -> int:
        pass
