from src.simulation.people.people_generator import PeopleGenerator
from typing import List

from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation


class People:
    def __init__(self, simulation: Simulation, actions_per_day: int) -> None:
        self._actions_per_day: int = actions_per_day
        people_generator: PeopleGenerator = PeopleGenerator(simulation)
        self._people: List[Person] = people_generator.generate()

    def print(self) -> None:
        for person in self._people:
            print(person)

    def take_actions_for_day(self) -> None:
        for action in range(self._actions_per_day):
            dead: List[Person] = []
            for person in self._people:
                if person.is_dead():
                    dead.append(person)
                    continue
                person.take_action()
            for person in dead:
                self._people.remove(person)

    def age(self) -> None:
        for person in self._people:
            person.age()

    def match_people(self) -> None:
        for person in self._people:
            if not person.has_spouse():
                for other in self._people:
                    if not other.has_spouse():
                        person.assign_spouse(other)
                        other.assign_spouse(person)
                        # TODO: make sure they have the same house
                        break