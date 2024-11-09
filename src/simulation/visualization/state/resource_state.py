from src.simulation.grid.grid import Grid


class ResourceState:
    def __init__(self, grid: Grid):
        self._grid = grid
        self._total_food: int = self._get_total_food()
        self._total_stone: int = self._get_total_stone()
        self._total_wood: int = self._get_total_wood()
        self._total_capacity: int = self._get_total_barn_capacity()
        self._total_remaining_capacity: int = self._get_total_remaining_capacity()
        del self._grid

    def _get_total_food(self) -> int:
        total_food = 0
        for barn in self._grid.get_barns():
            total_food += barn.get_food_stored()
        return total_food

    def _get_total_stone(self) -> int:
        total_stone = 0
        for barn in self._grid.get_barns():
            total_stone += barn.get_stone_stored()
        return total_stone

    def _get_total_wood(self) -> int:
        total_wood = 0
        for barn in self._grid.get_barns():
            total_wood += barn.get_wood_stored()
        return total_wood

    def _get_total_barn_capacity(self) -> int:
        total_capacity = 0
        for barn in self._grid.get_barns():
            total_capacity += barn.get_capacity()
        return total_capacity

    def _get_total_remaining_capacity(self) -> int:
        total_remaining_capacity = 0
        # Get the list of barns from the grid
        barns = self._grid.get_barns()

        # Calculate the remaining capacity for each barn
        for barn in barns:
            remaining_capacity = barn.get_remaining_capacity()
            total_remaining_capacity += remaining_capacity

        return total_remaining_capacity
