from building import Building
from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location


class Home(Building):
    def __init__(self, grid: Grid, location: Location) -> None:
        super().__init__(grid, location, 2, 2, "h", "H")
