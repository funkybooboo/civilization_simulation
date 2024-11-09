from src.simulation.grid.grid import Grid
from src.simulation.visualization.state.state import State


class GridDisasterState(State):
    def __init__(self, grid: Grid):
        self._grid = grid

        # TODO    

        del self._grid
