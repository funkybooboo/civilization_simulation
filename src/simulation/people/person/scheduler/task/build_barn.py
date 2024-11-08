from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.simulation import Simulation
from src.simulation.grid.grid import Grid

class BuildBarn(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5) # TODO: should the priority really be 5?
        self._grid = simulation.get_grid()
        self._person = person
        self._location = person.get_location()


    def execute(self) -> None:
        # TODO: check if person is in buildable place,
            # if not in buildable place, go to buildable place
        for construction_site in self._person.remember_construction_barns():
            self._person.
        # pseudocode below:
        #check person memory for construction site
        # if construction site for barn, go to barn and help build
        # go do building stuff at barn

        # else search for empty places to build barn #this goes into the start barn construction
        # once a place is found, go to it and check
        # add start barn construction task
        # call person build barn
        # call finished when finished



        #all tasks need return integer of how long its estimated to take
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