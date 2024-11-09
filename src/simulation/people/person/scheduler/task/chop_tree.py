from typing import override, Set, List, Optional

from task import Task
from src.simulation.grid.building.barn import Barn
from src.simulation.grid.building.building_type import BuildingType
from src.simulation.grid.building.tree import Tree
from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation
from src.simulation.grid.location import Location


class ChopTree(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)
        self._tree: Optional[Location] = None

    @override
    def execute(self) -> None:
        if not self._tree:
            self._tree: Optional[Tree] = self._person.move_to(BuildingType.TREE)
        if self._tree:
            wood: Optional[int] = self._tree.work(self._person)
            

            if wood:
                barn: Optional[Barn] = self._person.move_to(BuildingType.BARN)
                if barn:
                    barn.add_wood(wood)
                    self._finished()

    @override
    def _clean_up_task(self) -> None:

        pass

    @override
    def get_remaining_time(self) -> int:
        pass
