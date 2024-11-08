import random

from src.simulation.people.people import People


class PeopleDisasterGenerator:
    def __init__(self, people: People):
        self._people = people

    def generate(self, chance: float) -> None:
        """Randomly trigger one of several disasters with a given chance."""
        if random.random() < chance:
            severity = random.randint(1, 10)  # Severity between 1 and 10

            # List of disaster methods
            disaster_methods = [
                self._divorce,
                self._sickness,
                self._craving,
                self._death,
                self._forget_tasks,
                self._sleepwalk,
                self._so_many_babies
            ]

            # Randomly pick one disaster to trigger
            chosen_disaster = random.choice(disaster_methods)
            chosen_disaster(severity)  # Call the chosen disaster method with severity

    def _divorce(self, severity: int) -> None:
        """Divorce event, causing relationship breakdown."""
        print("A divorce has occurred!")
        # Severity could influence the emotional impact, e.g., a higher severity means more loss (friends, resources)
        if severity > 5:
            print("The divorce is messy. Some resources or relationships are lost.")
        else:
            print("A calm divorce. Little impact.")

        # Logic to handle divorce: You might have relationships or resource sharing to update

    def _sickness(self, severity: int) -> None:
        """Person gets sick, losing health."""
        health_loss = severity * 2  # Example: severity increases health loss
        print(f"A person is sick! They lose {health_loss} health.")
        # Logic to reduce health of the affected person
        # self.person.health -= health_loss

    def _craving(self, severity: int) -> None:
        """Craving causes hunger to increase."""
        hunger_increase = severity * 3  # Example: severity increases hunger
        print(f"A person has a craving and eats too much! Hunger increases by {hunger_increase}.")
        # Logic to increase hunger or affect food intake
        # self.person.hunger += hunger_increase

    def _death(self, severity: int) -> None:
        """A person dies."""
        print("A person has died!")
        # You can use severity to determine the cause or impact of the death
        if severity > 5:
            print("It was a violent death. Big loss.")
        else:
            print("It was a peaceful death.")

        # Logic to handle death: Mark the person as dead
        # self.person.is_dead = True  # Mark the person as dead in your game state

    def _forget_tasks(self, severity: int) -> None:
        """Person forgets their tasks."""
        print("Someone has forgotten their tasks!")
        # Severity could affect how many tasks are forgotten or how long it lasts
        if severity > 5:
            print("They've forgotten all their tasks for the week!")
        else:
            print("They forgot a few tasks, but it's manageable.")

        # Logic to clear or reset their task list
        # self.person.tasks.clear()

    def _sleepwalk(self, severity: int) -> None:
        """A person sleepwalks into the woods."""
        print("A person is sleepwalking into the woods!")
        # Severity could determine how far they go or the danger
        if severity > 5:
            print("They've wandered deep into the woods! They might be lost.")
        else:
            print("They wandered just outside, but they're safe.")

        # Logic to move the person on the map
        # self.person.location = self._random_corner()  # Move the person to one of the corners of the map

    def _so_many_babies(self, severity: int) -> None:
        """A person or group has a baby boom."""
        print("So many babies! A new generation begins!")
        # Severity could determine how many babies are born
        babies = severity  # Severity defines the number of babies
        print(f"{babies} new babies have been born!")
        # Logic to handle the increase in population
        # self.population += babies

    def _random_corner(self):
        """Helper function to randomly return a corner of the map."""
        # Example corners for a 2D map
        corners = [(0, 0), (0, 10), (10, 0), (10, 10)]
        return random.choice(corners)
