from typing import Dict, Type

from src.simulation.grid.building.barn import Barn
from src.simulation.grid.building.building import Building
from src.simulation.grid.building.building_type import BuildingType
from src.simulation.grid.building.farm import Farm
from src.simulation.grid.building.home import Home
from src.simulation.grid.building.mine import Mine
from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location


class BuildingFactory:
    _constructors: Dict[BuildingType, Type] = {
        BuildingType.HOME: Home,
        BuildingType.BARN: Barn,
        BuildingType.MINE: Mine,
        BuildingType.FARM: Farm,
    }

    def __init__(self, grid: Grid) -> None:
        self._grid = grid

    def create_instance(self, building_type, location: Location) -> Building:
        building_class: Type = self._constructors[building_type]
        return building_class(self._grid, location)
