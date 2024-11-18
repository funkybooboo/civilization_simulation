from typing_extensions import Optional

from src.simulation.grid.structure.structure import Structure


class MoveResult:
    def __init__(self, failed: bool, structure: Optional[Structure]):
        self._failed: bool = failed
        self._structure: Optional[Structure] = structure

    def has_failed(self) -> bool:
        return self._failed

    def get_structure(self) -> Optional[Structure]:
        return self._structure
