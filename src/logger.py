from loguru import logger
import sys
import os

# Create a logs directory if it doesn't exist
log_dir = "../logs"
os.makedirs(log_dir, exist_ok=True)

# Define log file path
log_file_path = os.path.join(log_dir, "app.log")

# Configure the logger
logger.remove()  # Remove the default logger
logger.add(sys.stdout, level="INFO", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")  # Log to console
logger.add(log_file_path,
           rotation="1 MB",        # Rotate after 1 MB
           retention="10 days",    # Keep logs for 10 days
           compression="zip",      # Compress old logs
           level="DEBUG",          # Log level for the file
           format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")  # Log format

# Optional: Customize exception logging
logger.add("error.log", level="ERROR", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")

# Example function to demonstrate usage
def log_example():
    logger.info("Logger is set up and ready to use!")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")

if __name__ == "__main__":
    log_example()
