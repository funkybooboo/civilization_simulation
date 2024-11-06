from people.person.person import Person
from people.person.scheduler.task.task import Task
from simulation import Simulation

class BuildBarn(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5) # TODO: should the priority really be 5?
    
    def execute(self) -> None:
        # TODO: check if person is in buildable place,
            # if not in buildable place, go to buildable place
        self._person.build_barn()
        self._finished()