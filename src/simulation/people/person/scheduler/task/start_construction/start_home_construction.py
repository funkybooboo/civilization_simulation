from src.simulation.grid.structure.structure_type import StructureType
from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.start_construction.start_construction import StartConstruction
from src.simulation.simulation import Simulation


class StartHomeConstruction(StartConstruction):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5, 2, 2, StructureType.CONSTRUCTION_HOME)