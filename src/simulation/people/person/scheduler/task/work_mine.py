from typing import Optional, override

from src.simulation.grid.structure.store.barn import Barn
from src.simulation.grid.structure.work.mine import Mine
from task import Task
from src.simulation.grid.structure.structure_type import StructureType

from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation


class WorkMine(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)
        self._mine: Optional[Mine] = None
        self._stone: Optional[int] = None
        self._barn: Optional[Barn] = None

    @override
    def execute(self) -> None:
        if not self._mine:
            self._mine: Optional[Mine] = self._person.move_to(StructureType.MINE)
        if self._mine:
            if not self._stone:
                self._stone = self._mine.work(self._person)

            if self._stone:
                self._barn: Optional[Barn] = self._person.move_to(StructureType.BARN)
                if self._barn:
                    self._barn.add_resource("stone", self._stone)
                    self._finished()

    @override
    def _clean_up_task(self) -> None:
        self._mine.remove_worker(self._person)

    @override
    def get_remaining_time(self) -> int:
        return self._person.move_to_time_estimate() + self._mine.work_time_estimate() if self._mine else 3
