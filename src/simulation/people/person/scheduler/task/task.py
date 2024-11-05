from abc import ABC, abstractmethod


class Task(ABC):
    def __init__(self, simulation, person, priority):
        self._simulation = simulation
        self._person = person
        self._priority = priority  # 10 high to 1 low

    def __lt__(self, other):
        return self.get_priority() < other.get_priority()

    def get_priority(self):
        return self._priority

    @abstractmethod
    def execute(self):
        # move to the task
        # do the task
        pass
