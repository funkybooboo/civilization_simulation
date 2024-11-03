from random import randint
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder
from copy import deepcopy


class Mover:
    def __init__(self, person):
        self.person = person

    def move(self):
        self.person.memory.combine(self.person.vision.look_around())
        choice = self.person.thinker.think()
        l1 = self.person.location
        if self.person.fear == self.person.simulation.max_fear:
            self.person.number_of_max_fear += 1
        other = None
        for _ in range(self.person.speed):

            if self.person.is_dead():
                return other

            other = self.person.thinker.make(choice)

            self.person.memory.combine(self.person.vision.look_around())

            # hit person
            if other:
                return other
            # in a fire
            if self.person.location in self.person.simulation.fire_locations:
                self.person.health -= 25
                self.person.end_turn_in_fire = True
                self.person.number_of_fire_touches += 1
            else:
                self.person.end_turn_in_fire = False
            # at a stair
            if self.person.simulation.is_stair(self.person.location):
                if self.person.location[0] > 0:
                    self.person.simulation.number_of_stairs += 1
                    self.person.location = (self.person.location[0] - 1, self.person.location[1], self.person.location[2])
                    return other
            # at an exit
            if self.person.simulation.is_exit(self.person.location):
                return other
            # at broken glass
            if self.person.simulation.is_broken_glass(self.person.location):
                return other

        l2 = self.person.location
        if l1 == l2:
            self.person.times_not_move += 1
        else:
            self.person.times_not_move = 0
        if self.person.times_not_move == 10:
            raise Exception("Person is stuck")
        return other

    def explore(self):
        if self.person.is_in_room():
            closest_door = self.get_closest(self.person.location, self.person.memory.doors)
            if closest_door:
                return self.towards(closest_door)
        while True:
            random_location = self.get_random_location()
            for fire_location in self.person.simulation.fire_locations:
                if self.person.is_near(fire_location, random_location):
                    continue
                return self.towards(random_location)

    def get_random_location(self):
        floor = self.person.location[0]
        while True:
            x = randint(0, self.person.simulation.grid.x_size - 1)
            y = randint(0, self.person.simulation.grid.y_size - 1)
            location = (floor, x, y)
            if self.person.simulation.is_valid_location_for_person(location):
                break
        return location

    def towards(self, location):
        if location is None:
            return None
        self.person.simulation.is_not_in_building(location)
        n_x = -1
        n_y = -1
        for i in range(4):
            grid = self.get_grid(i)
            path = self.get_path(location, grid)
            if path and len(path) >= 2:
                node = path[1]
                n_x = node.y
                n_y = node.x
                break
        if n_x == -1 or n_y == -1:
            return None
        new_location = (n_x, n_y)
        return self.place(new_location)

    def place(self, location):
        if not self.is_one_away(self.person.location, location):
            raise Exception(f"location is not one away: {location}")
        if not self.person.simulation.is_valid_location_for_person(location):
            raise Exception(
                f"location is not valid: {location} {self.person.simulation.building.text[location[0]][location[1]][location[2]]}")
        self.person.location = location

    def get_path(self, location, grid):
        if location is None:
            raise Exception("location is None")
        if grid is None:
            raise Exception("grid is None")
        self.person.simulation.is_not_in_building(self.person.location)
        self.person.simulation.is_not_in_building(location)
        x1 = self.person.location[1]
        y1 = self.person.location[2]
        start = grid.node(y1, x1)
        x2 = location[1]
        y2 = location[2]
        end = grid.node(y2, x2)
        finder = DijkstraFinder(diagonal_movement=DiagonalMovement.always)
        path, runs = finder.find_path(start, end, grid)
        return path

    def get_grid(self, i):
        matrix = deepcopy(self.person.simulation.building.matrix)
        if i == 0:
            self._switcher(matrix, -1, -2)
        elif i == 1:
            self._switcher(matrix, 3, -2)
        elif i == 2:
            self._switcher(matrix, -1, 5)
        elif i == 3:
            self._switcher(matrix, 3, 5)
        else:
            raise Exception("invalid i")
        grid = Grid(matrix=matrix)
        return grid

    @staticmethod
    def _switcher(matrix, p, f):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == -1:
                    matrix[row][col] = p
                elif matrix[row][col] == -2:
                    matrix[row][col] = f

    def get_closest(self, location1, locations):
        """
        get the closet of something from a list. ex: get the closest wall, get the closest person, etc.
        """
        if len(locations) == 0:
            return None
        check = deepcopy(locations)
        closest = None
        while not closest:
            if len(check) == 0:
                return None
            location2 = next(iter(check))
            if location2[0] == location1[0]:
                closest = location2
            else:
                check.remove(location2)
        if not closest:
            return None
        for location2 in locations:
            d1 = self.get_distance(location1, location2)
            d2 = self.get_distance(location1, closest)
            if d1 is None or d2 is None:
                continue
            if d1 < d2:
                closest = location2
        return closest

    def get_furthest(self, location1, lst):
        """
        get the furthest of something from a list. ex: get the furthest wall, get the furthest person, etc.
        """
        if len(lst) == 0:
            return None
        furthest = next(iter(lst))
        for location2 in lst:
            d1 = self.get_distance(location1, location2)
            d2 = self.get_distance(location1, furthest)
            if d1 is None or d2 is None:
                continue
            if d1 > d2:
                furthest = location2
        return furthest

    @staticmethod
    def get_distance(location1, location2):
        if not location1 or not location2:
            return None
        x1 = location1[1]
        y1 = location1[2]
        x2 = location2[1]
        y2 = location2[2]
        return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

    @staticmethod
    def is_one_away(location1, location2):
        if not location1 or not location2:
            return False
        if not isinstance(location1, tuple) or not isinstance(location2, tuple):
            return False
        a = abs(location1[1] - location2[1])
        b = abs(location1[2] - location2[2])
        if a > 1 or b > 1:
            return False
        return True

    def is_next_to(self, locations):
        for location in locations:
            if self.is_one_away(self.person.location, location):
                return True
        return False

    def is_near(self, location1, location2, distance=5):
        if not location1 or not location2:
            return False
        d1 = self.get_distance(location1, location2)
        if d1:
            if d1 < distance:
                return True
        return False

    def can_get_to_location(self, location):
        grid = self.get_grid(0)
        path = self.get_path(location, grid)
        if path:
            return True
        return False

