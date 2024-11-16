from __future__ import annotations

from typing import TYPE_CHECKING

from src.simulation.grid.structure.work.construction.construction import Construction

if TYPE_CHECKING:
    from src.simulation.grid.grid import Grid
    from src.simulation.grid.location import Location


class ConstructionHome(Construction):
    def __init__(self, grid: Grid, location: Location):
        super().__init__(
            grid,
            location,
            2,
            2,
            "h",
            required_wood=20,
            required_stone=10,
            max_work_count=2,
            max_worker_count=2,
            finished_completion_level=3,
        )
