import os
import sys

from loguru import logger


def setup_logger(mode: str = "dev") -> None:
    # Create a logs directory if it doesn't exist
    log_dir: str = "../logs"
    os.makedirs(log_dir, exist_ok=True)

    # Define log file path
    log_file_path: str = os.path.join(log_dir, "app.log")

    # Remove the default logger
    logger.remove()

    # Set log level based on mode for console logging
    console_log_level: str = "INFO"  # Log everything except DEBUG to the console
    file_log_level: str = "DEBUG"  # Log everything to the file (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    # Configure the logger to log to the console (everything except DEBUG)
    logger.add(
        sys.stdout,
        level=console_log_level,  # Don't log DEBUG messages to the console
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    )

    # Configure the logger to log to the file (everything, including DEBUG)
    logger.add(
        log_file_path,
        rotation="5 MB",  # Rotate log file after it reaches 5 MB
        retention="0 days",  # Delete rotated files immediately after rotation
        level=file_log_level,  # Log everything to the file
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    )

    # Configure the logger to log ERROR and above to a separate error log file
    logger.add(
        os.path.join(log_dir, "error.log"),
        level="ERROR",
        rotation="5 MB",  # Rotate log file after it reaches 5 MB
        retention="0 days",  # Delete rotated files immediately after rotation
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    )


if __name__ == "__main__":
    # Example usage: Pass 'prod' or 'dev' to setup the logger
    setup_logger(mode="dev")  # Change to 'prod' for production mode

    logger.debug("This is a debug message.")  # Will not appear on console, but will appear in the log file
    logger.info("This is an info message.")  # Will appear on both console and log file
    logger.warning("This is a warning message.")  # Will appear on both console and log file
    logger.error("This is an error message.")  # Will appear on both console and log file
    logger.critical("This is a critical message.")  # Will appear on both console and log file
