from people.person.person import Person
from people.person.scheduler.task.task import Task
from simulation import Simulation

class ChopTree(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5) # TODO: change the priority?
    
    def execute(self) -> None:
        # TODO: check if person is in a place with trees,
            # if not in a place with trees, go to a place with trees
        self._person.chop_tree()
        self._finished()
        