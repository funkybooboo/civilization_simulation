import os
from dotenv import load_dotenv
from logger import setup_logger, logger
from simulation.simulation import Simulation

def main():
    # Set up the logger based on the desired environment
    environment = 'dev'  # Change this to 'prod' for production mode
    setup_logger(mode=environment)

    logger.info("Starting the simulation program.")

    load_dotenv(f'../env/{environment}.env')
    logger.debug(f"Loaded environment variables from ../env/{environment}.env")

    actions_per_day = int(os.getenv('ACTIONS_PER_DAY', 5))
    days_per_year = int(os.getenv('DAYS_PER_YEAR', 365))
    years = int(os.getenv('YEARS', 50))
    grid_size = int(os.getenv('GRID_SIZE', 100))

    logger.info(f"Configuration: ACTIONS_PER_DAY={actions_per_day}, DAYS_PER_YEAR={days_per_year}, YEARS={years}, GRID_SIZE={grid_size}")

    for i in range(10):
        logger.info(f"Running simulation {i + 1}")
        simulation = Simulation(actions_per_day, days_per_year, years, grid_size)
        stats = simulation.run()
        logger.info(f"Simulation {i + 1} completed with stats: {stats}")

        # TODO display stats
        logger.debug(f"Stats for simulation {i + 1}: {stats}")

if __name__ == "__main__":
    main()
