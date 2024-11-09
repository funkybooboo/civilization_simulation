from src.simulation.grid.building.barn import Barn
from src.simulation.grid.building.farm import Farm
from src.simulation.grid.building.home import Home
from src.simulation.grid.building.mine import Mine
from src.simulation.grid.grid import Grid
from src.simulation.grid.location import Location
from src.simulation.people.people import People
from src.simulation.people.person.scheduler.task.build_barn import BuildBarn
from src.simulation.people.person.scheduler.task.build_farm import BuildFarm
from src.simulation.people.person.scheduler.task.build_home import BuildHome
from src.simulation.people.person.scheduler.task.build_mine import BuildMine
from src.simulation.people.person.scheduler.task.chop_tree import ChopTree
from src.simulation.people.person.scheduler.task.eat import Eat
from src.simulation.people.person.scheduler.task.explore import Explore
from src.simulation.people.person.scheduler.task.find_home import FindHome
from src.simulation.people.person.scheduler.task.find_spouse import FindSpouse
from src.simulation.people.person.scheduler.task.start_barn_construction import StartBarnConstruction
from src.simulation.people.person.scheduler.task.start_farm_construction import StartFarmConstruction
from src.simulation.people.person.scheduler.task.start_home_construction import StartHomeConstruction
from src.simulation.people.person.scheduler.task.start_mine_construction import StartMineConstruction
from src.simulation.people.person.scheduler.task.work_farm import WorkFarm
from src.simulation.people.person.scheduler.task.work_mine import WorkMine


class State:
    def __init__(self, grid: Grid, people: People):
        self._grid: Grid = grid
        self._people: People = people
        
        # people stats
        self._people_count: int = len(people)
        self._average_health: float = self.get_average_health()
        self._average_hunger: float = self.get_average_hunger()

        # task stats
        self._average_complete_task_count: float = self.get_average_complete_task_count()
        self._average_active_task_count: float = self.get_average_active_task_count()
        self._average_active_build_barn_task_count: float = self.get_average_active_build_barn_task_count()
        self._average_complete_build_barn_task_count: float = self.get_average_complete_build_barn_task_count()
        self._average_active_build_farm_task_count: float = self.get_average_active_build_farm_task_count()
        self._average_complete_build_farm_task_count: float = self.get_average_complete_build_farm_task_count()
        self._average_active_build_home_task_count: float = self.get_average_active_build_home_task_count()
        self._average_complete_build_home_task_count: float = self.get_average_complete_build_home_task_count()
        self._average_active_build_mine_task_count: float = self.get_average_active_build_mine_task_count()
        self._average_complete_build_mine_task_count: float = self.get_average_complete_build_mine_task_count()
        self._average_active_chop_tree_task_count: float = self.get_average_active_chop_tree_task_count()
        self._average_complete_chop_tree_task_count: float = self.get_average_complete_chop_tree_task_count()
        self._average_active_eat_task_count: float = self.get_average_active_eat_task_count()
        self._average_complete_eat_task_count: float = self.get_average_complete_eat_task_count()
        self._average_active_explore_task_count: float = self.get_average_active_explore_task_count()
        self._average_complete_explore_task_count: float = self.get_average_complete_explore_task_count()
        self._average_active_find_home_task_count: float = self.get_average_active_find_home_task_count()
        self._average_complete_find_home_task_count: float = self.get_average_complete_find_home_task_count()
        self._average_active_find_spouse_task_count: float = self.get_average_active_find_spouse_task_count()
        self._average_complete_find_spouse_task_count: float = self.get_average_complete_find_spouse_task_count()
        self._average_active_start_barn_construction_task_count: float = self.get_average_active_start_barn_construction_task_count()
        self._average_complete_start_barn_construction_task_count: float = self.get_average_complete_start_barn_construction_task_count()
        self._average_active_start_farm_construction_task_count: float = self.get_average_active_start_farm_construction_task_count()
        self._average_complete_start_farm_construction_task_count: float = self.get_average_complete_start_farm_construction_task_count()
        self._average_active_start_home_construction_task_count: float = self.get_average_active_start_home_construction_task_count()
        self._average_complete_start_home_construction_task_count: float = self.get_average_complete_start_home_construction_task_count()
        self._average_active_start_mine_construction_task_count: float = self.get_average_active_start_mine_construction_task_count()
        self._average_complete_start_mine_construction_task_count: float = self.get_average_complete_start_mine_construction_task_count()
        self._average_active_work_farm_task_count: float = self.get_average_active_work_farm_task_count()
        self._average_complete_work_farm_task_count: float = self.get_average_complete_work_farm_task_count()
        self._average_active_work_mine_task_count: float = self.get_average_active_work_mine_task_count()
        self._average_complete_work_mine_task_count: float = self.get_average_complete_work_mine_task_count()

        # disaster stats
        # TODO count up the disasters for this year and the disaster types

        # grid stats
        self._barn_count: int = self.get_barn_count()
        self._construction_barn_count: int = self.get_construction_barn_count()
        self._farm_count: int = self.get_farm_count()
        self._construction_farm_count: int = self.get_construction_farm_count()
        self._mine_count: int = self.get_mine_count()
        self._construction_mine_count: int = self.get_construction_mine_count()
        self._home_count: int = grid.get_home_count()
        self._construction_home_count: int = self.get_construction_home_count()
        self._tree_count: int = self.get_tree_count()
        
        # resource stats
        self._total_food: int = self.get_total_food()
        self._total_stone: int = self.get_total_stone()
        self._total_wood: int = self.get_total_wood()
        self._total_capacity: int = self.get_total_barn_capacity()
        self._total_remaining_capacity: int = self.get_total_remaining_capacity()

    def get_average_health(self) -> float:
        average_health: float = 0.0
        for person in self._people:
            average_health += person.get_health()
        average_health /= len(self._people)
        return average_health

    def get_average_hunger(self) -> float:
        average_hunger: float = 0.0
        for person in self._people:
            average_hunger += person.get_hunger()
        average_hunger /= len(self._people)
        return average_hunger

    def _get_average_task_count_with_predicate(self, task_predicate: callable) -> float:
        total_count = 0.0
        for person in self._people:
            total_count += sum(1 for task in person.get_scheduler().get_all_tasks() if task_predicate(task))
        average = total_count / len(self._people) if self._people else 0.0
        return average

    def get_average_complete_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: task.is_finished()
        )

    def get_average_active_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: not task.is_finished()
        )

    def get_average_active_build_barn_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildBarn) and not task.is_finished()
        )

    def get_average_complete_build_barn_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildBarn) and task.is_finished()
        )

    def get_average_active_build_farm_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildFarm) and not task.is_finished()
        )

    def get_average_complete_build_farm_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildFarm) and task.is_finished()
        )

    def get_average_active_build_home_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildHome) and not task.is_finished()
        )

    def get_average_complete_build_home_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildHome) and task.is_finished()
        )

    def get_average_active_build_mine_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildMine) and not task.is_finished()
        )

    def get_average_complete_build_mine_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, BuildMine) and task.is_finished()
        )

    def get_average_active_chop_tree_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, ChopTree) and not task.is_finished()
        )

    def get_average_complete_chop_tree_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, ChopTree) and task.is_finished()
        )

    def get_average_active_eat_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, Eat) and not task.is_finished()
        )

    def get_average_complete_eat_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, Eat) and task.is_finished()
        )

    def get_average_active_explore_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, Explore) and not task.is_finished()
        )

    def get_average_complete_explore_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, Explore) and task.is_finished()
        )

    def get_average_active_find_home_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, FindHome) and not task.is_finished()
        )

    def get_average_complete_find_home_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, FindHome) and task.is_finished()
        )

    def get_average_active_find_spouse_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, FindSpouse) and not task.is_finished()
        )

    def get_average_complete_find_spouse_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, FindSpouse) and task.is_finished()
        )

    def get_average_active_start_barn_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartBarnConstruction) and not task.is_finished()
        )

    def get_average_complete_start_barn_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartBarnConstruction) and task.is_finished()
        )

    def get_average_active_start_farm_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartFarmConstruction) and not task.is_finished()
        )

    def get_average_complete_start_farm_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartFarmConstruction) and task.is_finished()
        )

    def get_average_active_start_home_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartHomeConstruction) and not task.is_finished()
        )

    def get_average_complete_start_home_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartHomeConstruction) and task.is_finished()
        )

    def get_average_active_start_mine_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartMineConstruction) and not task.is_finished()
        )

    def get_average_complete_start_mine_construction_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, StartMineConstruction) and task.is_finished()
        )

    def get_average_active_work_farm_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, WorkFarm) and not task.is_finished()
        )

    def get_average_complete_work_farm_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, WorkFarm) and task.is_finished()
        )

    def get_average_active_work_mine_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, WorkMine) and not task.is_finished()
        )

    def get_average_complete_work_mine_task_count(self) -> float:
        return self._get_average_task_count_with_predicate(
            lambda task: isinstance(task, WorkMine) and task.is_finished()
        )

    def get_construction_home_count(self) -> int:
        return sum(
            1
            for building in self._grid.get_buildings().values()
            if isinstance(building, Home) and building.is_under_construction()
        )

    def get_barn_count(self) -> int:
        return sum(
            1 for building in self._grid.get_buildings().values() 
            if isinstance(building, Barn)
        )

    def get_construction_barn_count(self) -> int:
        return sum(
            1
            for building in self._grid.get_buildings().values()
            if isinstance(building, Barn) and building.is_under_construction()
        )

    def get_farm_count(self) -> int:
        return sum(
            1 for building in self._grid.get_buildings().values() if isinstance(building, Farm)
        )

    def get_construction_farm_count(self) -> int:
        return sum(
            1
            for building in self._grid.get_buildings().values()
            if isinstance(building, Farm) and building.is_under_construction()
        )

    def get_mine_count(self) -> int:
        return sum(
            1 for building in self._grid.get_buildings().values() if isinstance(building, Mine)
        )

    def get_construction_mine_count(self) -> int:
        return sum(
            1
            for building in self._grid.get_buildings().values()
            if isinstance(building, Mine) and building.is_under_construction()
        )

    def get_tree_count(self) -> int:
        count: int = 0
        for i in range(len(self._grid.get_grid())):
            for j in range(len(self._grid.get_grid()[i])):
                location: Location = Location(i, j)
                if self._grid.is_tree(location):
                    count += 1
        return count

    def get_total_food(self) -> int:
        total_food = 0
        for barn in self._grid.get_barns():
            total_food += barn.get_food_stored()
        return total_food

    def get_total_stone(self) -> int:
        total_stone = 0
        for barn in self._grid.get_barns():
            total_stone += barn.get_stone_stored()
        return total_stone

    def get_total_wood(self) -> int:
        total_wood = 0
        for barn in self._grid.get_barns():
            total_wood += barn.get_wood_stored()
        return total_wood

    def get_total_barn_capacity(self) -> int:
        total_capacity = 0
        for barn in self._grid.get_barns():
            total_capacity += barn.get_capacity()
        return total_capacity

    def get_total_remaining_capacity(self) -> int:
        total_remaining_capacity = 0
        # Get the list of barns from the grid
        barns = self._grid.get_barns()

        # Calculate the remaining capacity for each barn
        for barn in barns:
            remaining_capacity = barn.get_remaining_capacity()
            total_remaining_capacity += remaining_capacity

        return total_remaining_capacity
