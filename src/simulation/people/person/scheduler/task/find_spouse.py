from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.simulation import Simulation


class FindSpouse(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 10)
        self._person = person
        self.spouse = person.has_spouse()
        self._simulation = simulation

    def execute(self) -> None:
        if self.spouse:
            for other in self.simulation.get_people():
                if not other.has_spouse():
                    self._person.assign_spouse(other)
                    other.assign_spouse(self._person)
                    # TODO: make sure they have the same house
                    break
