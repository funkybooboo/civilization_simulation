import random
from copy import deepcopy
from typing import Dict, List

from src.simulation.grid.structure.store.barn import Barn
from src.simulation.grid.structure.store.home import Home
from src.simulation.grid.structure.work.work import Work
from structure.structure import Structure
from grid_generator import GridGenerator
from location import Location
from src.logger import logger

from src.simulation.grid.structure.structure_factory import StructureFactory
from src.simulation.grid.structure.structure_type import StructureType
from src.simulation.grid.grid_disaster_generator import GridDisasterGenerator


class Grid:
    _char_to_num: Dict[str, int] = {
        "h": 10,
        "H": 0,
        "b": 10,
        "B": 0,
        "f": 3,
        "F": 5,
        "m": 0,
        "M": 0,
        " ": 1,
        "*": 10,
    }

    def __init__(self, size: int) -> None:
        grid_generator = GridGenerator(size)
        self._width: int = size
        self._height: int = size
        self._grid: List[List[str]] = grid_generator.generate()
        self._building_factory = StructureFactory(self)
        self._buildings: Dict[Location, Structure] = (
            self._find_buildings()
        )  # stores the top left corner of every structure
        self._disaster_generator = GridDisasterGenerator(self)

    def generate_disasters(self, chance: float = 0.50) -> None:
        self._disaster_generator.generate(chance)

    def get_grid(self) -> List[List[str]]:
        return self._grid

    def get_buildings_deepcopy(self) -> Dict[Location, Structure]:
        return deepcopy(self._buildings)
    
    def get_home_locations(self) -> List[Location]:
        home_locations = [location for location, building in self._buildings.items() if isinstance(building, Home)]
        return home_locations
    
    def _find_buildings(self) -> Dict[Location, Structure]:
        buildings: Dict[Location, Structure] = {}
        visited: set[Location] = (
            set()
        )  # Keep track of visited locations to avoid double-counting

        # Iterate over the grid and check each location
        for y in range(self._height):
            for x in range(self._width):
                location: Location = Location(x, y)

                # Skip empty spaces or trees
                if self.is_empty(location) or self.is_tree(location):
                    continue

                # Skip if we've already visited this location
                if location in visited:
                    continue

                if self.is_barn(location):
                    building_type = StructureType.BARN
                elif self.is_home(location):
                    building_type = StructureType.HOME
                elif self.is_mine(location):
                    building_type = StructureType.MINE
                elif self.is_farm(location):
                    building_type = StructureType.FARM
                elif self.is_construction_barn(location):
                    building_type = StructureType.CONSTRUCTION_BARN
                elif self.is_construction_farm(location):
                    building_type = StructureType.CONSTRUCTION_FARM
                elif self.is_construction_home(location):
                    building_type = StructureType.CONSTRUCTION_HOME
                elif self.is_construction_mine(location):
                    building_type = StructureType.CONSTRUCTION_MINE
                else:
                    continue

                # Create a new structure instance and associate it with the first location
                # (we could use the top-left corner as the "representative" location for each structure)
                if location not in buildings:
                    building = self._building_factory.create_instance(
                        building_type, location
                    )
                    if not building:
                        continue
                    buildings[location] = building

        return buildings
    
    def work_structures_exchange_memories(self):
        work_structures: List[Work] = list(filter(lambda b: not isinstance(b, Work), self._buildings.values()))
        for work_structure in work_structures:
            work_structure.exchange_worker_memories()

    def start_building_construction(self, building_type: StructureType, location: Location) -> None:
        try:
            building: Structure = self._building_factory.create_instance(building_type, location)
        except Exception as e:
            logger.error("Could not start structure construction", e)
            return
        self._buildings[location] = building

    def turn_completed_constructions_to_buildings(self):
        locations: List[Location] = list(self._buildings.keys())
        for location in locations:
            if self.is_construction_barn(location):
                building_type = StructureType.BARN
            elif self.is_construction_farm(location):
                building_type = StructureType.FARM
            elif self.is_construction_home(location):
                building_type = StructureType.HOME
            elif self.is_construction_mine(location):
                building_type = StructureType.MINE
            else:
                continue
            if self._buildings[location].has_capacity():
                continue
            self._buildings[location] = self._building_factory.create_instance(building_type, location)

    def get_buildings(self) -> Dict[Location, Structure]:
        return self._buildings

    def get_structure(self, location: Location) -> Structure:
        if self._grid[location.y][location.x] == "*" and location in self._buildings:
            # Create the tree and add it to the buildings list
            return self._building_factory.create_instance(StructureType.TREE, location)
        return self._buildings[location]

    def remove_tree(self, location: Location) -> None:
        self._grid[location.y][location.x] = " "

    def get_home_count(self) -> int:
        # Iterate through the values of the _buildings dictionary and count instances of Home
        return sum(
            1 for building in self._buildings.values() if isinstance(building, Home)
        )

    def get_char(self, location: Location) -> str:
        return self._grid[location.y][location.x]

    def is_location_char(self, location: Location, char: str) -> bool:
        return self._grid[location.y][location.x] == char

    def is_valid_location_for_person(self, location: Location) -> bool:
        return self.is_empty(location)

    def is_location_in_bounds(self, location: Location) -> bool:
        return 0 <= location.x < self._width and 0 <= location.y < self._height

    def __str__(self) -> str:
        return "\n".join(" ".join(row) for row in self._grid)

    def grow_trees(self, chance: int = 0.10) -> None:
        for i in range(len(self._grid)):
            for j in range(len(self._grid[i])):
                location: Location = Location(i, j)
                if not self.is_tree(location):
                    continue
                neighbors = location.get_neighbors()
                random.shuffle(neighbors)
                for neighbor in neighbors:
                    if not self.is_location_in_bounds(neighbor) or not self.is_empty(
                        neighbor
                    ):
                        continue
                    if random.random() < chance:
                        self._grid[neighbor.y][neighbor.x] = "*"  # Place a tree here
                        break

    def chop_down_tree(self, location: Location) -> int:
        if not self.is_tree(location):
            raise Exception(f"Tried to chop down a non-tree at location {location}")
        self._grid[location.y][location.x] = " "
        return 100

    def get_path_finding_matrix(self) -> List[List[int]]:
        path_finding_matrix: List[List[int | str]] = deepcopy(self._grid)
        for i in range(len(self._grid)):
            row = self._grid[i]
            for j in range(len(row)):
                cell = row[j]
                path_finding_matrix[i][j] = self._char_to_num[cell]
        return path_finding_matrix

    def get_barns(self) -> List[Barn]:
        return [building for building in self._buildings.values() if isinstance(building, Barn)]

    def is_tree(self, location: Location) -> bool:
        return self._is_item(location, "*")

    def is_barn(self, location: Location) -> bool:
        return self._is_item(location, "B")

    def is_construction_barn(self, location: Location) -> bool:
        return self._is_item(location, "b")

    def is_home(self, location: Location) -> bool:
        return self._is_item(location, "H")

    def is_construction_home(self, location: Location) -> bool:
        return self._is_item(location, "h")

    def is_farm(self, location: Location) -> bool:
        return self._is_item(location, "F")

    def is_construction_farm(self, location: Location) -> bool:
        return self._is_item(location, "f")

    def is_mine(self, location: Location) -> bool:
        return self._is_item(location, "M")

    def is_construction_mine(self, location: Location) -> bool:
        return self._is_item(location, "m")

    def is_empty(self, location: Location) -> bool:
        return self._is_item(location, " ")

    def is_building(self, location: Location, building_char: str) -> bool:
        return self._is_item(location, building_char)

    def _is_item(self, location: Location, char: str) -> bool:
        return self._grid[location.y][location.x] == char

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height


if __name__ == "__main__":
    grid = Grid(75)
    print(grid)
