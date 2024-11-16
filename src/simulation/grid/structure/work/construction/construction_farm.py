from __future__ import annotations

from typing import TYPE_CHECKING

from src.simulation.grid.structure.work.construction.construction import Construction

if TYPE_CHECKING:
    from src.simulation.grid.grid import Grid
    from src.simulation.grid.location import Location

class ConstructionFarm(Construction):
    def __init__(self, grid: Grid, location: Location):
        super().__init__(
            grid,
            location,
            5,
            5,
            "f",
            required_wood=30,
            required_stone=0,
            max_work_count=2,
            max_worker_count=3,
            finished_completion_level=3,
        )
