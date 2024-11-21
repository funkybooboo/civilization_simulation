from __future__ import annotations

from typing import TYPE_CHECKING

from src.settings import settings
from src.simulation.grid.structure.structure_type import StructureType
from src.simulation.people.person.scheduler.task.task_type import TaskType
from src.simulation.people.person.scheduler.task.work.work import Work

if TYPE_CHECKING:
    from src.simulation.people.person.person import Person
    from src.simulation.simulation import Simulation


class ChopTree(Work):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(
            simulation,
            person,
            StructureType.TREE,
            settings.get("wood", "wood"),
            TaskType.CHOP_TREE,
        )
