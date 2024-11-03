import random

class GridGenerator:
    def __init__(self,
             size,
             tree_density=0.4,
             ca_iterations=40,
         ):
        self.grid = []
        self.width = size
        self.height = size
        self.tree_density = tree_density
        self.ca_iterations = ca_iterations
        self.end_of_world_char = 'e'
        self.tree_char = '*'

    def generate(self):
        self.grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        self._add_clustered_trees()
        self._place_town_in_center(self.height, self.width)
        return self.grid

    def _place_town_in_center(self, height, width):
        # Read town layout from town.txt
        town_layout = self._read_town_layout('../data/town.txt')
        # Calculate town position
        town_width = len(town_layout[0])
        town_height = len(town_layout)
        town_x = (width - town_width) // 2
        town_y = (height - town_height) // 2
        # Place the town in the map
        for y in range(town_height):
            for x in range(town_width):
                self.grid[town_y + y][town_x + x] = town_layout[y][x]

    @staticmethod
    def _read_town_layout(filename):
        with open(filename, 'r') as file:
            return [line.rstrip('\n') for line in file.readlines()]

    def _add_clustered_trees(self):
        self._create_trees()
        self._generate_inner_trees()
        self.grid = self._do_cellular_automata()
        return self.grid

    def _create_trees(self):
        self.grid[0] = [self.end_of_world_char] * len(self.grid[0])
        self.grid[-1] = [self.end_of_world_char] * len(self.grid[-1])
        for i in range(len(self.grid)):
            self.grid[i][0] = self.end_of_world_char
            self.grid[i][-1] = self.end_of_world_char

    def _generate_inner_trees(self):
        for i in range(2, len(self.grid) - 2):
            for j in range(2, len(self.grid[i]) - 2):
                if random.random() < self.tree_density:
                    self.grid[i][j] = self.tree_char

    def _do_cellular_automata(self):
        for _ in range(self.ca_iterations):
            grid_copy = [row[:] for row in self.grid]
            for i in range(2, len(self.grid) - 2):
                for j in range(2, len(self.grid[i]) - 2):
                    count = self._count_number_of_neighbors(i, j)
                    if self.grid[i][j] == self.tree_char and count < 3:
                        grid_copy[i][j] = ' '
                    elif self.grid[i][j] == ' ' and count > 4:
                        grid_copy[i][j] = self.tree_char
            self.grid = grid_copy
        return self.grid

    def _count_number_of_neighbors(self, row, col):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0) or not (0 <= row + i < len(self.grid)) or not (0 <= col + j < len(self.grid[row])):
                    continue
                if self.grid[row + i][col + j] == self.tree_char:
                    count += 1
        return count

    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))

if __name__ == '__main__':
    grid_size = 75
    tree_density = 0.4  # Control tree density here
    ca_iterations = 40   # Control cellular automata iterations here
    grid_generator = GridGenerator(grid_size, tree_density, ca_iterations)
    generated_grid = grid_generator.generate()
    grid_generator.display_grid()
