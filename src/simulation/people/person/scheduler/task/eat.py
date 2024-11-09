from typing import override, Optional
from src.simulation.grid.building.barn import Barn
from src.simulation.grid.building.building_type import BuildingType
from task import Task

from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation


class Eat(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)

        self._barn: Optional[Barn] = None

    @override
    def execute(self) -> None:        
        if self._person.has_home():
            if not self._person.at_home():
                self._person.move_to_home()
            else:
                self._person.eat()
                self._finished()
        else:
            if not self._barn:
                self._barn: Optional[Barn] = self._person.move_to(BuildingType.BARN) # TODO: make sure this barn has food in it
            if self._barn:
                self._person.eat()
                self._finished()

    @override
    def _clean_up_task(self) -> None:
        pass

    @override
    def get_remaining_time(self) -> int:
        pass
