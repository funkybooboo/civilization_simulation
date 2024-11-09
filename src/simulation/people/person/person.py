from typing import List, Optional, Set

from memory import Memory
from mover import Mover
from scheduler.scheduler import Scheduler
from scheduler.task.task_type import TaskType

from src.simulation.grid.building.building import Building
from src.simulation.grid.building.building_type import BuildingType
from src.simulation.grid.building.home import Home
from src.simulation.grid.location import Location
from src.simulation.simulation import Simulation


class Person:
    def __init__(
        self, simulation: Simulation, name: str, pk: int, location: Location, age: int
    ) -> None:
        self._name: str = name
        self._pk: int = pk
        self._age: int = age
        self._simulation = simulation

        self._location: Location = location
        self._memory: Memory = Memory()
        self._mover: Mover = Mover(simulation.get_grid(), self, self._memory, 10)

        self._health: int = 100
        self._hunger: int = (
            100  # when your hunger gets below 25, health starts going down; when it gets above 75, health starts going up
        )
        self._home: Optional[Home] = None
        self._spouse: Optional[Person] = None
        self._cycles_since_looked_for_spouse: int = 0
        self._scheduler: Scheduler = Scheduler(simulation, self)

        self._visited_buildings: Set[Building] = set()
        self._moving_to_building_type: Optional[BuildingType] = None
        self._building: Optional[Building] = None

    def take_action(self) -> None:
        self._add_tasks()
        self._scheduler.execute()

    def _add_tasks(self) -> None:
        self._hunger -= 1

        if self._hunger < 20:
            self._health -= 1
        elif self._hunger > 80:
            self._health += 1

        if not self._home:
            self._scheduler.add(TaskType.FIND_HOME)

        if not self._spouse:
            self._cycles_since_looked_for_spouse += 1
            if self._cycles_since_looked_for_spouse > 20: # TODO: change this to check for a spouse every year
                self._scheduler.add(TaskType.FIND_SPOUSE)
                self._cycles_since_looked_for_spouse = 0

        if self._hunger < 50:
            self._scheduler.add(TaskType.EAT)
        # todo figure out other actions

    def get_location(self) -> Location:
        return self._location

    def get_health(self) -> int:
        return self._health

    def get_hunger(self) -> int:
        return self._hunger
    
    def get_home(self) -> Optional[Home]:
        return self._home
    
    def get_spouse(self) -> Optional[Person]:
        return self._spouse

    def get_scheduler(self) -> Scheduler:
        return self._scheduler

    def set_location(self, other: Location) -> None:
        if not self._simulation.get_grid().is_location_in_bounds(other):
            raise Exception("You tried to put a person outside of the map")
        self._location = other

    def is_dead(self) -> bool:
        return self._health <= 0 or self._age >= 80

    def eat(self) -> None:
        if self.at_barn():
            # TODO: decrease hygiene? decrease health explicitly?
            self._hunger = min(self._hunger + 5, 100) # eating in a barn is less effective
        elif self.at_home():
            self._hunger = min(self._hunger + 10, 100)

    def assign_spouse(self, spouse: "Person") -> None:
        self._spouse = spouse

    def assign_home(self, home: Home) -> None:
        self._home = home

    def has_home(self) -> bool:
        return self._home is not None

    def has_spouse(self) -> bool:
        return self._spouse is not None
    
    def age(self) -> None:
        self._age += 1

    def remember_barns(self) -> Set[Location]:
        return self._memory.get_barn_locations()

    def remember_construction_barns(self) -> Set[Location]:
        return self._memory.get_construction_barn_locations()

    def remember_farms(self) -> Set[Location]:
        return self._memory.get_farm_locations()

    def remember_construction_farms(self) -> Set[Location]:
        return self._memory.get_construction_farm_locations()

    def remember_mines(self) -> Set[Location]:
        return self._memory.get_mine_locations()

    def remember_construction_mines(self) -> Set[Location]:
        return self._memory.get_construction_mine_locations()

    def remember_homes(self) -> Set[Location]:
        return self._memory.get_home_locations()

    def remember_construction_homes(self) -> Set[Location]:
        return self._memory.get_construction_home_locations()

    def remember_trees(self) -> Set[Location]:
        return self._memory.get_tree_locations()

    def remember_empties(self) -> Set[Location]:
        return self._memory.get_empties_locations()

    def remember_people(self) -> Set[Location]:
        return self._memory.get_people_locations()


    def find_build_location(self, building_type: BuildingType) -> Location:
        # check memory for open spots to build
        # if you cant find any then walk to a place where empty space is likely
        pass

    def find_tree_to_chop(self) -> None:
        pass

    def at_home(self) -> bool:
        if self.has_home():
            return self._mover.is_next_to([self._home._get_location()])
        else:
            return False

    def at_barn(self) -> bool:
        is_at_barn: bool = False
        # find all barns in grid
        all_barns = self._simulation.get_grid().get_barns()
        # check if person is next to any of them
        for barn in all_barns:
            if self._mover.is_next_to(barn._get_location()):
                is_at_barn = True
        return is_at_barn
    
    def at_farm(self) -> bool:
        pass

    def at_mine(self) -> bool:
        pass

    def explore(self) -> None:
        self._mover.explore()

    def build_home(self) -> None:
        # TODO: find a location for a house
        # TODO: add other tasks to gather supplies?
        pass

    def build_farm(self) -> None:
        pass

    def build_mine(self) -> None:
        pass

    def build_barn(self) -> None:
        pass

    def work_farm(self) -> None:
        pass

    def work_mine(self) -> None:
        pass

    def chop_tree(self) -> None:
        pass

    def store_stuff(self) -> None:
        pass

    def move_to_home(self) -> Optional[Home]:
        self._moving_to_building_type = BuildingType.HOME
        self._visited_buildings = set()
        self._building = self._home
        self._mover.towards(self._home.get_location())
        if self._location.is_one_away(self._home.get_location()):
            self._moving_to_building_type = None
            self._visited_buildings = set()
            self._building = None
            return self._home
        return None

    def move_to_time_estimate(self) -> int:
        if not self._building:  # the current building I am trying to get too
            return (
                5  # you haven't told me to go to a building_type yet, so I'm guessing 5
            )
        return (
            self._building.get_location().distance_to(self._location) // 10
        )  # move 10 blocks every action

    def move_to(self, building_type: BuildingType) -> Optional[Building]:
        # check if types are different
        if self._moving_to_building_type != building_type:
            self._moving_to_building_type = building_type
            self._visited_buildings = set()
            self._building = None

        if not self._building:
            if building_type == BuildingType.FARM:
                self._building = self._move_to(list(self._memory.get_farm_locations()))
            elif building_type == BuildingType.MINE:
                self._building = self._move_to(list(self._memory.get_mine_locations()))
            elif building_type == BuildingType.BARN:
                self._building = self._move_to(list(self._memory.get_barn_locations()))
            elif building_type == BuildingType.HOME:
                self._building = self._move_to(list(self._memory.get_home_locations()))
            else:
                raise Exception("You tried to go to a unknown building")

        if self._location.is_one_away(self._building.get_location()):
            if self._building.has_capacity():
                self._moving_to_building_type = None
                self._visited_buildings = set()
                self._building = None
                return self._building
            else:
                self._visited_buildings.add(self._building)
        return None

    def _move_to(self, locations: List[Location]) -> Building:
        visited_buildings_locations: List[Location] = [
            b.get_location() for b in self._visited_buildings
        ]
        filtered = list(
            filter(lambda l: not l in visited_buildings_locations, locations)
        )
        closest = self._mover.get_closest(filtered)
        self._mover.towards(closest)
        return self._simulation.get_grid().get_building(closest)
    
    def __str__(self) -> str:
        pass  # TODO implement what to print for a person
