from building import Building
from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location


class Barn(Building):
    def __init__(self, grid: Grid, location: Location) -> None:
        super().__init__(grid, location, 3, 3, "b", "B")
        self.max_capacity = 500  # Set the total capacity for all items
        self.inventory = {"food": 0, "wood": 0, "stone": 0}  # Initial inventory counts for each item

    def total_items(self) -> int:
        """Returns the total number of items in the barn."""
        return sum(self.inventory.values())

    def has_space_for(self, item_type: str, amount: int) -> bool:
        """Checks if there's enough space to add the specified amount of an item type."""
        return self.total_items() + amount <= self.max_capacity

    def add_item(self, item_type: str, amount: int) -> bool:
        """Attempts to add an item to the barn. Returns True if successful, False otherwise."""
        if item_type in self.inventory and self.has_space_for(item_type, amount):
            self.inventory[item_type] += amount
            return True
        return False

    def remove_item(self, item_type: str, amount: int) -> bool:
        """Attempts to remove an item from the barn. Returns True if successful, False otherwise."""
        if item_type in self.inventory and self.inventory[item_type] >= amount:
            self.inventory[item_type] -= amount
            return True
        return False

    def get_inventory(self) -> dict:
        """Returns the current inventory levels."""
        return self.inventory