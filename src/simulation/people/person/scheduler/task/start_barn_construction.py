from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.simulation import Simulation
from src.simulation.grid.grid import Grid

class StartBarnConstruction(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:


    def execute(self) -> None:
        # call a function in person
        # which calls a private function to set up the construction site
