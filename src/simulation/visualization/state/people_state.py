from src.simulation.people.people import People
from src.simulation.visualization.state.state import State


class PeopleState(State):
    def __init__(self, people: People):
        self._people: People = people

        self._people_count: int = len(people)
        self._average_health: float = self._get_average_health()
        self._average_hunger: float = self._get_average_hunger()
        
        del self._people

    def _get_average_health(self) -> float:
        average_health: float = 0.0
        for person in self._people:
            average_health += person.get_health()
        average_health /= len(self._people)
        return average_health

    def _get_average_hunger(self) -> float:
        average_hunger: float = 0.0
        for person in self._people:
            average_hunger += person.get_hunger()
        average_hunger /= len(self._people)
        return average_hunger
