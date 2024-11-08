from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.simulation import Simulation
from src.simulation.grid.grid import Grid

class BuildBarn(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5) # TODO: should the priority really be 5?
        self._grid = simulation.get_grid()
        self._location = person.get_location()


    def execute(self) -> None:
        # TODO: check if person is in buildable place,
            # if not in buildable place, go to buildable place
        build = self.is_clear()
        # check if there is a construction site
        # if not start construction
        #all tasks need return integer
        #

        #





        self._person.build_barn()
        self._finished()


    def is_clear(self) -> bool:
        clear = False
        for location in self._location.get_neighbors():
            char = Grid.get_char(self._grid, location)
            clear = char.isspace()
            if not clear: break

        return clear


    ## use get_closest or furthest
    ## is next to house or false etc for person methods