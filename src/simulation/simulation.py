from copy import deepcopy

from grid.grid import Grid
from people.people import People
from visualization.state_tracker import StateTracker


class Simulation:
    def __init__(
        self, actions_per_day: int, days_per_year: int, years: int, grid_size: int
    ) -> None:
        self._days_per_year: int = days_per_year
        self._years: int = years
        self._grid: Grid = Grid(grid_size)
        self._people: People = People(self, actions_per_day)
        self._max_days: int = self._years * self._days_per_year
        self._current_day: int = 0

    def run(self) -> StateTracker:        
        tracker: StateTracker = StateTracker()
        for day in range(self._max_days):
            self._current_day += 1
            self._people.take_actions_for_day()
            # TODO check if people are stuck
            
            if self._has_been_a_year(day):
                self._people.age()
                self._grid.grow_trees()
                self._create_disasters()
                tracker.add(self._get_year(day), deepcopy(self._grid), deepcopy(self._people))

        return tracker

    def _create_disasters(self):
        self._people.generate_disasters()
        self._grid.generate_disasters()
    
    def _has_been_a_year(self, day):
        return day % self._days_per_year == 0
    
    def _get_year(self, day: int) -> int:
        return day // self._days_per_year
    
    def get_current_time(self) -> int:
        return self._people.get_time()

    def get_grid(self) -> Grid:
        return self._grid

    def get_people(self) -> People:
        return self._people

