from typing import Set, List, Optional

class Memory:
    def __init__(self) -> None:
        self.barns: Set = set()
        self.construction_barns: Set = set()
        self.farms: Set = set()
        self.construction_farms: Set = set()
        self.mines: Set = set()
        self.construction_mines: Set = set()
        self.homes: Set = set()
        self.construction_homes: Set = set()
        self.trees: Set = set()
        self.empties: Set = set()
        self.people: Set = set()
        self.items: List[str] = list(vars(self).keys())

    def dont_know_where_anything_is(self) -> bool:
        if self.barns or self.farms or self.homes or self.mines:
            return False
        return True

    def combine(self, other: 'Memory') -> None:
        for item in self.items:
            for location in getattr(other, item):
                self.add(item, location)

    def add(self, what: str, where: Optional[str]) -> None:
        if what is None or where is None:
            return
        if what not in self.items:
            return
        for item in self.items:
            if item != what:
                self.__remove(item, where)
        getattr(self, what).add(where)

    def __remove(self, what: str, where: Optional[str]) -> None:
        if what is None or where is None:
            return
        if what not in self.items:
            return
        if where in getattr(self, what):
            getattr(self, what).remove(where)
