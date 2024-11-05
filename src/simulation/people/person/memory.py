class Memory:
    def __init__(self):
        self.barns = set()
        self.construction_barns = set()
        self.farms = set()
        self.construction_farms = set()
        self.mines = set()
        self.construction_mines = set()
        self.homes = set()
        self.construction_homes = set()
        self.trees = set()
        self.empties = set()
        self.people = set()
        self.items = list(vars(self).keys())

    def dont_know_where_anything_is(self):
        if self.barns or self.farms or self.homes or self.mines:
            return False
        return True

    def combine(self, other):
        for item in self.items:
            for location in getattr(other, item):
                self.add(item, location)

    def add(self, what, where):
        if what is None or where is None:
            return
        if what not in self.items:
            return
        for item in self.items:
            if item != what:
                self.__remove(item, where)
        getattr(self, what).add(where)

    def __remove(self, what, where):
        if what is None or where is None:
            return
        if what not in self.items:
            return
        if where in getattr(self, what):
            getattr(self, what).remove(where)
