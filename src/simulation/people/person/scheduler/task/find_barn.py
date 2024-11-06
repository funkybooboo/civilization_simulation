from people.person.person import Person
from people.person.scheduler.task.task import Task
from simulation import Simulation

class FindBarn(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5) #TODO: change priority?
    
    def execute(self) -> None:
        if not self._person.at_barn():
            self._person.find_barn_to_store_at()
        else:
            self._finished()
