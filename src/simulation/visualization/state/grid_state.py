from src.simulation.grid.grid import Grid
from src.simulation.grid.building.barn import Barn
from src.simulation.grid.building.farm import Farm
from src.simulation.grid.building.home import Home
from src.simulation.grid.building.mine import Mine
from src.simulation.grid.location import Location


class GridState:
    def __init__(self, grid: Grid):
        self._grid = grid

        self._barn_count: int = self._get_barn_count()
        self._construction_barn_count: int = self._get_construction_barn_count()
        self._farm_count: int = self._get_farm_count()
        self._construction_farm_count: int = self._get_construction_farm_count()
        self._mine_count: int = self._get_mine_count()
        self._construction_mine_count: int = self._get_construction_mine_count()
        self._home_count: int = grid.get_home_count()
        self._construction_home_count: int = self._get_construction_home_count()
        self._tree_count: int = self._get_tree_count()
        
        del self._grid

    def _get_construction_home_count(self) -> int:
        return sum(
                1
                for building in self._grid.get_buildings().values()
                if isinstance(building, Home) and building.is_under_construction()
            )

    def _get_barn_count(self) -> int:
        return sum(
            1 for building in self._grid.get_buildings().values()
            if isinstance(building, Barn)
        )

    def _get_construction_barn_count(self) -> int:
        return sum(
            1
            for building in self._grid.get_buildings().values()
            if isinstance(building, Barn) and building.is_under_construction()
        )

    def _get_farm_count(self) -> int:
        return sum(
            1 for building in self._grid.get_buildings().values() if isinstance(building, Farm)
        )

    def _get_construction_farm_count(self) -> int:
        return sum(
            1
            for building in self._grid.get_buildings().values()
            if isinstance(building, Farm) and building.is_under_construction()
        )

    def _get_mine_count(self) -> int:
        return sum(
            1 for building in self._grid.get_buildings().values() if isinstance(building, Mine)
        )

    def _get_construction_mine_count(self) -> int:
        return sum(
            1
            for building in self._grid.get_buildings().values()
            if isinstance(building, Mine) and building.is_under_construction()
        )

    def _get_tree_count(self) -> int:
        count: int = 0
        for i in range(len(self._grid.get_grid())):
            for j in range(len(self._grid.get_grid()[i])):
                location: Location = Location(i, j)
                if self._grid.is_tree(location):
                    count += 1
        return count

