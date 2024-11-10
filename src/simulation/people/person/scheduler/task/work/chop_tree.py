from src.simulation.grid.structure.structure_type import StructureType
from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.work.work import Work
from src.simulation.simulation import Simulation


class ChopTree(Work):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5, StructureType.TREE, StructureType.BARN, "wood")
