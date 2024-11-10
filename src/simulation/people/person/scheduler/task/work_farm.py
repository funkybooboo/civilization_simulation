from typing import Optional, override

from src.simulation.grid.structure.store.barn import Barn
from src.simulation.grid.structure.structure_type import StructureType
from src.simulation.grid.structure.work.farm import Farm
from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.simulation import Simulation


class WorkFarm(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)
        self._farm: Optional[Farm] = None
        self._food: Optional[int] = None
        self._barn: Optional[Barn] = None

    @override
    def execute(self) -> None:
        if not self._farm:
            self._farm: Optional[Farm] = self._person.move_to(StructureType.FARM)
        if self._farm:
            if not self._food:
                self._food = self._farm.work(self._person)

            if self._food:
                self._barn: Optional[Barn] = self._person.move_to(StructureType.BARN)
                if self._barn:
                    self._barn.add_resource("food", self._food)
                    self._finished()

    @override
    def _clean_up_task(self) -> None:
        self._farm.remove_worker(self._person)

    @override
    def get_remaining_time(self) -> int:
        return self._person.move_to_time_estimate() + self._farm.work_time_estimate() if self._farm else 3
