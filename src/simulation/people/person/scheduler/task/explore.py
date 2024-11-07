from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.simulation import Simulation


class Explore(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 1) # very low priority, inessential task for when all else is done

    def execute(self) -> None:
        self._person.explore()
        self._finished()
