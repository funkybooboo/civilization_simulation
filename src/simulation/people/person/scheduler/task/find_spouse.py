from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.simulation import Simulation


class FindSpouse(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 10)

    def execute(self) -> None:
        if self._person.has_spouse():
            for other in self._simulation.get_people_object().get_person_list():
                if not other.has_spouse():
                    self._person.assign_spouse(other)
                    other.assign_spouse(self._person)
                    # TODO: make sure they have the same house
                    self._finished()
                    break