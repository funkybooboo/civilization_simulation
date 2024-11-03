from mover import Mover
from scheduler import Scheduler
from src.simulation.people.person.memory import Memory
from vision import Vision


class Person:
    def __init__(self,
             simulation,
             name,
             pk,
             location,
             age,
         ):

        self.simulation = simulation
        self.name = name
        self.pk = pk
        self.age = age
        # how many blocks can the person move in one turn
        self.speed = 10
        # how many blocks can the person see
        self.visibility = 30
        # where the person is located
        # (x, y)
        self.location = location

        self.memory = Memory()

        self.vision = Vision(self)

        self.mover = Mover(self)

        self.health: int = 100
        self.hunger: int = 100  # when your hunger gets below 25, health starts going down; when it gets above 75, health starts going up
        self.home = None
        self.spouse = None
        self.scheduler = Scheduler()

    def take_action(self):
        tasks = []
        # if home is None then add a task to find a house
        # if spouse is None then add a task to find a spouse
        # if hunger is low then add a task to eat

        for task in tasks:
            self.scheduler.add(task)

    def is_dead(self):
        return self.health <= 0 or self.age >= 80

    def __str__(self):
        pass # TODO implement what to print for a person
