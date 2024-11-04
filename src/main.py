import os
from dotenv import load_dotenv
from simulation.simulation import Simulation


def main():
    # TODO logging
    environment = 'dev'
    load_dotenv(f'../env/{environment}.env')
    actions_per_day = os.getenv('ACTIONS_PER_DAY', 5)
    days_per_year = os.getenv('DAYS_PER_YEAR', 365)
    years = os.getenv('YEARS', 50)
    grid_size = os.getenv('GRID_SIZE', 100)
    # TODO other config info
    
    for _ in range(10):
        simulation = Simulation(actions_per_day, days_per_year, years, grid_size)
        stats = simulation.run()
        # TODO display stats


if __name__ == "__main__":
    main()
