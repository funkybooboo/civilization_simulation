from src.simulation.people.people import People
from src.simulation.people.person.scheduler.task.construction.build_barn import (
    BuildBarn,
)
from src.simulation.people.person.scheduler.task.construction.build_farm import (
    BuildFarm,
)
from src.simulation.people.person.scheduler.task.construction.build_home import (
    BuildHome,
)
from src.simulation.people.person.scheduler.task.construction.build_mine import (
    BuildMine,
)
from src.simulation.people.person.scheduler.task.eat import Eat
from src.simulation.people.person.scheduler.task.explore import Explore
from src.simulation.people.person.scheduler.task.find_home import FindHome
from src.simulation.people.person.scheduler.task.find_spouse import FindSpouse
from src.simulation.people.person.scheduler.task.start_construction.start_barn_construction import (
    StartBarnConstruction,
)
from src.simulation.people.person.scheduler.task.start_construction.start_farm_construction import (
    StartFarmConstruction,
)
from src.simulation.people.person.scheduler.task.start_construction.start_home_construction import (
    StartHomeConstruction,
)
from src.simulation.people.person.scheduler.task.start_construction.start_mine_construction import (
    StartMineConstruction,
)

from src.simulation.people.person.scheduler.task.transport import Transport
from src.simulation.people.person.scheduler.task.work.chop_tree import ChopTree
from src.simulation.people.person.scheduler.task.work.work_farm import WorkFarm
from src.simulation.people.person.scheduler.task.work.work_mine import WorkMine
from src.simulation.visualization.state.state import State


class TaskState(State):
    def __init__(self, people: People):
        self._people = people

        self._average_complete_task_count: float = (
            self._get_average_complete_task_count()
        )
        self._average_active_task_count: float = self._get_average_active_task_count()
        self._average_active_build_barn_task_count: float = (
            self._get_average_active_build_barn_task_count()
        )
        self._average_complete_build_barn_task_count: float = (
            self._get_average_complete_build_barn_task_count()
        )
        self._average_active_build_farm_task_count: float = (
            self._get_average_active_build_farm_task_count()
        )
        self._average_complete_build_farm_task_count: float = (
            self._get_average_complete_build_farm_task_count()
        )
        self._average_active_build_home_task_count: float = (
            self._get_average_active_build_home_task_count()
        )
        self._average_complete_build_home_task_count: float = (
            self._get_average_complete_build_home_task_count()
        )
        self._average_active_build_mine_task_count: float = (
            self._get_average_active_build_mine_task_count()
        )
        self._average_complete_build_mine_task_count: float = (
            self._get_average_complete_build_mine_task_count()
        )
        self._average_active_chop_tree_task_count: float = (
            self._get_average_active_chop_tree_task_count()
        )
        self._average_complete_chop_tree_task_count: float = (
            self._get_average_complete_chop_tree_task_count()
        )
        self._average_active_eat_task_count: float = (
            self._get_average_active_eat_task_count()
        )
        self._average_complete_eat_task_count: float = (
            self._get_average_complete_eat_task_count()
        )
        self._average_active_explore_task_count: float = (
            self._get_average_active_explore_task_count()
        )
        self._average_complete_explore_task_count: float = (
            self._get_average_complete_explore_task_count()
        )
        self._average_active_find_home_task_count: float = (
            self._get_average_active_find_home_task_count()
        )
        self._average_complete_find_home_task_count: float = (
            self._get_average_complete_find_home_task_count()
        )
        self._average_active_find_spouse_task_count: float = (
            self._get_average_active_find_spouse_task_count()
        )
        self._average_complete_find_spouse_task_count: float = (
            self._get_average_complete_find_spouse_task_count()
        )
        self._average_active_start_barn_construction_task_count: float = (
            self._get_average_active_start_barn_construction_task_count()
        )
        self._average_complete_start_barn_construction_task_count: float = (
            self._get_average_complete_start_barn_construction_task_count()
        )
        self._average_active_start_farm_construction_task_count: float = (
            self._get_average_active_start_farm_construction_task_count()
        )
        self._average_complete_start_farm_construction_task_count: float = (
            self._get_average_complete_start_farm_construction_task_count()
        )
        self._average_active_start_home_construction_task_count: float = (
            self._get_average_active_start_home_construction_task_count()
        )
        self._average_complete_start_home_construction_task_count: float = (
            self._get_average_complete_start_home_construction_task_count()
        )
        self._average_active_start_mine_construction_task_count: float = (
            self._get_average_active_start_mine_construction_task_count()
        )
        self._average_complete_start_mine_construction_task_count: float = (
            self._get_average_complete_start_mine_construction_task_count()
        )
        self._average_active_work_farm_task_count: float = (
            self._get_average_active_work_farm_task_count()
        )
        self._average_complete_work_farm_task_count: float = (
            self._get_average_complete_work_farm_task_count()
        )
        self._average_active_work_mine_task_count: float = (
            self._get_average_active_work_mine_task_count()
        )
        self._average_complete_work_mine_task_count: float = (
            self._get_average_complete_work_mine_task_count()
        )
        self._average_active_transport_task_count: float = (
            self._get_average_active_transport_task_count()
        )
        self._average_complete_transport_task_count: float = (
            self._get_average_complete_transport_task_count()
        )

        del self._people

    def _get_average_task_count_with_predicate(self, task_predicate: callable) -> float:
        total_count = 0.0
        for person in self._people:
            total_count += sum(
                1
                for task in person.get_scheduler().get_all_tasks()
                if task_predicate(task)
            )
        average = total_count / len(self._people) if self._people else 0.0
        return average

    def _get_average_complete_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: task.is_finished()
        )

    def _get_average_active_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: not task.is_finished()
        )

    def _get_average_active_build_barn_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildBarn) and not task.is_finished()
        )

    def _get_average_complete_build_barn_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildBarn) and task.is_finished()
        )

    def _get_average_active_build_farm_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildFarm) and not task.is_finished()
        )

    def _get_average_complete_build_farm_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildFarm) and task.is_finished()
        )

    def _get_average_active_build_home_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildHome) and not task.is_finished()
        )

    def _get_average_complete_build_home_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildHome) and task.is_finished()
        )

    def _get_average_active_build_mine_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildMine) and not task.is_finished()
        )

    def _get_average_complete_build_mine_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildMine) and task.is_finished()
        )

    def _get_average_active_chop_tree_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, ChopTree) and not task.is_finished()
        )

    def _get_average_complete_chop_tree_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, ChopTree) and task.is_finished()
        )

    def _get_average_active_eat_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, Eat) and not task.is_finished()
        )

    def _get_average_complete_eat_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, Eat) and task.is_finished()
        )

    def _get_average_active_explore_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, Explore) and not task.is_finished()
        )

    def _get_average_complete_explore_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, Explore) and task.is_finished()
        )

    def _get_average_active_find_home_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, FindHome) and not task.is_finished()
        )

    def _get_average_complete_find_home_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, FindHome) and task.is_finished()
        )

    def _get_average_active_find_spouse_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, FindSpouse) and not task.is_finished()
        )

    def _get_average_complete_find_spouse_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, FindSpouse) and task.is_finished()
        )

    def _get_average_active_start_barn_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartBarnConstruction)
            and not task.is_finished()
        )

    def _get_average_complete_start_barn_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartBarnConstruction) and task.is_finished()
        )

    def _get_average_active_start_farm_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartFarmConstruction)
            and not task.is_finished()
        )

    def _get_average_complete_start_farm_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartFarmConstruction) and task.is_finished()
        )

    def _get_average_active_start_home_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartHomeConstruction)
            and not task.is_finished()
        )

    def _get_average_complete_start_home_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartHomeConstruction) and task.is_finished()
        )

    def _get_average_active_start_mine_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartMineConstruction)
            and not task.is_finished()
        )

    def _get_average_complete_start_mine_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartMineConstruction) and task.is_finished()
        )

    def _get_average_active_work_farm_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, WorkFarm) and not task.is_finished()
        )

    def _get_average_complete_work_farm_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, WorkFarm) and task.is_finished()
        )

    def _get_average_active_work_mine_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, WorkMine) and not task.is_finished()
        )

    def _get_average_complete_work_mine_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, WorkMine) and task.is_finished()
        )

    def _get_average_active_transport_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, Transport) and not task.is_finished()
        )

    def _get_average_complete_transport_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, Transport) and task.is_finished()
        )
