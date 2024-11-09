from numbers import Number
from typing import Dict

from matplotlib import pyplot as plt
import seaborn as sns

from src.simulation.grid.grid import Grid
from src.simulation.people.people import People
from src.simulation.visualization.state.grid_disaster_state import GridDisasterState
from src.simulation.visualization.state.grid_state import GridState
from src.simulation.visualization.state.people_disaster_state import PeopleDisasterState
from src.simulation.visualization.state.people_state import PeopleState
from src.simulation.visualization.state.resource_state import ResourceState
from src.simulation.visualization.state.task_state import TaskState


class StatePlotter:
    def __init__(self):
        # { title: { year: { label: number } } }
        self._states: Dict[str, Dict[int, Dict[str, Number]]] = {}

    def add(self, year: int, grid: Grid, people: People):
        # Define state classes to process
        states = [
            GridDisasterState(grid),
            GridState(grid),
            PeopleDisasterState(people),
            PeopleState(people),
            ResourceState(grid),
            TaskState(people)
        ]

        # Add data for each state class
        for state in states:
            title, data = state.get_data()
            self._add_state_data(title, year, data)

    def _add_state_data(self, title: str, year: int, data: Dict[str, Number]):
        """
        Helper method to add data to the states dictionary.
        Ensures that the state is initialized if it doesn't exist.
        """
        if title not in self._states:
            self._states[title] = {}
        self._states[title][year] = data

    def plot(self):
        """
        Generate plots for each state category stored in `_states`.
        Each title in `_states` will get its own plot with data for each year.
        """
        for title, data in self._states.items():
            self._plot(title, data)

    @staticmethod
    def _plot(title: str, lines: Dict[int, Dict[str, Number]]):
        """
        Plots lines for each label over the years.
        
        :param title: A string to be used as the title of the plot. Default is "Line Plot of Data Over Years".
        :param lines: A dictionary where keys are years (int) and values are dictionaries, 
                      where each dictionary maps labels (str) to numerical values (int/float).
        """
        # Prepare data for plotting
        years = sorted(lines.keys())

        # We will store data for each label over time
        labels_data = {}

        # Loop through each year and accumulate the data for each label
        for year in years:
            year_data = lines[year]  # The data for this year is a dictionary of {label: value}
            for label, value in year_data.items():
                if label not in labels_data:
                    labels_data[label] = {'years': [], 'values': []}
                labels_data[label]['years'].append(year)
                labels_data[label]['values'].append(value)

        # Now plot the lines for each label
        plt.figure(figsize=(10, 6))

        for label, data in labels_data.items():
            sns.lineplot(x=data['years'], y=data['values'], label=label)

        # Add titles and labels
        plt.title(title)
        plt.xlabel("Year")
        plt.ylabel("Value")
        plt.legend(title="Labels")

        # Show the plot
        plt.show()
