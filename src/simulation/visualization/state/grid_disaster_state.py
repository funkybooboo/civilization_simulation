from typing import Dict

from src.simulation.grid.grid import Grid
from src.simulation.visualization.state.state import State


class GridDisasterState(State):
    def __init__(self, grid: Grid):
        # Get disaster counts from the GridDisasterGenerator
        disaster_counts: Dict[str, int] = grid.get_disaster_counts()

        # Initialize disaster attributes based on counts
        self._rats_eat_home_food = disaster_counts.get("rats_eat_home_food", 0)
        self._burn_buildings = disaster_counts.get("burn_buildings", 0)
        self._decrease_farm_yield = disaster_counts.get("decrease_farm_yield", 0)
        self._decrease_mine_yield = disaster_counts.get("decrease_mine_yield", 0)
        self._forest_fire = disaster_counts.get("forest_fire", 0)
        self._steal_barn_resources = disaster_counts.get("steal_barn_resources", 0)
