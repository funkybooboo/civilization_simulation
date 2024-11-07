from grid_plotter import GridPlotter
from src.simulation.grid.grid import Grid
from src.simulation.people.people import People
from src.simulation.result.simulation_state_plotter import SimulationStatePlotter


class SimulationStateTracker:
    def __init__(self) -> None:
        self._grid_plotter = GridPlotter()
        self._simulation_state_plotter = SimulationStatePlotter()

    def display_town_slide_show(self) -> None:
        self._grid_plotter.show_slide_show()
        
    def display_simulation_stats(self):
        self._simulation_state_plotter.plot_simulation_states()
    
    def add(self, year: int, grid: Grid, people: People):
        self._grid_plotter.add(grid.get_grid_deepcopy())
        self._simulation_state_plotter.add(year, grid, people)
