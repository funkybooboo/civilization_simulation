from typing import override

from task import Task

from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation

## search for empty space first,
# determine edge of town, go to edge of town
# then build
# if no space exists, add task clear land

class BuildBarn(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)
        self._person = person


    @override
    def execute(self) -> None:
        if self._person.remember_construction_barns() is not None:
            self._person._mover.get_closest(list(self._person.remember_construction_barns())


    @override
    def _clean_up_task(self) -> None:
        pass

    @override
    def get_remaining_time(self) -> int:
        pass
