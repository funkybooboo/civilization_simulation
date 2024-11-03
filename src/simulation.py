from src.grid_generator import GridGenerator
from src.people_generator import PeopleGenerator


class Simulation:
    def __init__(self, grid, people):
        grid_generator = GridGenerator(100)
        num_people = grid_generator.num_houses * 2
        people_generator = PeopleGenerator(num_people)

        self.grid = grid_generator.generate()
        self.people = people_generator.generate() # a list of all people in the simulation
        self.locations = {} # a dictionary of where all entities are on the map

    def run(self):
        # This is the main loop of the simulation
        # For every person in people:
        # Ask that person to decide what they're going to do
        
        pass