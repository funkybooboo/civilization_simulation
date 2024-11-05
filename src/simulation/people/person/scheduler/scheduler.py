import heapq
from typing import Optional, List

from src.simulation.people.person.scheduler.task.task_factory import TaskFactory
from src.simulation.people.person.scheduler.task.task import Task  # Assuming Task class is imported here


class Scheduler:
    def __init__(self, simulation: object, person: object) -> None:
        # TODO: maybe change how tasks are being stored?
        self._task_factory: TaskFactory = TaskFactory(simulation, person)
        self._tasks: List[Task] = []  # List of tasks, assuming Task is the type of tasks
        self._current_task: Optional[Task] = None  # Current task, could be None

    def add(self, what: str) -> None:
        task: Task = self._task_factory.create_instance(what)
        heapq.heappush(self._tasks, task)

    def _add(self, task: Task) -> None:
        heapq.heappush(self._tasks, task)

    def execute(self) -> None:
        if not self._current_task and not self._tasks:
            return
        if not self._current_task and self._tasks:
            self._current_task = heapq.heappop(self._tasks)

        self._add(self._current_task)
        next_task: Task = heapq.heappop(self._tasks)

        if self._current_task != next_task:
            self._current_task = next_task

        self._current_task.execute()
        if self._current_task.is_finished():
            self._current_task = None
