from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.people.person.scheduler.task.task_type import TaskType
from src.simulation.people.person.scheduler.task.eat import Eat
from src.simulation.people.person.scheduler.task.find_home import FindHome
from src.simulation.people.person.scheduler.task.find_spouse import FindSpouse
from people.person.scheduler.task.find_farm import FindFarm
from people.person.scheduler.task.find_mine import FindMine
from people.person.scheduler.task.find_tree import FindTree
from people.person.scheduler.task.find_barn import FindBarn
from people.person.scheduler.task.work_farm import WorkFarm
from people.person.scheduler.task.work_mine import WorkMine
from people.person.scheduler.task.chop_tree import ChopTree
from people.person.scheduler.task.store_stuff import StoreStuff
from people.person.scheduler.task.build_home import BuildHome
from people.person.scheduler.task.build_farm import BuildFarm
from people.person.scheduler.task.build_mine import BuildMine
from people.person.scheduler.task.build_barn import BuildBarn
from typing import Type

from src.simulation.simulation import Simulation


class TaskFactory:
    _constructors: dict[TaskType, Type] = {
        TaskType.EAT: Eat,
        TaskType.FIND_HOME: FindHome,
        TaskType.FIND_SPOUSE: FindSpouse,
        # TODO: add the rest of the tasks
        TaskType.FIND_FARM: FindFarm,
        TaskType.FIND_MINE: FindMine,
        TaskType.FIND_TREE: FindTree,
        TaskType.FIND_BARN: FindBarn,
        TaskType.WORK_FARM: WorkFarm,
        TaskType.WORK_MINE: WorkMine,
        TaskType.CHOP_TREE: ChopTree,
        TaskType.STORE_STUFF: StoreStuff,
        TaskType.BUILD_HOME: BuildHome,
        TaskType.BUILD_FARM: BuildFarm,
        TaskType.BUILD_MINE: BuildMine,
        TaskType.BUILD_BARN: BuildBarn
    }

    def __init__(self, simulation: Simulation, person: Person) -> None:
        self._simulation = simulation
        self._person = person

    def create_instance(self, what: TaskType) -> Task:
        task_class: Type = self._constructors[what]
        return task_class(self._simulation, self._person)
