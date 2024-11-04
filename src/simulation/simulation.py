from src.simulation.grid.grid import Grid
from src.simulation.people.people import People


class Simulation:
    def __init__(self, actions_per_day, days_per_year, years, grid_size):
        self._actions_per_day = actions_per_day
        self._days_per_year = days_per_year
        self._years = years
        self._grid = Grid(grid_size)
        self._people = People(self)

    def run(self):
        stats = {
            # TODO figure out what we care about
        }
        days = self._years * self._days_per_year
        for day in range(days):
            # TODO flesh out this logic
            self._people.take_actions()
            self._grid.grow_trees()

        return stats
