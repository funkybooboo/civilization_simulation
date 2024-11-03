from src.simulation.people.people_generator import PeopleGenerator


class People:
    def __init__(self, simulation):
        people_generator = PeopleGenerator(simulation)
        self._people = people_generator.generate()

    def print(self):
        for person in self._people:
            print(person)

    def take_action(self):
        for person in self._people:
            person.take_action()
