from src.simulation.people.person.scheduler.task.task import Task


class Eat(Task):
    def __init__(self, simulation, person):
        super().__init__(simulation, person, 10)

    def execute(self):
        # TODO if not at house then move to house
        # else
        self._person.eat()
