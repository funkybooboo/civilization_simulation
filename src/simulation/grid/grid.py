from typing import Tuple, Dict, List

from src.simulation.grid.grid_generator import GridGenerator


class Grid:
    def __init__(self, size: int) -> None:
        grid_generator = GridGenerator(size)
        self._width: int = size
        self._height: int = size
        self._grid: List[List[str]] = grid_generator.generate()
        self.buildings: Dict[str, List[Tuple[int, int]]] = self._find_buildings()

    def _find_buildings(self) -> Dict[str, List[Tuple[int, int]]]:
        buildings = {}
        for y in range(self._height):
            for x in range(self._width):
                cell = self._grid[y][x]
                if cell != " ":
                    if cell not in buildings:
                        buildings[cell] = []
                    buildings[cell].append((x, y))
        return buildings

    def is_valid_location_for_person(self, location: Tuple[int, int]) -> bool:
        if not self.is_location_in_bounds(location):
            return False
        if self.is_tree(location) or any(self.is_building(location, building) for building in self.buildings):
            return False
        return True

    def is_location_in_bounds(self, location: Tuple[int, int]) -> bool:
        x, y = location
        return 0 <= x < self._width and 0 <= y < self._height

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height

    def __str__(self) -> str:
        return "\n".join(" ".join(row) for row in self._grid)

    def grow_trees(self) -> None:
        pass

    def chop_down_tree(self, location: Tuple[int, int]) -> int:
        x, y = location
        if not self.is_tree(location):
            raise Exception(f"Tried to chop down a non-tree at location {location}")
        self._grid[y][x] = " "
        return 100

    def get_path_finding_matrix(self) -> List[List[int]]:
        pass

    def is_tree(self, location: Tuple[int, int]) -> bool:
        return self._is_item(location[0], location[1], "*")

    def is_barn(self, location: Tuple[int, int]) -> bool:
        return self._is_item(location[0], location[1], "B")

    def is_construction_barn(self, location: Tuple[int, int]) -> bool:
        return self._is_item(location[0], location[1], "b")

    def is_home(self, location: Tuple[int, int]) -> bool:
        return self._is_item(location[0], location[1], "H")

    def is_construction_home(self, location: Tuple[int, int]) -> bool:
        return self._is_item(location[0], location[1], "h")

    def is_farm(self, location: Tuple[int, int]) -> bool:
        return self._is_item(location[0], location[1], "F")

    def is_construction_farm(self, location: Tuple[int, int]) -> bool:
        return self._is_item(location[0], location[1], "f")

    def is_mine(self, location: Tuple[int, int]) -> bool:
        return self._is_item(location[0], location[1], "M")

    def is_construction_mine(self, location: Tuple[int, int]) -> bool:
        return self._is_item(location[0], location[1], "m")

    def is_empty(self, location: Tuple[int, int]) -> bool:
        return self._is_item(location[0], location[1], " ")

    def is_building(self, location: Tuple[int, int], building_char: str) -> bool:
        return self._is_item(location[0], location[1], building_char)

    def _is_item(self, x: int, y: int, char: str) -> bool:
        return self._grid[y][x] == char


if __name__ == "__main__":
    grid = Grid(75)
    print(grid)
