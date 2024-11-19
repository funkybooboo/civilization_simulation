from __future__ import annotations

from copy import deepcopy
from random import randint
from typing import TYPE_CHECKING, List, Optional

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid as PathFindingGrid
from pathfinding.core.node import GridNode as PathFindingGridNode
from pathfinding.finder.a_star import AStarFinder

from src.settings import settings
from src.simulation.grid.location import Location
from src.simulation.people.person.movement.vision import Vision

if TYPE_CHECKING:
    from src.simulation.grid.grid import Grid
    from src.simulation.people.person.memories import Memories
    from src.simulation.people.person.person import Person


class Mover:
    def __init__(self, grid: Grid, person: Person, memories: Memories, speed: int) -> None:
        self._person = person
        self._grid = grid
        self._speed = speed
        self._memories = memories
        self._path_finding_grid = self._get_path_finding_grid()

    def explore(self) -> None:
        random_location = self._get_random_location()
        self.towards(random_location)

    def towards(self, target: Location) -> None:
        if not self._grid.is_in_bounds(target):
            return

        if self._invalid(target):
            target = self._adjust_target(target)

        vision = Vision(self._person, self._grid, settings.get("visibility", 30))

        for _ in range(self._speed):
            self._memories.combine(vision.look_around())
            path = self._get_path(target)
            
            if path and len(path) >= 2:
                next_node = path[1]
                new_location = Location(next_node.y, next_node.x)  # Convert to Location
                self._place(new_location)

    def _invalid(self, location: Location) -> bool:
        return self._grid.is_barn(location) or self._grid.is_mine(location) or self._grid.is_home(location)

    def _adjust_target(self, target):
        neighbors: List[Location] = target.get_neighbors()
        found: bool = False
        for neighbor in neighbors:
            if not self._invalid(neighbor) and self.can_get_to(neighbor):
                target = neighbor
                found = True
                break
        if not found:
            raise Exception("Can only move to empty spaces.")
        return target

    def get_closest(self, locations: List[Location], current_location=None) -> Optional[Location]:
        if not current_location:
            current_location = self._person.get_location()
        if not locations:
            return None
        return min(locations, key=lambda loc: current_location.distance_to(loc), default=None)

    def can_get_to(self, target: Location) -> bool:
        return bool(self._get_path(target))

    def _place(self, location: Location) -> None:
        current_location = deepcopy(self._person.get_location())
        if not current_location.is_one_away(location):
            raise ValueError(f"Location is not one away: {location}")
        if not self._grid.is_in_bounds(location) or self._invalid(location):
            raise ValueError(f"Location is not valid: {location} {self._grid.get_grid()[location.y][location.x]}")
        self._person.set_location(location)

    def _get_random_location(self) -> Location:
        while True:
            x = randint(0, self._grid.get_width() - 1)
            y = randint(0, self._grid.get_height() - 1)
            location = Location(x, y)
            if self._grid.is_in_bounds(location) and not self._invalid(location) and self.can_get_to(location):
                return location

    def _get_path(
        self,
        target: Location,
    ) -> List[PathFindingGridNode]:
        start: Location = deepcopy(self._person.get_location())
        if not self._grid.is_in_bounds(start) or self._invalid(start):
            raise ValueError("Person out of bounds")

        start_node = self._path_finding_grid.node(start.y, start.x)
        end_node = self._path_finding_grid.node(target.y, target.x)

        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        path, _ = finder.find_path(start_node, end_node, self._path_finding_grid)
        return path

    def _get_path_finding_grid(self) -> PathFindingGrid:
        matrix = self._grid.get_path_finding_matrix()
        return PathFindingGrid(matrix=matrix)

    # For debugging
    def _print_grid(self, target: Location, path) -> None:
        grid = self._grid.get_grid()
        person_location = self._person.get_location()
    
        # Extract y (row) and x (column) from the Location object for the person
        person_y = person_location.y  # row
        person_x = person_location.x  # column
    
        # Extract y (row) and x (column) from the Location object for the target
        target_y = target.y  # row
        target_x = target.x  # column
    
        # Convert path from nodes (e.g., tuples) to Location objects
        path_locations = [Location(y, x) for y, x in path]
    
        # Top border: Adjusted to account for the number of columns
        border = "+" + "-" * len(grid[0]) + "+"
        print(border)
    
        # Print each row with characters joined by an empty string
        for y_idx, row in enumerate(grid):
            row_display = []
            for x_idx, cell in enumerate(row):
                # If we're at the person's location, mark it with 'P'
                if y_idx == person_y and x_idx == person_x:
                    row_display.append("P")
                # If we're at the target's location, mark it with 'T'
                elif y_idx == target_y and x_idx == target_x:
                    row_display.append("T")
                # If we're at a location in the path, mark it with 'r'
                elif Location(y_idx, x_idx) in path_locations:
                    row_display.append("r")
                else:
                    row_display.append(cell)  # otherwise, display the normal grid cell
    
            # Print the row with no spaces between characters (join with an empty string)
            print("|" + "".join(row_display) + "|")
    
        # Bottom border: Same as top border
        print(border)
