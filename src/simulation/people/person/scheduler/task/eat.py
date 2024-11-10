from typing import override, Optional
from src.simulation.grid.building.barn import Barn
from src.simulation.grid.building.building_type import BuildingType
from src.simulation.grid.building.home import Home
from task import Task

from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation


class Eat(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)

        self._home: Optional[Home] = None
        self._barn: Optional[Barn] = None
        self._food: int = 0

    @override
    def execute(self) -> None:
        if self._person.is_satiated():
            self._finished()
            return

        if self._person.has_home():
            self._handle_home_food_logic()
        else:
            self._handle_barn_food_logic()

    def _handle_home_food_logic(self) -> None:
        self._home = self._person.move_to_home()

        if self._home:
            if self._food:
                self._deposit_food_at_home()
            elif self._home.has_food():
                self._eat_at_home()
            else:
                self._acquire_food_from_barn()

    def _deposit_food_at_home(self) -> None:
        self._person.move_to_home()
        self._home.add_food(self._food)
        self._food = 0

    def _eat_at_home(self) -> None:
        self._person.eat(self._home)
        self._finished()

    def _acquire_food_from_barn(self) -> None:
        if not self._barn:
            self._barn = self._person.move_to(BuildingType.BARN)

        if self._barn:
            self._food = self._barn.remove_food(self._home.get_food_capacity())
            # if the barn has no food, start working a farm to get food
            if self._food <= 0:
                self._person.work_farm()

    def _handle_barn_food_logic(self) -> None:
        if not self._barn:
            self._barn = self._person.move_to(BuildingType.BARN)

        if self._barn:
            self._person.eat(self._barn)
            self._finished()

    @override
    def _clean_up_task(self) -> None:
        self._home = None
        self._barn = None
        self._food = 0

    @override
    def get_remaining_time(self) -> int:
        return self._person.move_to_time_estimate() + 1
