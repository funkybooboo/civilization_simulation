from src.simulation.grid.structure.store.home import Home
from task import Task
from typing import override

from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation

class FindHome(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)

    @override
    def execute(self) -> None:
        if not self._person.has_home():
            all_home_locations = self._simulation.get_grid().get_home_locations()
            # query the grid to make sure there is a home in that location
            for home_location in self._person.get_home_locations():
                if home_location in all_home_locations:
                    home: Home = self._simulation.get_grid().get_structure(home_location)

                    if not home.has_owner():
                        self._person.assign_home(home)

                        if self._person.has_spouse():
                            self._person.get_spouse().assign_home(home)
                        
                        home.assign_owner()
                        self._finished()
                        return

            # if all homes have owners, build a home (add build_home task)
            self._person.start_home_construction()
        else:
            self._finished()

    @override
    def _clean_up_task(self) -> None:
        pass

    @override
    def get_remaining_time(self) -> int:
        return 0
