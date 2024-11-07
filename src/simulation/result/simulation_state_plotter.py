from typing import Dict

import matplotlib.pyplot as plt
import seaborn as sns

from simulation_state import SimulationState
from src.simulation.grid.grid import Grid
from src.simulation.people.people import People


class SimulationStatePlotter:
    def __init__(self):
        self._years: Dict[int, SimulationState] = {}

    def add(self, year: int, grid: Grid, people: People):
        pass
