from src.simulation.grid.building.building import Building


class House(Building):
    def __init__(self, grid, x, y):
        super().__init__(grid, x, y, 2, 2, "h", "H")
