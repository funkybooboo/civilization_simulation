from src.simulation.grid.grid import Grid
from src.simulation.people.people import People


class SimulationState:
    def __init__(self, grid: Grid, people: People):
        # people stats
        self._people_count: int = len(people)
        self._average_health: float = people.get_average_health()
        self._average_hunger: float = people.get_average_hunger()
        # TODO active tasks count for each type
        # TODO completed tasks count for each type
        
        # grid stats
        # TODO number of each type of buildings
        # TODO number of trees
        # TODO resource count
        # TODO barn capacity
