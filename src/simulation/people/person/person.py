from typing import Optional
from typing import List, Set

from src.simulation.grid.building.home import Home
from src.simulation.grid.location import Location
from memory import Memory
from mover import Mover
from scheduler.scheduler import Scheduler
from scheduler.task.task_type import TaskType
from src.simulation.simulation import Simulation


class Person:
    def __init__(
        self, simulation: Simulation, name: str, pk: int, location: Location, age: int
    ) -> None:
        self._name: str = name
        self._pk: int = pk
        self._age: int = age

        self._location: Location = location
        self._memory: Memory = Memory()
        self._mover: Mover = Mover(simulation.get_grid(), self, self._memory, 10)

        self._health: int = 100
        self._hunger: int = (
            100  # when your hunger gets below 25, health starts going down; when it gets above 75, health starts going up
        )
        self._home: Optional[Home] = None  # Home can be None or an object (e.g., Home)
        # todo self.home needs to be adjusted so that it provides location
        self._spouse: Optional[Person] = (
            None  # Spouse can be None or an object (e.g., Person)
        )
        self._scheduler: Scheduler = Scheduler(simulation, self)

    def take_action(self) -> None:
        self._determine_actions()
        self._scheduler.execute()

    def _determine_actions(self) -> None:
        self._hunger -= 1  # TODO adjust

        if self._hunger < 20:
            self._health -= 1
        elif self._hunger > 80:
            self._health += 1

        if not self.has_home():
            self._scheduler.add(TaskType.FIND_HOME)

        if not self.has_spouse():
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

    def set_location(self, other: Location) -> None:
        # TODO check if its in bounds
        self._location = other

    def is_dead(self) -> bool:
        return self._health <= 0 or self._age >= 80

    def eat(self) -> None:
        self._hunger = min(self._hunger + 10, 100)

    def assign_spouse(self, spouse: "Person") -> None:
        self._spouse = spouse

    def has_spouse(self) -> bool:
        return self._spouse is not None

    def assign_home(self, home: Home) -> None:
        self._home = home

    def get_home(self) -> Home:
        return self._home

    def has_home(self) -> bool:
        return self._home is not None

    def get_scheduler(self) -> Scheduler:
        return self._scheduler
    
    def age(self) -> None:
        self._age += 1

    def at_home(self) -> bool:
        pass

    def at_barn(self) -> bool:
        pass

    def at_farm(self) -> bool:
        pass

    def at_mine(self) -> bool:
        pass

    def at_home_construction(self) -> bool:
        pass

    def at_barn_construction(self) -> bool:
        pass

    def at_mine_construction(self) -> bool:
        pass

    def at_farm_construction(self) -> bool:
        pass

    def go_to_home(self) -> None:
        self._mover.towards(self._home)

    def go_to_random_spot(self) -> None:
        self._mover.explore()

    def find_farm_to_work_at(self) -> None:
        self._mover.towards(self._mover.get_closest(self._location, list(self.remember_farms())))

    def find_mine_to_work_at(self) -> None:
        self._mover.towards(self._mover.get_closest(self._location, list(self.remember_mines())))

    def find_tree_to_chop(self) -> None:
        self._mover.towards(self._mover.get_closest(self._location, list(self.remember_trees())))

    def find_barn_to_store_at(self) -> None:
        self._mover.towards(self._mover.get_closest(self._location, list(self.remember_barns())))

    def build_home(self) -> None:
        pass

    def build_farm(self) -> None:
        pass

    def build_mine(self) -> None:
        pass

    def build_barn(self) -> None:
        pass
    # query memory of construction barns
    # start construction

    ## also add has spouse function
    ## create private build method start construct
    # query from memory

    # maybe still have start construction class



    def work_farm(self) -> None:
        pass

    def work_mine(self) -> None:
        pass

    def chop_tree(self) -> None:
        pass

    def store_stuff(self) -> None:
        pass

    def remember_barns(self) -> Set[Location]:
        return self._memory.remember('barns')

    def remember_construction_barns(self) -> Set[Location]:
        return self._memory.remember('construction_barns')

    def remember_farms(self) -> Set[Location]:
        return self._memory.remember('farms')

    def remember_construction_farms(self) -> Set[Location]:
        return self._memory.remember('construction_farms')

    def remember_mines(self) -> Set[Location]:
        return self._memory.remember('mines')

    def remember_construction_mines(self) -> Set[Location]:
        return self._memory.remember('construction_mines')

    def remember_homes(self) -> Set[Location]:
        return self._memory.remember('homes')

    def remember_construction_homes(self) -> Set[Location]:
        return self._memory.remember('construction_homes')

    def remember_trees(self) -> Set[Location]:
        return self._memory.remember('trees')

    def remember_empties(self) -> Set[Location]:
        return self._memory.remember('empties')

    def remember_people(self) -> Set[Location]:
        return self._memory.remember('people')


    def __str__(self) -> str:
        pass  # TODO implement what to print for a person
