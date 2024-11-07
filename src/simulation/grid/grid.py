from copy import deepcopy
from typing import Dict, List

from location import Location
from grid_generator import GridGenerator
from building.barn import Barn
from building.building import Building
from building.farm import Farm
from building.home import Home
from building.mine import Mine


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
    
    # Define building sizes and types
    _building_info = {
        'H': (Home, 2, 2),   # Home
        'F': (Farm, 5, 5),   # Farm
        'B': (Barn, 3, 3),   # Barn
        'M': (Mine, 3, 3),   # Mine
        'h': (Home, 2, 2),   # Under construction Home
        'f': (Farm, 5, 5),   # Under construction Farm
        'b': (Barn, 3, 3),   # Under construction Barn
        'm': (Mine, 3, 3),   # Under construction Mine
    }
    
    def __init__(self, size: int) -> None:
        grid_generator = GridGenerator(size)
        self._width: int = size
        self._height: int = size
        self._grid: List[List[str]] = grid_generator.generate()
        self._buildings: Dict[Location, Building] = self._find_buildings() # stores the top left corner of every building
        
    def get_grid_deepcopy(self) -> List[List[str]]:
        return deepcopy(self._grid)
    
    def get_buildings_deepcopy(self) -> Dict[Location, Building]:
        return deepcopy(self._buildings)

    def _find_buildings(self) -> Dict[Location, Building]:
        buildings: Dict[Location, Building] = {}
        visited: set[Location] = set()  # Keep track of visited locations to avoid double-counting
    
        # Iterate over the grid and check each location
        for y in range(self._height):
            for x in range(self._width):
                location: Location = Location(x, y)
                cell = self._grid[y][x]
    
                # Skip empty spaces or trees
                if cell == " " or cell == "*":
                    continue
    
                # Skip if we've already visited this location
                if location in visited:
                    continue
    
                # Determine the type and size of the building
                if cell in self._building_info:
                    building_type, width, height = self._building_info[cell]
                else:
                    continue  # Unknown building type, skip it
    
                # Now, we need to verify that the building occupies the expected area
                for dy in range(height):
                    for dx in range(width):
                        building_location = Location(x + dx, y + dy)
                        if building_location not in visited:
                            visited.add(building_location)
    
                # Create a new building instance and associate it with the first location
                # (we could use the top-left corner as the "representative" location for each building)
                if location not in buildings:
                    building = building_type(location)
                    buildings[location] = building
                    # Add all the other locations in the building to map to the same building object
                    for dy in range(height):
                        for dx in range(width):
                            building_location = Location(x + dx, y + dy)
                            buildings[building_location] = building
    
        return buildings

    def is_valid_location_for_person(self, location: Location) -> bool:
        return self.is_empty(location)

    def is_location_in_bounds(self, location: Location) -> bool:
        return 0 <= location.x < self._width and 0 <= location.y < self._height

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height

    def __str__(self) -> str:
        return "\n".join(" ".join(row) for row in self._grid)

    def grow_trees(self) -> None:
        pass

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


if __name__ == "__main__":
    grid = Grid(75)
    print(grid)
