from __future__ import annotations

from typing import TYPE_CHECKING

from src.simulation.grid.structure.structure_type import StructureType
from src.simulation.people.person.scheduler.task.construction.build import Build
from src.simulation.people.person.scheduler.task.task_type import TaskType

if TYPE_CHECKING:
    from src.simulation.people.person.person import Person
    from src.simulation.simulation import Simulation


class BuildBarn(Build):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, StructureType.CONSTRUCTION_BARN, StructureType.BARN, TaskType.BUILD_BARN)
