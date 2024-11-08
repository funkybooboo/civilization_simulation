from copy import deepcopy
import random
from typing import Dict, List

from location import Location
from grid_generator import GridGenerator
from building.barn import Barn
from building.building import Building
from building.farm import Farm
from building.home import Home
from building.mine import Mine
from src.simulation.grid.building.building_factory import BuildingFactory
from src.simulation.grid.building.building_type import BuildingType
from src.simulation.grid.grid_disaster_generator import GridDisasterGenerator


class Grid:
    _char_to_num: Dict[str, int] = {
        'h': 10,
        'H': 0,
        'b': 10,
        'B': 0,
        'f': 3,
        'F': 5,
        'm': 0,
        'M': 0,
        ' ': 1,
        '*': 10
    }
    
    def __init__(self, size: int) -> None:
        grid_generator = GridGenerator(size)
        self._width: int = size
        self._height: int = size
        self._grid: List[List[str]] = grid_generator.generate()
        self._building_factory = BuildingFactory(self)
        self._buildings: Dict[Location, Building] = self._find_buildings() # stores the top left corner of every building
        self._disaster_generator = GridDisasterGenerator(self)
    
    def generate_disasters(self, chance: float = 0.50) -> None:
        self._disaster_generator.generate(chance)

    def get_grid(self) -> List[List[str]]:
        return self._grid
    
    def get_buildings_deepcopy(self) -> Dict[Location, Building]:
        return deepcopy(self._buildings)

    def _find_buildings(self) -> Dict[Location, Building]:
        buildings: Dict[Location, Building] = {}
        visited: set[Location] = set()  # Keep track of visited locations to avoid double-counting
    
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
                    
                if self.is_barn(location) or self.is_construction_barn(location):
                    building_type = BuildingType.BARN
                elif self.is_home(location) or self.is_construction_home(location):
                    building_type = BuildingType.HOME
                elif self.is_mine(location) or self.is_construction_mine(location):
                    building_type = BuildingType.MINE
                elif self.is_farm(location) or self.is_construction_farm(location):
                    building_type = BuildingType.FARM
                else:
                    continue
    
                # Create a new building instance and associate it with the first location
                # (we could use the top-left corner as the "representative" location for each building)
                if location not in buildings:
                    building = self._building_factory.create_instance(building_type, location)
                    if not building:
                        continue
                    buildings[location] = building
                    # Add all the other locations in the building to map to the same building object
                    for dy in range(building.get_height()):
                        for dx in range(building.get_width()):
                            building_location = Location(x + dx, y + dy)
                            buildings[building_location] = building
    
        return buildings
    
    def get_buildings(self) -> Dict[Location, Building]:
        return self._buildings

    def home_count(self) -> int:
        # Iterate through the values of the _buildings dictionary and count instances of Home
        return sum(1 for building in self._buildings.values() if isinstance(building, Home))

    def get_char(self, location: Location) -> str:
        return self._grid[location.y][location.x]

    def is_location_char(self, location: Location, char: str) -> bool:
        return self._grid[location.y][location.x] == char

    def get_home_count(self) -> int:
        return sum(1 for building in self._buildings.values() if isinstance(building, Home))

    def get_construction_home_count(self) -> int:
        return sum(1 for building in self._buildings.values() if isinstance(building, Home) and building.is_under_construction())

    def get_barn_count(self) -> int:
        return sum(1 for building in self._buildings.values() if isinstance(building, Barn))

    def get_construction_barn_count(self) -> int:
        return sum(1 for building in self._buildings.values() if isinstance(building, Barn) and building.is_under_construction())

    def get_farm_count(self) -> int:
        return sum(1 for building in self._buildings.values() if isinstance(building, Farm))

    def get_construction_farm_count(self) -> int:
        return sum(1 for building in self._buildings.values() if isinstance(building, Farm) and building.is_under_construction())

    def get_mine_count(self) -> int:
        return sum(1 for building in self._buildings.values() if isinstance(building, Mine))

    def get_construction_mine_count(self) -> int:
        return sum(1 for building in self._buildings.values() if isinstance(building, Mine) and building.is_under_construction())

    def get_tree_count(self) -> int:
        count: int = 0
        for i in range(len(self._grid)):
            for j in range(len(self._grid[i])):
                location: Location = Location(i, j)
                if self.is_tree(location):
                    count += 1
        return count

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
                    if not self.is_location_in_bounds(neighbor) or not self.is_empty(neighbor):
                        continue
                    if random.random() < chance:
                        self._grid[neighbor.y][neighbor.x] = '*'  # Place a tree here
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
