from grid_plotter import GridPlotter
from src.simulation.grid.grid import Grid
from src.simulation.people.people import People
from src.simulation.visualization.state_plotter import StatePlotter


class StateTracker:
    def __init__(self) -> None:
        self._grid_plotter = GridPlotter()
        self._state_plotter = StatePlotter()

    def display_town_slide_show(self) -> None:
        self._grid_plotter.show_slide_show()
        
    def display_simulation_stats(self):
        self._state_plotter.plot_simulation_states()
    
    def add(self, year: int, grid: Grid, people: People):
        self._grid_plotter.add(grid.get_grid())
        self._state_plotter.add(year, grid, people)
