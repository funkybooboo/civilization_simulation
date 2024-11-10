from abc import ABC
from typing import override

from typing_extensions import Optional

from src.simulation.grid.structure.store.store import Store
from src.simulation.grid.structure.structure_type import StructureType
from src.simulation.grid.structure.work.work import Work as WorkStructure
from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.simulation import Simulation


class Work(Task, ABC):
    def __init__(
            self, 
            simulation: Simulation, 
            person: Person, 
            priority: int,
            work_structure: StructureType, 
            store_structure: Optional[StructureType],
            resource_name: str
    ) -> None:
        super().__init__(simulation, person, priority)
        self._work_structure: StructureType = work_structure
        self._store_structure: StructureType = store_structure
        self._resource_name: str = resource_name
        
        self._work: Optional[WorkStructure] = None
        self._resource: Optional[int] = None
        self._store: Optional[Store] = None

    @override
    def execute(self) -> None:
        if self._work:
            if not self._resource:
                self._resource = self._work.work(self._person)
                if self._resource:
                    self._store: Optional[Store] = self._person.move_to_workable_structure(self._store_structure)
                    if self._store:
                        self._store.add_resource(self._resource_name, self._resource)
                        self._finished()
        else:
            self._work: Optional[WorkStructure] = self._person.move_to_workable_structure(self._work_structure)

    @override
    def _clean_up_task(self) -> None:
        if self._work:
            self._work.remove_worker(self._person)

    @override
    def get_remaining_time(self) -> int:
        return self._person.move_to_time_estimate() + self._work.work_time_estimate() if self._work else 3
