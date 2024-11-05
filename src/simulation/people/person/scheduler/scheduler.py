import heapq

from src.simulation.people.person.scheduler.task.task_factory import TaskFactory


class Scheduler:
    def __init__(self):
        # TODO: maybe change how tasks is being stored?
        self._task_factory = TaskFactory()
        self._tasks = []
        self._current_task = None

    def add(self, what):
        task = self._task_factory.create_instance(what)
        heapq.heappush(self._tasks, task)

    def _add(self, task):
        heapq.heappush(self._tasks, task)

    def get(self):
        if not self._tasks:
            return None
        task = heapq.heappop(self._tasks)
        if not task == self._current_task:
            self.add(self._current_task)
            self._current_task = task
        return self._current_task
