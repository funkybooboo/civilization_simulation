from typing import List

from people_generator import PeopleGenerator
from person.person import Person

from ..simulation import Simulation
from .people_disaster_generator import PeopleDisasterGenerator


class People:
    def __init__(self, simulation: Simulation, actions_per_day: int) -> None:
        self._actions_per_day: int = actions_per_day
        people_generator: PeopleGenerator = PeopleGenerator(simulation)
        self._people: List[Person] = people_generator.generate()
        self._disaster_generator: PeopleDisasterGenerator = PeopleDisasterGenerator(
            self
        )
        self._time: int = 0

    def generate_disasters(self, chance: float = 0.50) -> None:
        self._disaster_generator.generate(chance)

    def print(self) -> None:
        for person in self._people:
            print(person)

    def take_actions_for_day(self) -> None:
        for action in range(self._actions_per_day):
            self._time += 1
            dead: List[Person] = []
            for person in self._people:
                if person.is_dead():
                    dead.append(person)
                    continue
                person.take_action()
            for person in dead:
                self._people.remove(person)

    def get_time(self) -> int:
        return self._time

    def age(self) -> None:
        for person in self._people:
            person.age()

    def __len__(self) -> int:
        return len(self._people)

    def get_average_health(self) -> float:
        average_health: float = 0.0
        for person in self._people:
            average_health += person.get_health()
        average_health /= len(self._people)
        return average_health

    def get_average_hunger(self) -> float:
        average_hunger: float = 0.0
        for person in self._people:
            average_hunger += person.get_hunger()
        average_hunger /= len(self._people)
        return average_hunger
