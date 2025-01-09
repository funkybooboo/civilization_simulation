from __future__ import annotations

import os
import random
from copy import deepcopy
from typing import TYPE_CHECKING, List

from src.logger import logger
from src.settings import settings
from src.simulation.grid.structure.store.home import Home
from src.simulation.people.person.person import Person

if TYPE_CHECKING:
    from src.simulation.grid.location import Location
    from src.simulation.simulation import Simulation


class PeopleGenerator:
    def __init__(self, simulation: Simulation) -> None:
        self._grid = simulation.get_grid()
        home_count: int = self._grid.get_structure_count(Home)
        # Randomly assign 1 or 2 people per home, then calculate the total number of people
        total_people = sum(random.choice([1, 2]) for _ in range(home_count))
        self._max_pk = total_people
        self._simulation: Simulation = simulation

    @staticmethod
    def _get_names() -> List[str]:
        try:
            # Get the directory of the current script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Construct the absolute path to the file
            file_path = os.path.join(script_dir, "../../../data/first_names.txt")
            with open(file_path, "r") as file:
                names: List[str] = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            logger.error("Could not find names file. Using default names.")
            names: List[str] = [
                "James",
                "John",
                "Robert",
                "Michael",
                "William",
                "David",
                "Joseph",
                "Charles",
                "Thomas",
                "Daniel",
                "Emma",
                "Olivia",
                "Sophia",
                "Isabella",
                "Ava",
                "Mia",
                "Amelia",
                "Harper",
                "Evelyn",
                "Abigail",
            ]
        return names

    def generate(self) -> List[Person]:
        logger.debug("Generating people...")
        people: List[Person] = []
        names: List[str] = self._get_names()
        empty_spots_near_town: List[Location] = self._grid.get_empty_spots_near_town()
        for pk in range(self._max_pk):
            name: str = random.choice(names)
            location: Location = deepcopy(random.choice(empty_spots_near_town))
            age: int = random.randint(
                settings.get("inital_spawn_age_min", 20), settings.get("inital_spawn_age_max", 30)
            )
            person: Person = self._make_person(name, pk, location, age)
            people.append(person)
        logger.info(f"Generated {len(people)} people")
        return people

    def make_baby(self, location: Location) -> Person:
        name: str = random.choice(self._get_names())
        age: int = 0
        self._max_pk += 1
        person: Person = self._make_person(name, self._max_pk, location, age)
        logger.info(f"Baby {name} was born!")
        return person

    def _make_person(self, name, pk, location, age) -> Person:
        building_locations = list(self._grid.get_buildings().keys())
        return Person(self._simulation, name, pk, location, age, building_locations)
