# Echoes of Eden

## Summary

Echoes of Eden is a civilization simulation. The simulation starts with a small, stable village in the middle of a
forest. Each person in the village has a set of tasks they can do, including gathering resources, building structures, 
having a family, and exploring. They are also aware of various personal metrics such as health, hunger, and family 
status. Villagers choose what tasks to do based on these personal metrics, and by using various epsilon-greedy 
algorithms.

The simulation uses a 2D array to map the village and keep track of where each villager is. As villagers move around the
map, they can remember which structures they have passed. They use this memory to know where to find things later and 
determine what tasks need to be done. Villagers also have an inventory that enforces a limit on how many resources they 
can carry at a time.

After a set amount of iterations (mimicking some amount of years), the simulation will finish and print graphs and 
statistics about the village. The purpose of these is for use in analyzing how successful the simulation's 
decision-making algorithms are at keeping the village alive and thriving.

## How to Run

This program uses poetry to manage dependencies. Before running the program, install poetry. Then install the program's 
dependencies using `poetry shell` and `poetry install`. 

All settings used throughout the program are stored in `example.dev_settings.yaml` (the settings used during 
development) and `example.prod_settings.yaml` (the settings used during production). Before running the program, change 
these file names to `dev_settings.yaml` and `prod_settings.yaml`.

Then, to run the simulation, run `PYTHONPATH=$(pwd) python3 src/main.py`. The simulation will take some time to complete. 
You will get the simulation results plotted as output of the program.

## Code Structure

The project directories are organized like so:

src
* `logger.py`: logs messages to the console about what is happening in the simulation as it runs
* `main.py`: runs the simulation
* `settings.py`: loads settings from the settings.yaml file into a global 'settings' variable
* simulation
  * `simulation.py`: the actual simulation: stores people, iterations, and grid, and contains methods for creating disasters and running the simulation
  * grid
    * `disjoint_set.py`: used to group work structures to ensure they have the same yield function, i.e., groves of trees have the same wood yield.
    * `grid.py`: a 2D array for mapping the simulation spatially, including locations of structures and people
    * `grid_disaster_generator.py`: generates grid-related disasters like mine disaster, stolen resources, or forest fire
    * `grid_generator.py`: generates a unique grid each time, with a small starting village and surrounding forest
    * `location.py`: handles logic about a specific location, such as travel time to another place, or determining what's nearby
    * `structure_generator.py`: generates structures within the grid
    * `temperature.py`: manages the temperature for every day of the year; temperature is taken from a normal distribution, using a mean from a sin wave that spans the year
    * structure
      * `structure.py`: an abstract class, handles location/placement of structure on grid
      * `structure_factory.py`: manages the creation of structures
      * `structure_type.py`: an enum used in the code to identify structure types
      * store
        * `barn.py`: storage for food, wood and stone
        * `home.py`: storage for a person's food
        * `store.py`: an abstract class, handles the implementation for all storage types
      * work
        * `farm.py`: yields food
        * `mine.py`: yields stone
        * `tree.py`: yields wood
        * `work.py`: an abstract class, handles the implementation for all work types
        * construction
          * `construction.py`: an abstract class, handles the implementation for all construction types
          * `construction_barn.py`: when completed a `barn` will take its place
          * `construction_farm.py`: when completed a `farm` will take its place
          * `construction_home.py`: when completed a `home` will take its place
          * `construction_mine.py`: when completed a `mine` will take its place
  * people
    * `home_manager.py`: handles all logic for people swapping homes
    * `people.py`:  handles all logic for the general population or people
    * `people_disaster_generator.py`: creates disasters that directly involve people: divorce, sickness, craving, death, forget tasks, sleepwalk, baby boom
    * `people_generator.py`: creates each person, assigning an age, name, and location spawned.
    * person
      * `backpack.py`: handles all logic for a person's inventory
      * `memories.py`: handles all logic for a person's memory
      * `person.py`: handles all logic for a person's actions
      * `thinker.py`: handles all logic for adding tasks and adjusting task priorities for a person
      * movement
        * `move_result.py`: defines class MoveResult for storing if a call to move_to succeeded and resulted in a structure 
        * `mover.py`: handles all lower-level logic for moving a person around the grid
        * `navigator.py`: handles all higher-level logic for moving a person around the grid
        * `vision.py`: handles all logic for what a person can see around them as they move around the grid
      * scheduler
        * `scheduler.py`: handles all logic for which task should be executed at what time based on priority values
        * task
          * `eat.py`: represents task of eating
          * `explore.py`: represents task of exploring the grid
          * `find_home.py`: represents task of finding a home
          * `find_spouse`: represents task of finding a spouse
          * `task.py`: an abstract class, with abstract methods for each task type to override
          * `task_factory.py`: manages the creation of tasks
          * `task_type.py`: an enum used in the code to identify task types
          * `transport.py`: represents task of transporting items to a location
          * construction
            * `build.py`: an abstract class, handles logic of building at an already declared construction site for all structure types
            * `build_barn.py`: represents task of building a barn at the already declared construction site
            * `build_farm.py`: represents task of building a farm at the already declared construction site
            * `build_home.py`: represents task of building a home at the already declared construction site
            * `build_mine.py`: represents task of building a mine at the already declared construction site
          * start_construction
            * `start_barn_construction.py`: represents task of starting construction site for barn
            * `start_construction.py`: an abstract class, handles logic of starting construction for all structure types
            * `start_farm_construction.py`: represents task of starting construction site for farm
            * `start_home_construction.py`: represents task of starting construction site for home
            * `start_mine_construction.py`: represents task of starting construction site for mine
          * work
            * `chop_tree.py`: represents task of chopping tree
            * `work.py`: an abstract class, handles logic of all types of work actions
            * `work_farm.py`: represents task of working farm 
            * `work_mine.py`: represents task of working mine
  * visualization
    * `visualizer.py`: manages and displays town grid and simulation stats using grid and state plotters
    * plotter
      * `grid_plotter.py`: generates and visualizes random grid snapshots with terrain types, displaying them as a slideshow
      * `state_plotter.py`: aggregates and visualizes simulation states (e.g., grid, people, resources) over time through line plots.
    * state
      * `grid_disaster_state.py`: Initialize grid disaster attributes based on counts
      * `grid_state.py`: establishes counts of grid values (barns, homes, mines, constructions, ...)
      * `people_disaster_state.py`: Initialize people disaster attributes based on counts
      * `people_state.py`: establishes averages for people values (hunger, health, etc.)
      * `resource_state.py`: calculates/stores resource data for barns
      * `state.py`: generating and formatting state data
      * `task_state.py`: calculates/stores task data for 


## Dev Tools

1. A more comprehensive tool that checks for errors, enforces a coding standard, and looks for code smells.
   - `poetry run pylint src/**/*.py`
2. A static type checker for Python that can help catch type errors.
   - `poetry run mypy src/**/*.py`
3. An opinionated code formatter that enforces a consistent style.
   - `poetry run black src/**/*.py`
   - `poetry run isort src/**/*.py`
   - `poetry run autoflake --in-place --remove-unused-variables src/**/*.py`

## Licence

This project uses the MIT license. (See the 'LICENSE' file in this directory.)
