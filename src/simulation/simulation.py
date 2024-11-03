from src.simulation.grid.grid import Grid
from src.simulation.people.people import People


class Simulation:
    def __init__(self, max_time):
        self._max_time = max_time
        self._grid = Grid(100)
        self._people = People(self)

    def run(self):
        stats = {
            # TODO figure out what we care about
        }

        for time in range(self._max_time):
            self._people.take_action()
            self._grid.grow_trees()

        return stats
