from src.simulation.people.person.scheduler.task.task import Task


class FindHome(Task):
    def __init__(self, simulation, person):
        super().__init__(simulation, person, 5)

    def execute(self):
        if not self._person.is_home():
            self._person.find_home()
        else:
            self._finished()
            