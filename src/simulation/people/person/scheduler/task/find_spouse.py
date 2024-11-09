from typing import override

from src.simulation.people.person.scheduler.task.task_type import TaskType
from task import Task

from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation


class FindSpouse(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)
        self._person = person

    @override
    def execute(self) -> None:
        if not self._person.has_spouse():
            for other in self._simulation.get_people_object().get_person_list():
                if not other.has_spouse():
                    self._person.assign_spouse(other)
                    other.assign_spouse(self._person)
                    # if both have house or just self does, assign other's home
                    if (other.has_spouse() and self._person.has_spouse()) or (self._person.has_home() and not other.has_home()):
                        other.get_home().remove_owner()
                        other.assign_home(self._person.get_home())
                    # if self doesn't have home
                    elif other.has_home() and not self._person.has_home():
                        self._person.assign_home(other.get_home())
                    else: #if both don't have house, then find one
                        self._person.get_scheduler().add(TaskType.FIND_HOME)
                        other.get_scheduler().add(TaskType.FIND_HOME)
                    # make sure they have the same house
                    break
        self._finished()

    @override
    def _clean_up_task(self) -> None:
        pass

    @override
    def get_remaining_time(self) -> int:
        pass
