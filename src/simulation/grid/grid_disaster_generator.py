import random

from src.simulation.grid.grid import Grid


class GridDisasterGenerator:
    def __init__(self, grid: Grid):
        self._grid = grid

    def generate(self, chance: float) -> None:
        """Randomly trigger one of the disaster types with a given chance."""
        if random.random() < chance:
            severity = random.randint(1, 10)

            # List of disaster methods
            disaster_methods = [
                self._remove_home_food,
                self._burn_buildings,
                self._disease_farm,
                self._forest_fire,
                self._steal_barn_resources,
            ]

            # Randomly pick one disaster to trigger
            chosen_disaster = random.choice(disaster_methods)
            chosen_disaster(severity)

    def _remove_home_food(self, severity: int) -> None:
        """Remove food from home storage based on disaster severity."""
        # Example logic: lose food based on severity
        food_lost = severity * 10  # for example, 10 units of food per severity point
        # Logic to decrease food in the home (e.g., update the home storage state)
        # self.home.food -= food_lost  # This depends on how your game is structured

    def _burn_buildings(self, severity: int) -> None:
        """Burn down buildings based on severity."""
        # Example logic: burn buildings based on severity
        buildings_burned = (
            severity // 2
        )  # Each point of severity could burn down 0.5 buildings
        # Logic to decrement building count (or other effects)
        # self.buildings -= buildings_burned

    def _disease_farm(self, severity: int) -> None:
        """Disease infects the farm, reducing resources or crops."""
        # Example logic: disease damages crops or farm productivity
        crop_damage = severity * 2  # Each severity point reduces farm crop yield
        # Logic to update farm resources
        # self.farm.crops -= crop_damage

    def _forest_fire(self, severity: int) -> None:
        """Forest fire destroys trees or forest resources."""
        # Example logic: fire burns down trees or reduces forest resources
        trees_burned = severity * 100  # Severity affects the number of trees lost
        # Logic to reduce forest resources
        # self.forest.trees -= trees_burned

    def _steal_barn_resources(self, severity: int) -> None:
        """Theft reduces resources in the barn based on severity."""
        # Example logic: the higher the severity, the more resources are stolen
        resources_stolen = severity * 100  # Resources stolen proportional to severity
        # Logic to reduce barn resources
        # self.barn.resources -= resources_stolen
