from typing import Dict

import matplotlib.pyplot as plt
import seaborn as sns

from state import State
from src.simulation.grid.grid import Grid
from src.simulation.people.people import People


class StatePlotter:
    def __init__(self):
        self._years: Dict[int, State] = {}

    def add(self, year: int, grid: Grid, people: People):
        self._years[year] = State(grid, people)
    
    def plot_simulation_states(self):
        pass
