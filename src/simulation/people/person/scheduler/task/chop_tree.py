from typing import override, Optional

from src.simulation.grid.structure.store.barn import Barn
from src.simulation.grid.structure.work.tree import Tree
from task import Task
from src.simulation.grid.structure.structure_type import StructureType
from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation


class ChopTree(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)
        self._tree: Optional[Tree] = None
        self._wood: Optional[int] = None
        self._barn: Optional[Barn] = None

    @override
    def execute(self) -> None:
        if not self._tree:
            self._tree: Optional[Tree] = self._person.move_to(StructureType.TREE)
        if self._tree:
            if not self._wood:
                self._wood = self._tree.work(self._person)

            if self._wood:
                self._barn: Optional[Barn] = self._person.move_to(StructureType.BARN)
                if self._barn:
                    self._barn.add_resource("wood", self._wood)
                    self._finished()

    @override
    def _clean_up_task(self) -> None:
        self._tree.remove_worker(self._person)

    @override
    def get_remaining_time(self) -> int:
        return self._person.move_to_time_estimate() + Tree.work_time_estimate()
