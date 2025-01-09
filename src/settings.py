import argparse
import os
import yaml
from typing import Dict, Any


class Settings:
    def __init__(self, e: str):
        """Initialize Settings and load environment-specific configurations."""
        self._settings: Dict[str, Any] = self._load_settings(e)

    @staticmethod
    def _load_settings(e: str) -> Dict[str, Any]:
        """Load settings from the environment-specific yaml file"""
        settings_file = f"../settings/{e}_settings.yaml"
        if not os.path.isfile(settings_file):
            raise FileNotFoundError(f"Settings file {settings_file} not found.")

        # Load the YAML file into a dictionary
        with open(settings_file, "r") as file:
            s = yaml.safe_load(file)

        return s

    def get(self, key: str, default=None):
        """Get a configuration value by key."""
        value = self._settings.get(key)
        if value is None:
            return default
        return value


# Helper function to get environment from command line args
def get_environment() -> str:
    """Get the environment from command-line arguments (e.g., dev, prod)."""
    parser = argparse.ArgumentParser(description="Run the simulation program.")
    parser.add_argument("--settings", type=str, default="dev", help="Specify the environment (default: dev)")
    args = parser.parse_args()
    return args.settings


# Get the environment and load settings
environment = get_environment()
settings = Settings(environment)  # This will initialize the global `settings` object

# Example of accessing a setting
print(settings.get("max_simulations"))  # Should print: 1 (based on your example YAML)
