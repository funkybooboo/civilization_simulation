from typing import Dict

from src.simulation.people.people import People
from src.simulation.visualization.state.state import State


class PeopleDisasterState(State):
    def __init__(self, people: People):
        # Get disaster counts from the PeopleDisasterGenerator
        disaster_counts: Dict[str, int] = people.get_disaster_counts()

        # Initialize disaster attributes based on counts
        self._divorce = disaster_counts.get("divorce", 0)
        self._sickness = disaster_counts.get("sickness", 0)
        self._craving = disaster_counts.get("craving", 0)
        self._death = disaster_counts.get("death", 0)
        self._forget_tasks = disaster_counts.get("forget_tasks", 0)
        self._sleepwalk = disaster_counts.get("sleepwalk", 0)
        self._so_many_babies = disaster_counts.get("so_many_babies", 0)
