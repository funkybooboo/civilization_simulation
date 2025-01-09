from __future__ import annotations

from typing import TYPE_CHECKING

from src.settings import settings
from src.simulation.grid.structure.structure_type import StructureType
from src.simulation.people.person.scheduler.task.start_construction.start_construction import StartConstruction
from src.simulation.people.person.scheduler.task.task_type import TaskType

if TYPE_CHECKING:
    from src.simulation.people.person.person import Person
    from src.simulation.simulation import Simulation


class StartFarmConstruction(StartConstruction):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(
            simulation,
            person,
            settings.get("farm_size", 5),
            settings.get("farm_size", 5),
            StructureType.CONSTRUCTION_FARM,
            TaskType.START_FARM_CONSTRUCTION,
        )
