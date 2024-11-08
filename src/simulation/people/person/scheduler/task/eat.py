from typing_extensions import override

from src.simulation.people.person.person import Person
from task import Task
from src.simulation.simulation import Simulation


class Eat(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 1)
    
    @override
    def execute(self) -> None:
        if not self._person.at_home():
            self._person.go_to_home()
        else:
            self._person.eat()
            self._finished()

    @override
    def get_remaining_time(self) -> int:
        return 3
