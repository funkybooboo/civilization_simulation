from __future__ import annotations

from typing import TYPE_CHECKING, Callable

import numpy as np

from src.logger import logger
from src.settings import settings
from src.simulation.grid.structure.work.work import Work

if TYPE_CHECKING:
    from src.simulation.grid.grid import Grid
    from src.simulation.grid.location import Location


class Tree(Work):
    def __init__(self, grid: Grid, location: Location) -> None:
        logger.debug(f"Initializing Tree at location {location}")

        max_worker_count: int = settings.get("tree_max_worker_count", 1)
        max_work_count: int = settings.get("tree_max_work_count", 2)
        yield_func: Callable[[], float] = lambda: np.random.normal(
            loc=settings.get("tree_yield_func_loc", 3), scale=settings.get("tree_yield_func_scale", 1)
        )
        yield_variance = np.random.normal(
            loc=settings.get("tree_yield_var_loc", 3), scale=settings.get("tree_yield_var_scale", 0.9)
        )
        super().__init__(
            grid,
            location,
            settings.get("tree_size", 1),
            settings.get("tree_size", 1),
            settings.get("tree_char", "*"),
            max_worker_count,
            max_work_count,
            yield_func,
            yield_variance,
        )

        logger.debug(
            f"Tree initialized with max workers: {max_worker_count}, "
            f"max work count: {max_work_count}, "
            f"yield variance: {yield_variance:.2f}, "
            f"size: {settings.get('tree_size', 1)}"
        )
