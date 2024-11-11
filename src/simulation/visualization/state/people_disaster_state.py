from src.simulation.people.people import People
from src.simulation.visualization.state.state import State


class PeopleDisasterState(State):
    def __init__(self, people: People):
        self._people = people

        # TODO

        del self._people
