from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location
from src.simulation.grid.structure.work.construction.construction import Construction


class ConstructionBarn(Construction):
    def __init__(self, grid: Grid, location: Location):
        super().__init__(
            grid,
            location,
            3,
            3,
            "b",
            required_wood=60,
            required_stone=30,
            max_work_count=3,
            max_worker_count=3,
            finished_completion_level=5,
        )
