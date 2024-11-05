from typing import Set, List, Tuple


class Memory:
    def __init__(self) -> None:
        self.barns: Set[Tuple[int, int]] = set()
        self.construction_barns: Set[Tuple[int, int]] = set()
        self.farms: Set[Tuple[int, int]] = set()
        self.construction_farms: Set[Tuple[int, int]] = set()
        self.mines: Set[Tuple[int, int]] = set()
        self.construction_mines: Set[Tuple[int, int]] = set()
        self.homes: Set[Tuple[int, int]] = set()
        self.construction_homes: Set[Tuple[int, int]] = set()
        self.trees: Set[Tuple[int, int]] = set()
        self.empties: Set[Tuple[int, int]] = set()
        self.people: Set[Tuple[int, int]] = set()
        self.items: List[str] = list(vars(self).keys())

    def dont_know_where_anything_is(self) -> bool:
        return not (self.barns or self.farms or self.homes or self.mines)

    def combine(self, other: 'Memory') -> None:
        for item in self.items:
            for location in getattr(other, item):
                self.add(item, location)

    def add(self, what: str, where: Tuple[int, int]) -> None:
        if what is None or where is None:
            return
        if what not in self.items:
            return
        for item in self.items:
            if item != what:
                self.__remove(item, where)
        getattr(self, what).add(where)

    def __remove(self, what: str, where: Tuple[int, int]) -> None:
        if what is None or where is None:
            return
        if what not in self.items:
            return
        if where in getattr(self, what):
            getattr(self, what).remove(where)
