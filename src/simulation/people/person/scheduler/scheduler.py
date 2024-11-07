import heapq
from typing import List, Optional

from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.people.person.scheduler.task.task_factory import TaskFactory
from src.simulation.people.person.scheduler.task.task_type import TaskType
from src.simulation.simulation import Simulation


class Scheduler:
    def __init__(self, simulation: Simulation, person: Person) -> None:
        self._task_factory: TaskFactory = TaskFactory(simulation, person)
        self._tasks: List[Task] = []
        self._current_task: Optional[Task] = None
        self._last_added_time = 0  # Timestamp for when the last task was added
        self._interruption_threshold = 3  # Initial threshold
        self._max_interruption_threshold = 10  # Cap on how high the threshold can go
        self._simulation = simulation  # Store the simulation reference to access the time

    def add(self, what: TaskType) -> None:
        task: Task = self._task_factory.create_instance(what)
        if task:
            heapq.heappush(self._tasks, task)
            self._last_added_time = self._get_current_time()

    def _add(self, task: Optional[Task]) -> None:
        if task:
            heapq.heappush(self._tasks, task)

    def _pop(self) -> Optional[Task]:
        return heapq.heappop(self._tasks) if self._tasks else None

    def _get_current_time(self) -> int:
        # Get the current time from the simulation (assumes simulation has a time attribute)
        return self._simulation.get_day()  # Replace with actual time tracking mechanism in the simulation

    def _calculate_dynamic_threshold(self) -> int:
        base_threshold = max(1, len(self._tasks) // 2)

        task_addition_rate_factor = 1 if self._get_current_time() - self._last_added_time > 1 else 2

        if self._current_task:
            priority_factor = 1 if self._current_task.get_priority() == 1 else 3
        else:
            priority_factor = 3

        dynamic_threshold = min(self._max_interruption_threshold, base_threshold * task_addition_rate_factor * priority_factor)

        return dynamic_threshold

    def execute(self) -> None:
        if not self._current_task and not self._tasks:
            return

        if not self._current_task and self._tasks:
            self._current_task = self._pop()

        self._interruption_threshold = self._calculate_dynamic_threshold()

        if self._current_task and self._current_task.get_interruptions() >= self._interruption_threshold:
            self._current_task.execute()
            if self._current_task.is_finished():
                self._current_task = None
            return

        self._add(self._current_task)
        next_task: Optional[Task] = self._pop()

        if self._current_task != next_task:
            self._current_task.increment_interruptions()
            self._current_task = next_task

        self._current_task.execute()

        if self._current_task.is_finished():
            self._current_task = None
