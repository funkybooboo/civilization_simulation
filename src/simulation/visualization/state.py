from src.simulation.grid.grid import Grid
from src.simulation.people.people import People


class State:
    def __init__(self, grid: Grid, people: People):
        # people stats
        self._people_count: int = len(people)
        self._average_health: float = people.get_average_health()
        self._average_hunger: float = people.get_average_hunger()
        # TODO active tasks count for each type
        # TODO completed tasks count for each type

        # grid stats
        self._barn_count: int = grid.get_barn_count()
        self._construction_barn_count: int = grid.get_construction_barn_count()
        self._farm_count: int = grid.get_farm_count()
        self._construction_farm_count: int = grid.get_construction_farm_count()
        self._mine_count: int = grid.get_mine_count()
        self._construction_mine_count: int = grid.get_construction_mine_count()
        self._home_count: int = grid.get_home_count()
        self._construction_home_count: int = grid.get_construction_home_count()
        self._tree_count: int = grid.get_tree_count()
        # TODO resource count
        # TODO barn capacity
