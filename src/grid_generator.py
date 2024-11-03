import random

class GridGenerator:
    def __init__(self,
             size,
             tree_density=0.1,
             ca_iterations=40,
        ):
        self._grid = []
        self._width = size
        self._height = size
        self._tree_density = tree_density
        self._ca_iterations = ca_iterations
        self._end_of_world_char = 'e'
        self._tree_char = '*'
        self.num_houses = 10
        self.num_farms = 3
        self.num_mines = 1
        self.num_barns = 1

    def generate(self):
        self._grid = [[' ' for _ in range(self._width)] for _ in range(self._height)]
        self._add_clustered_trees()
        self._place_town_in_center()
        return self._grid

    def _place_town_in_center(self):
        # Read town layout from town.txt
        town_layout = self._read_town_layout('../data/town.txt')
        # Calculate town position
        town_width = len(town_layout[0])
        town_height = len(town_layout)
        town_x = (self._width - town_width) // 2
        town_y = (self._height - town_height) // 2
        # Place the town in the map
        for y in range(town_height):
            for x in range(town_width):
                self._grid[town_y + y][town_x + x] = town_layout[y][x]

    @staticmethod
    def _read_town_layout(filename):
        with open(filename, 'r') as file:
            return [line.rstrip('\n') for line in file.readlines()]

    def _add_clustered_trees(self):
        self._create_trees()
        self._generate_inner_trees()
        self._do_cellular_automata()

    def _create_trees(self):
        self._grid[0] = [self._end_of_world_char] * len(self._grid[0])
        self._grid[-1] = [self._end_of_world_char] * len(self._grid[-1])
        for i in range(len(self._grid)):
            self._grid[i][0] = self._end_of_world_char
            self._grid[i][-1] = self._end_of_world_char

    def _generate_inner_trees(self):
        for i in range(2, len(self._grid) - 2):
            for j in range(2, len(self._grid[i]) - 2):
                if random.random() < self._tree_density:
                    self._grid[i][j] = self._tree_char

    def _do_cellular_automata(self):
        for _ in range(self._ca_iterations):
            grid_copy = [row[:] for row in self._grid]
            for i in range(2, len(self._grid) - 2):
                for j in range(2, len(self._grid[i]) - 2):
                    count = self._count_number_of_neighbors(i, j)
                    if self._grid[i][j] == self._tree_char and count < 3:
                        grid_copy[i][j] = ' '
                    elif self._grid[i][j] == ' ' and count > 4:
                        grid_copy[i][j] = self._tree_char
            self._grid = grid_copy

    def _count_number_of_neighbors(self, row, col):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0) or not (0 <= row + i < len(self._grid)) or not (0 <= col + j < len(self._grid[row])):
                    continue
                if self._grid[row + i][col + j] == self._tree_char:
                    count += 1
        return count

    def display_grid(self):
        for row in self._grid:
            print(' '.join(row))

if __name__ == '__main__':
    grid_size = 75
    tree_density = 0.4  # Control tree density here
    ca_iterations = 40   # Control cellular automata iterations here
    grid_generator = GridGenerator(grid_size, tree_density, ca_iterations)
    generated_grid = grid_generator.generate()
    grid_generator.display_grid()
