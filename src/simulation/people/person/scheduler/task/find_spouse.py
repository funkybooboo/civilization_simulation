from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.find_home import FindHome
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.people.person.scheduler.task.task_type import TaskType
from src.simulation.simulation import Simulation
from src.simulation.people.person.scheduler.scheduler import Scheduler


class FindSpouse(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 10)
        self._person = person
        self.spouse = person.has_spouse()
        self._simulation = simulation


    def execute(self) -> None:
        if self.spouse:
            for other in self._simulation.get_people(): #TODO: get people does not return what is expected for loop
                if not other.has_spouse():
                    self._person.assign_spouse(other)
                    other.assign_spouse(self._person)
                    if (other.has_home() and self._person.has_home()) or (self._person.has_home() and not other.has_home()):
                        other.assign_home(self._person.get_home())
                    elif other.has_home() and not self._person.has_home():
                        self._person.assign_home(other.get_home())
                    else:
                        self._person.get_scheduler().add(TaskType.FIND_HOME)
                    break
