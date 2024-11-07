from copy import deepcopy

from grid.grid import Grid
from people.people import People
from result.simulation_state_tracker import SimulationStateTracker


class Simulation:
    def __init__(
        self, actions_per_day: int, days_per_year: int, years: int, grid_size: int
    ) -> None:
        self._days_per_year: int = days_per_year
        self._years: int = years
        self._grid: Grid = Grid(grid_size)
        self._people: People = People(self, actions_per_day)
        self._max_days: int = self._years * self._days_per_year

    def run(self) -> SimulationStateTracker:        
        tracker: SimulationStateTracker = SimulationStateTracker()
        for day in range(self._max_days):
            self._people.take_actions_for_day()
            
            if self._has_been_a_year(day):
                self._people.age()
                self._grid.grow_trees()
                # todo: add a disaster percentage chance (crops diseased, house burned, cemetary makes zombies, mines collapse, divorce, be preggers 'pregaganant')

                tracker.add(self._get_year(day), deepcopy(self._grid), deepcopy(self._people))
            
        return tracker
    
    def _has_been_a_year(self, day):
        return day % self._days_per_year == 0
    
    def _get_year(self, day: int) -> int:
        return day // self._days_per_year
