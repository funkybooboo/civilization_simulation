from src.simulation.grid.grid import Grid
from src.simulation.people.people import People
from src.simulation.visualization.state.grid_disaster_state import GridDisasterState
from src.simulation.visualization.state.grid_state import GridState
from src.simulation.visualization.state.people_disaster_state import PeopleDisasterState
from src.simulation.visualization.state.people_state import PeopleState
from src.simulation.visualization.state.resource_state import ResourceState
from src.simulation.visualization.state.task_state import TaskState


class State:
    def __init__(self, grid: Grid, people: People):
        self._grid_disaster_state: GridDisasterState = GridDisasterState(grid)
        self._grid_state: GridState = GridState(grid)
        self._people_disaster_state: PeopleDisasterState = PeopleDisasterState(people)
        self._people_state: PeopleState = PeopleState(people)
        self._resource_state: ResourceState = ResourceState(grid)
        self._task_state: TaskState = TaskState(people)
