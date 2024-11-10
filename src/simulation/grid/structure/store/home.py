from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location
from src.simulation.grid.structure.store.store import Store


class Home(Store):
    def __init__(self, grid: Grid, location: Location) -> None:
        # Home only stores food, with a maximum of 36
        allowed_resources = {"food": 36}  # Only food can be stored
        super().__init__(grid, location, 2, 2, "H", allowed_resources)

        self._occupied: bool = False

    def has_owner(self) -> bool:
        return self._occupied

    def assign_owner(self) -> None:
        self._occupied = True

    def remove_owner(self) -> None:
        self._occupied = False
