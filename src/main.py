import argparse
import os
from argparse import ArgumentParser, Namespace

from dotenv import load_dotenv

from src.logger import logger, setup_logger
from src.simulation.simulation import Simulation
from src.simulation.visualization.state_tracker import StateTracker


def main() -> None:
    environment: str = get_environment()
    setup_logger(mode=environment)

    logger.info("Starting the simulation program.")

    load_dotenv(f"../env/{environment}.env")
    logger.debug(f"Loaded environment variables from ../env/{environment}.env")

    max_simulations: int = int(os.getenv("MAX_SIMULATIONS", "10"))
    actions_per_day: int = int(os.getenv("ACTIONS_PER_DAY", "5"))
    days_per_year: int = int(os.getenv("DAYS_PER_YEAR", "365"))
    years: int = int(os.getenv("YEARS", "50"))
    grid_size: int = int(os.getenv("GRID_SIZE", "100"))

    logger.info(
        f"Configuration: ACTIONS_PER_DAY={actions_per_day}, DAYS_PER_YEAR={days_per_year}, YEARS={years}, GRID_SIZE={grid_size}"
    )

    for i in range(max_simulations):
        logger.info(f"Running simulation {i + 1}")
        simulation: Simulation = Simulation(
            actions_per_day, days_per_year, years, grid_size
        )
        tracker: StateTracker = simulation.run()

        tracker.display_simulation_stats()
        tracker.display_town_slide_show()

        logger.info(f"Simulation {i + 1} completed")


def get_environment() -> str:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Run the simulation program."
    )
    parser.add_argument(
        "--env", type=str, default="dev", help="Specify the environment (default: dev)"
    )
    args: Namespace = parser.parse_args()
    return args.environment


if __name__ == "__main__":
    main()
