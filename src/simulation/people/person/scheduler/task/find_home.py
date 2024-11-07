from src.simulation.people.person.scheduler.task.task import Task


class FindHome(Task):
    def __init__(self, simulation, person):
        super().__init__(simulation, person, 5)

    def execute(self):
        if not self._person.has_home():
            # TODO: find a home for the person
            self._person.assign_home()
        else:
            self._finished()
            