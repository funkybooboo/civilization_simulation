from src.simulation.grid.grid_generator import GridGenerator


class Grid:
    def __init__(self, size):
        grid_generator = GridGenerator(size)
        self._grid = grid_generator.generate()
        self.buildings = self._find_buildings()

    def _find_buildings(self):
        # TODO scan the grid and find the starting buildings, make sure a group of b's are all mapped to the same barn instance
        return {}

    def __str__(self):
        s = ''
        for row in self._grid:
            s += ' '.join(row) + '\n'
        return s

    def grow_trees(self):
        # TODO scan the grid and for every tree found there is a chance that a tree will grow next to it
        pass

    def chop_down_tree(self, x, y):
        if not self.is_tree(x, y):
            raise Exception("tried to chop down not a tree")
        self._grid[y][x] = ' '
        return 100

    def is_tree(self, x, y):
        self._is_item(x, y, '*')

    def _is_item(self, x, y, char):
        return self._grid[y][x] == char

if __name__ == '__main__':
    grid = Grid(75)
    print(grid)