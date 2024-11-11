import re
from abc import ABC
from numbers import Number
from typing import Dict, Tuple


class State(ABC):
    def get_data(self) -> Tuple[str, Dict[str, Number]]:
        """
        Returns the data dictionary with labels formatted and mapped to their corresponding values.
        Subclasses should implement this method to specify the class-specific title and attributes.
        """
        title = (
            self.get_title()
        )  # Get the title dynamically using each subclass's title
        data = self._data_generator()  # Use the common data generation logic
        return title, data

    def _data_generator(self) -> Dict[str, Number]:
        """
        Generates a dictionary with human-readable labels for the attributes and their corresponding values.
        """
        data = {}

        # Iterate over instance variables (attributes)
        for attr_name, value in vars(self).items():
            # Skip private attributes (those starting with '_')
            if not attr_name.startswith("_"):
                # Generate a human-readable label
                label = self._format_label(attr_name)
                # Add to the data dictionary
                data[label] = value

        return data

    @staticmethod
    def _format_label(field_name: str) -> str:
        """
        Format the attribute name into a human-readable label:
        - Split by underscores
        - Capitalize each word
        - Join with spaces
        """
        return " ".join(word.capitalize() for word in field_name.split("_"))

    def get_title(self) -> str:
        """
        Dynamically generate the title from the class name:
        - Split the class name into words
        - Replace "State" with "Stats"
        - Join the words with spaces
        """
        class_name = self.__class__.__name__

        # Split class name at uppercase letters to handle camelCase format
        words = re.sub("([a-z])([A-Z])", r"\1 \2", class_name).split()

        # Replace 'State' with 'Stats' and join the words with spaces
        title = " ".join(words).replace("State", "Stats")
        return title
