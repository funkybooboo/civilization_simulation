from typing import override, Set, List

from task import Task

from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation
from src.simulation.grid.location import Location


class ChopTree(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)
        self._tree: Location = None

    @override
    def execute(self) -> None:
        if not self._tree:
            tree_locations: Set[Location] = self._person._memory.get_tree_locations()
            tree_locations_list: List[Location] = list(tree_locations)
            if tree_locations:
                self._tree = self._person._mover.get_closest(tree_locations)
                self._person.move_to()

    @override
    def _clean_up_task(self) -> None:
        pass

    @override
    def get_remaining_time(self) -> int:
        pass
