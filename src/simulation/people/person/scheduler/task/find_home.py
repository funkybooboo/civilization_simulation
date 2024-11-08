from typing import override

from task import Task


class FindHome(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)

    @override
    def execute(self) -> None:
        if not self._person.has_home():
            all_homes = self._simulation.get_grid().get_homes()
            # query the grid to make sure there is a home in that location
            for home in self._person._memory.get_homes():
                if home in all_homes:
                    if not home.has_owner():
                        self._person.assign_home(home)
                        home.assign_owner()
                        self._finished()
            # if all homes have owners, build a home (add build_home task)
            self._person.build_home()
        else:
            self._finished()

    @override
    def _clean_up_task(self) -> None:
        pass

    @override
    def get_remaining_time(self) -> int:
        pass
        
            