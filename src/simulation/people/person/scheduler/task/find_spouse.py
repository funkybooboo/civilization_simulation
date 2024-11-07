from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.simulation import Simulation


class FindSpouse(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 10)

    def execute(self) -> None:
        if person._spouse is None:
            for other in simulation.get_people():
                if not other.has_spouse():
                    person.assign_spouse(other)
                    other.assign_spouse(person)
                    # TODO: make sure they have the same house
                    break
