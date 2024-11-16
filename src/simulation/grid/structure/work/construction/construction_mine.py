from __future__ import annotations

from typing import TYPE_CHECKING

from src.simulation.grid.structure.work.construction.construction import Construction

if TYPE_CHECKING:
    from src.simulation.grid.grid import Grid
    from src.simulation.grid.location import Location


class ConstructionMine(Construction):
    def __init__(self, grid: Grid, location: Location):
        super().__init__(
            grid,
            location,
            3,
            3,
            "m",
            required_wood=40,
            required_stone=40,
            max_work_count=5,
            max_worker_count=3,
            finished_completion_level=5,
        )
