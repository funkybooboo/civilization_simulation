from typing import List

from src.settings import settings
from src.simulation.grid.grid import Grid
from src.simulation.grid.structure.store.barn import Barn
from src.logger import logger
from src.simulation.people.people import People
from src.simulation.visualization.state.state import State
from src.simulation.people.person.backpack import Backpack
from src.simulation.grid.structure.store.home import Home

class ResourceState(State):
    def __init__(self, grid: Grid, people: People):
        logger.debug("Initializing YourClassName with grid.")
        self._barns: List[Barn] = []
        self._backpacks: List[Backpack] = []
        self._homes: List[Home] = []

        for barn in grid.get_structures(Barn):
            if isinstance(barn, Barn):
                self._barns.append(barn)
                logger.debug(f"Added barn: {barn}")

        self._total_barn_food: int = self._get_total_barn_food()
        logger.debug(f"Total food: {self._total_barn_food}")

        self._total_barn_stone: int = self._get_total_barn_stone()
        logger.debug(f"Total stone: {self._total_barn_stone}")

        self._total_barn_wood: int = self._get_total_barn_wood()
        logger.debug(f"Total wood: {self._total_barn_wood}")

        self._total_barn_capacity: int = self._get_total_barn_capacity()
        logger.debug(f"Total barn capacity: {self._total_barn_capacity}")

        self._total_remaining_barn_capacity: int = self._get_total_remaining_barn_capacity()
        logger.debug(f"Total remaining capacity: {self._total_remaining_barn_capacity}")

        # backpack capacities
        for person in people:
            self._backpacks.append(person.get_backpack())

        self._total_backpack_food: int = self._get_total_backpack_food()
        logger.debug(f"Total food: {self._total_backpack_food}")

        self._total_backpack_stone: int = self._get_total_backpack_stone()
        logger.debug(f"Total stone: {self._total_backpack_stone}")

        self._total_backpack_wood: int = self._get_total_backpack_wood()
        logger.debug(f"Total wood: {self._total_backpack_wood}")

        self._total_backpack_capacity: int = self._get_total_backpack_capacity()
        logger.debug(f"Total backpack capacity: {self._total_backpack_capacity}")

        self._total_remaining_backpack_capacity: int = self._get_total_remaining_backpack_capacity()
        logger.debug(f"Total remaining capacity: {self._total_remaining_backpack_capacity}")

        del self._backpacks

        # home stuffs
        for home in grid.get_structures(Home):
            if isinstance(home, Home):
                self._homes.append(home)
                logger.debug(f"Added home: {home}")

        self._total_home_food: int = self._get_total_home_food()
        logger.debug(f"Total food: {self._total_home_food}")

        self._total_home_capacity: int = self._get_total_home_capacity()
        logger.debug(f"Total home capacity: {self._total_home_capacity}")

        self._total_remaining_home_capacity: int = self._get_total_remaining_home_capacity()
        logger.debug(f"Total remaining capacity: {self._total_remaining_home_capacity}")

        del self._homes

    def _get_total_barn_food(self) -> int:
        logger.debug("Calculating total food.")
        total_food = 0
        for barn in self._barns:
            food = barn.get_resource(settings.get("food", "food"))
            total_food += food
            logger.debug(f"Barn {barn} has {food} food.")
        logger.debug(f"Total food: {total_food}")
        return total_food

    def _get_total_barn_stone(self) -> int:
        logger.debug("Calculating total stone.")
        total_stone = 0
        for barn in self._barns:
            stone = barn.get_resource(settings.get("stone", "stone"))
            total_stone += stone
            logger.debug(f"Barn {barn} has {stone} stone.")
        logger.debug(f"Total stone: {total_stone}")
        return total_stone

    def _get_total_barn_wood(self) -> int:
        logger.debug("Calculating total wood.")
        total_wood = 0
        for barn in self._barns:
            wood = barn.get_resource(settings.get("wood", "wood"))
            total_wood += wood
            logger.debug(f"Barn {barn} has {wood} wood.")
        logger.debug(f"Total wood: {total_wood}")
        return total_wood

    def _get_total_barn_capacity(self) -> int:
        logger.debug("Calculating total barn capacity.")
        total_capacity = 0
        for barn in self._barns:
            capacity = barn.get_capacity()
            total_capacity += capacity
            logger.debug(f"Barn {barn} has capacity {capacity}.")
        logger.debug(f"Total barn capacity: {total_capacity}")
        return total_capacity

    def _get_total_remaining_barn_capacity(self) -> int:
        logger.debug("Calculating total remaining barn capacity.")
        total_remaining_capacity = 0
        # Calculate the remaining capacity for each barn
        for barn in self._barns:
            remaining_capacity = barn.get_remaining_capacity()
            total_remaining_capacity += remaining_capacity
            logger.debug(f"Barn {barn} has remaining capacity: {remaining_capacity}.")

        logger.debug(f"Total remaining capacity: {total_remaining_capacity}")
        return total_remaining_capacity

    # backpack
    def _get_total_backpack_food(self) -> int:
        logger.debug("Calculating total food.")
        total_food = 0
        for backpack in self._backpacks:
            food = backpack.get_resource(settings.get("food", "food"))
            total_food += food
            logger.debug(f"Backpack {backpack} has {food} food.")
        logger.debug(f"Total food: {total_food}")
        return total_food

    def _get_total_backpack_stone(self) -> int:
        logger.debug("Calculating total stone.")
        total_stone = 0
        for backpack in self._backpacks:
            stone = backpack.get_resource(settings.get("stone", "stone"))
            total_stone += stone
            logger.debug(f"Backpack {backpack} has {stone} stone.")
        logger.debug(f"Total stone: {total_stone}")
        return total_stone

    def _get_total_backpack_wood(self) -> int:
        logger.debug("Calculating total wood.")
        total_wood = 0
        for backpack in self._backpacks:
            wood = backpack.get_resource(settings.get("wood", "wood"))
            total_wood += wood
            logger.debug(f"Backpack {backpack} has {wood} wood.")
        logger.debug(f"Total wood: {total_wood}")
        return total_wood

    def _get_total_backpack_capacity(self) -> int:
        logger.debug("Calculating total backpack capacity.")
        total_capacity = 0
        for backpack in self._backpacks:
            capacity = backpack.get_capacity()
            total_capacity += capacity
            logger.debug(f"Backpack {backpack} has capacity {capacity}.")
        logger.debug(f"Total backpack capacity: {total_capacity}")
        return total_capacity

    def _get_total_remaining_backpack_capacity(self) -> int:
        logger.debug("Calculating total remaining backpack capacity.")
        total_remaining_capacity = 0
        # Calculate the remaining capacity for each backpack
        for backpack in self._backpacks:
            remaining_capacity = backpack.get_remaining_capacity()
            total_remaining_capacity += remaining_capacity
            logger.debug(f"Backpack {backpack} has remaining capacity: {remaining_capacity}.")

        logger.debug(f"Total remaining capacity: {total_remaining_capacity}")
        return total_remaining_capacity

    # home
    def _get_total_home_food(self) -> int:
        logger.debug("Calculating total food.")
        total_food = 0
        for home in self._homes:
            food = home.get_resource(settings.get("food", "food"))
            total_food += food
            logger.debug(f"Home {home} has {food} food.")
        logger.debug(f"Total food: {total_food}")
        return total_food



    def _get_total_home_capacity(self) -> int:
        logger.debug("Calculating total home capacity.")
        total_capacity = 0
        for home in self._homes:
            capacity = home.get_capacity()
            total_capacity += capacity
            logger.debug(f"Home {home} has capacity {capacity}.")
        logger.debug(f"Total home capacity: {total_capacity}")
        return total_capacity

    def _get_total_remaining_home_capacity(self) -> int:
        logger.debug("Calculating total remaining home capacity.")
        total_remaining_capacity = 0
        # Calculate the remaining capacity for each home
        for home in self._homes:
            remaining_capacity = home.get_remaining_capacity()
            total_remaining_capacity += remaining_capacity
            logger.debug(f"Home {home} has remaining capacity: {remaining_capacity}.")

        logger.debug(f"Total remaining capacity: {total_remaining_capacity}")
        return total_remaining_capacity

