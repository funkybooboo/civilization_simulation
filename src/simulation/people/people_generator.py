import random
from typing import List

from src.simulation.grid.location import Location
from src.simulation.people.person.person import Person
from src.simulation.simulation import Simulation


class PeopleGenerator:
    def __init__(self, simulation: Simulation) -> None:
        home_count: int = simulation.get_grid().get_home_count()
        # Randomly assign 1 or 2 people per home, then calculate the total number of people
        total_people = sum(random.choice([1, 2]) for _ in range(home_count))
        self._max_pk = total_people
        self._simulation: Simulation = simulation

    @staticmethod
    def _get_names() -> List[str]:
        with open("../../../../data/first_names.txt", "r") as file:
            names: List[str] = [line.strip() for line in file if line.strip()]
        return names

    def generate(self) -> List[Person]:
        people: List[Person] = []
        names = self._get_names()
        for pk in range(self._max_pk):
            name: str = random.choice(names)
            location: Location = Location(
                20, 20
            )  # TODO place them in different valid spots near the town
            age: int = random.randint(20, 30)
            person: Person = Person(self._simulation, name, pk, location, age)
            people.append(person)
        return people
    
    def make_baby(self, location: Location) -> Person:
        name: str = random.choice(self._get_names())
        age: int = 0
        self._max_pk += 1
        person: Person = Person(self._simulation, name, self._max_pk, location, age)
        return person