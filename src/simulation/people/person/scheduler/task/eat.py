from src.simulation.people.person.person import Person
from task import Task
from src.simulation.simulation import Simulation


class Eat(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 10)

    def execute(self) -> None:
        if self._person.has_home():
            if not self._person.at_home():
                self._person.go_to_home()
            else:
                self._person.eat()
                self._finished()
        else:
            if not self._person.at_barn():
                self._person.find_barn_with_food()
            else:
                self._person.eat()
                self._finished()
