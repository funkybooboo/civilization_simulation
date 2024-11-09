from typing import Optional, override
from task import Task
from src.simulation.grid.building.building_type import BuildingType
from src.simulation.grid.building.mine import Mine
from src.simulation.grid.building.barn import Barn

from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation


class WorkMine(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)
        self._mine: Optional[Mine] = None

    @override
    def execute(self) -> None:
        if not self._mine:
            self._mine: Optional[Mine] = self._person.move_to(BuildingType.MINE)
        if self._mine:
            stone: Optional[int] = self._mine.work(self._person)

            if stone:
                barn: Optional[Barn] = self._person.move_to(BuildingType.BARN)
                if barn:
                    barn.add_stone(stone)
                    self._finished()

    @override
    def _clean_up_task(self) -> None:
        self._mine.remove_worker(self._person)

    @override
    def get_remaining_time(self) -> int:
        return self._person.move_to_time_estimate() + Mine.work_time_estimate()
