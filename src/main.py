import time
from src.logger import logger, setup_logger
from src.settings import environment, settings
from src.simulation.simulation import Simulation
from src.simulation.visualization.visualizer import Visualizer


def main() -> None:
    setup_logger(environment)
    logger.info("Starting the simulation program.")

    # Access settings via the globally initialized object
    max_simulations = settings.get("max_simulations", 1)

    for i in range(max_simulations):
        logger.info(f"Running simulation {i + 1}")

        # Start timing the simulation
        start_time = time.time()

        try:
            simulation: Simulation = Simulation()
            visualizer: Visualizer = simulation.run()
            visualizer.display_town_slide_show()
            visualizer.display_simulation_stats()

        except Exception as e:
            # Log the exception if something goes wrong
            logger.error(f"An error occurred during simulation {i + 1}: {e}")
            raise
        finally:
            # End timing the simulation and log the duration
            end_time = time.time()
            simulation_duration = end_time - start_time
            logger.info(f"Simulation {i + 1} completed in {simulation_duration:.2f} seconds")


if __name__ == "__main__":
    main()
