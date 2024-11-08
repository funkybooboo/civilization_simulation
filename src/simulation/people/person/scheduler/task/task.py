from abc import ABC, abstractmethod

from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation


class Task(ABC):
    def __init__(self, simulation: Simulation, person: Person, priority: int) -> None:
        self._simulation: Simulation = simulation
        self._person: Person = person
        self._priority: int = priority  # 10 high to 1 low
        self._is_finished: bool = False
        self._interruptions: int = 0

    def __lt__(self, other: "Task") -> bool:
        return self.get_priority() < other.get_priority()
    
    def get_interruptions(self) -> int:
        return self._interruptions
    
    def increment_interruptions(self) -> None:
        self._interruptions += 1

    def get_priority(self) -> int:
        return self._priority

    def _finished(self) -> None:
        self._is_finished = True

    def is_finished(self) -> bool:
        return self._is_finished

    @abstractmethod
    def execute(self) -> None:
        # move to the task
        # do the task
        pass
    
    @abstractmethod
    def get_remaining_time(self) -> int:
        # ballpark: how many action cycles will this task take?
        pass
