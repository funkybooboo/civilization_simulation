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
        self._interruption_threshold = 3  # Threshold for how many interruptions before "sticking" to the task

    def add(self, what: TaskType) -> None:
        task: Task = self._task_factory.create_instance(what)
        if task:
            heapq.heappush(self._tasks, task)

    def _add(self, task: Optional[Task]) -> None:
        if task:
            heapq.heappush(self._tasks, task)

    def _pop(self) -> Optional[Task]:
        return heapq.heappop(self._tasks) if self._tasks else None

    def execute(self) -> None:
        if not self._current_task and not self._tasks:
            return  # No tasks to execute

        if not self._current_task and self._tasks:
            self._current_task = self._pop()  # Get the first task if none is currently being worked on

        # If the current task has been interrupted enough times, stick with it
        if self._current_task and self._current_task.get_interruptions() >= self._interruption_threshold:
            self._current_task.execute()
            if self._current_task.is_finished():
                self._current_task = None  # Task is done, so remove it
            return

        # Re-add the current task to the queue (if it exists) to check for higher-priority tasks
        self._add(self._current_task)
        next_task: Optional[Task] = self._pop()

        # If the next task is of higher priority, stop the current task and start the new one
        if self._current_task != next_task:
            self._current_task.increment_interruptions()  # Increment interruptions for the current task
            self._current_task = next_task  # Switch to the new task

        self._current_task.execute()

        # If the task is finished, discard it from the scheduler
        if self._current_task.is_finished():
            self._current_task = None
