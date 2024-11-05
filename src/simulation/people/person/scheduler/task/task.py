from abc import ABC, abstractmethod


class Task(ABC):
    def __init__(self, grid, person, priority):
        self._grid = grid
        self._person = person
        self._priority = priority  # 10 high to 1 low
        self._is_finished = False

    def __lt__(self, other):
        return self.get_priority() < other.get_priority()

    def get_priority(self):
        return self._priority

    def _finished(self):
        self._is_finished = True

    def is_finished(self):
        return self._is_finished

    @abstractmethod
    def execute(self):
        # move to the task
        # do the task
        pass
