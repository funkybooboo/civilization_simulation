from sched import scheduler
from typing import List, Optional, Set

from memory import Memory
from mover import Mover
from scheduler.scheduler import Scheduler
from scheduler.task.task_type import TaskType

from src.simulation.grid.building.barn import Barn
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
        self._scheduler: Scheduler = Scheduler(simulation, self)
        self._max_time: int = 10

        self._visited_buildings: Set[Building] = set()
        self._moving_to_building_type: Optional[BuildingType] = None
        self._building: Optional[Building] = None
        self._searched_building_count: int = 0
    
    def get_scheduler(self) -> Scheduler:
        return self._scheduler

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


        if self._simulation.get_people().get_time() % self._max_time == 0:
            if not self._spouse:
                self._scheduler.add(TaskType.FIND_SPOUSE)
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
    
    def get_spouse(self) -> Optional["Person"]:
        return self._spouse
    
    def get_age(self) -> int:
        return self._age

    def set_location(self, other: Location) -> None:
        if not self._simulation.get_grid().is_location_in_bounds(other):
            raise Exception("You tried to put a person outside of the map")
        self._location = other

    def is_dead(self) -> bool:
        return self._health <= 0 or self._age >= 80

    def is_satiated(self) -> bool:
        return self._person.get_hunger() >= 90

    def eat(self, building: Barn | Home) -> None:
        if isinstance(building, Home):
            building.remove_food(3)
            self._hunger = min(self._hunger + 10, 100)
        else:
            building.remove_food(3)
            self._hunger = min(self._hunger + 5, 100) # eating in a barn is less effective

    def assign_spouse(self, spouse: "Person") -> None:
        self._spouse = spouse

    def assign_home(self, home: Home) -> None:
        self._home = home

    def has_home(self) -> bool:
        return self._home is not None

    def start_home_construction(self) -> None:
        self._scheduler.add(TaskType.START_HOME_CONSTRUCTION)

    def has_spouse(self) -> bool:
        return self._spouse is not None
    
    def age(self) -> None:
        self._age += 1
        
    def find_build_location(self, building_type: BuildingType) -> Location:
        # check memory for open spots to build
        # if you cant find any then walk to a place where empty space is likely
        pass

    def get_home_locations(self):
        return self._memory.get_home_locations()

    def explore(self) -> None:
        self._mover.explore()

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
        # TODO: if you're eating, only go to barns that have food in them

        # check if types are different
        if self._moving_to_building_type != building_type:
            self._moving_to_building_type = building_type
            self._visited_buildings = set()
            self._building = None

        if not self._building:
            if building_type == BuildingType.FARM:
                buildings: List[Location] = list(self._memory.get_farm_locations())
                construction_type: TaskType = TaskType.START_FARM_CONSTRUCTION
            elif building_type == BuildingType.MINE:
                buildings: List[Location] = list(self._memory.get_mine_locations())
                construction_type: TaskType = TaskType.START_MINE_CONSTRUCTION
            elif building_type == BuildingType.BARN:
                buildings: List[Location] = list(self._memory.get_barn_locations())
                construction_type: TaskType = TaskType.START_BARN_CONSTRUCTION
            elif building_type == BuildingType.HOME:
                buildings: List[Location] = list(self._memory.get_home_locations())
                construction_type: TaskType = TaskType.START_HOME_CONSTRUCTION
            elif building_type == BuildingType.TREE:
                self._building = self._move_to(list(self._memory.get_tree_locations()))
            else:
                raise Exception("You tried to go to a unknown building")

            self._building = self._move_to(buildings)
            if not building_type == BuildingType.TREE and not self._building and self._searched_building_count >= (len(buildings) * 0.37):
                self._scheduler.add(construction_type)


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
