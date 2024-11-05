from src.simulation.people.person.memory import Memory
from src.simulation.people.person.mover import Mover
from src.simulation.people.person.scheduler.scheduler import Scheduler
from src.simulation.people.person.scheduler.task.task_type import TaskType
from src.simulation.people.person.vision import Vision


class Person:
    def __init__(self, simulation, name, pk, location, age):

        self._simulation = simulation
        self._name = name
        self._pk = pk
        self._age = age
        # how many blocks can the person move in one turn
        self._speed = 10
        # how many blocks can the person see
        self._visibility = 30
        # where the person is located
        # (x, y)
        self._location = location

        self._memory = Memory()

        self._vision = Vision(self)

        self._mover = Mover(self)

        self._health: int = 100
        self._hunger: int = (
            100  # when your hunger gets below 25, health starts going down; when it gets above 75, health starts going up
        )
        self._home = None
        self._spouse = None
        self._scheduler = Scheduler()

    def take_action(self):
        self._hunger -= 1  # TODO adjust

        if self._hunger < 20:
            self._health -= 1
        elif self._hunger > 80:
            self._health += 1

        if not self._home:
            self._scheduler.add(TaskType.FIND_HOME)

        if not self._spouse:
            self._scheduler.add(TaskType.FIND_SPOUSE)
        else:
            # TODO chance to have a baby
            pass

        if self._hunger < 50:
            self._scheduler.add(TaskType.EAT)

        task = self._scheduler.get()
        task.execute()

    def is_dead(self):
        return self._health <= 0 or self._age >= 80

    def eat(self):
        self._hunger += 10

    def assign_spouse(self, spouse):
        self._spouse = spouse

    def assign_home(self, home):
        self._home = home

    def age(self):
        self._age += 1

    def __str__(self):
        pass  # TODO implement what to print for a person
