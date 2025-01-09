from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Optional, Tuple
from src.logger import logger

from src.simulation.grid.location import Location

if TYPE_CHECKING:
    from src.simulation.people.people import People
    from src.simulation.people.person.person import Person


class HomeManager:
    def __init__(self, people: People):
        self._people = people

    def swap_homes(self) -> None:
        logger.debug("Start swapping homes")
        # Step 1: Get the people who are far from their work centers
        far_people: Dict[Person, Location] = self._get_peoples_centers()
        logger.debug(f"Found {len(far_people)} people far from work centers")

        # Step 2: Remove people whose homes are near their work centers
        far_people = self._filter_people_near_centers(far_people)
        logger.debug(f"Removed people whose homes are near work centers, now {len(far_people)}far people")

        # Step 3: Match and swap homes for people within 20 blocks
        matches: List[Tuple[Person, Person]] = self._find_matches(far_people, 20)
        self._swap_home_assignments(matches)
        logger.debug(f"Swapped homes for those within 20 blocks")

        # Step 4: Remove matched people from the list
        self._remove_matched_people(far_people, matches)
        logger.debug(f"Removed matched people from list")

        # Step 5: Match and swap homes for people within 40 units
        matches = self._find_matches(far_people, 40)
        self._swap_home_assignments(matches)
        logger.debug(f"Swapped homes for those within 40 blocks")

    @staticmethod
    def _remove_matched_people(far_people: Dict[Person, Location], matches: List[Tuple[Person, Person]]) -> None:
        """Remove matched people from the far_people list"""
        for person1, person2 in matches:
            far_people.pop(person1, None)
            far_people.pop(person2, None)
            logger.debug(f"Removed person {person1} and {person2}from far people")

    @staticmethod
    def _swap_home_assignments(matches: List[Tuple[Person, Person]]) -> None:
        """Swap homes between matched people"""
        for person1, person2 in matches:
            home1, home2 = person1.get_home(), person2.get_home()
            logger.debug(f"{person1} old home {home1} and {person2} old home {home2}")
            person1.assign_home(home2)
            person2.assign_home(home1)
            logger.debug(f"{person1} new home {person1.get_home()} and {person2} new home {person2.get_home()}")

    @staticmethod
    def _find_matches(far_people: Dict[Person, Location], distance: int) -> List[Tuple[Person, Person]]:
        """Find pairs of people whose homes are within the given distance"""
        matches = []
        matched_people = set()

        for person1, center1 in far_people.items():
            if person1 in matched_people:
                logger.debug(f"{person1} is already matched")
                continue

            for person2, center2 in far_people.items():
                if person2 in matched_people or person1 == person2:
                    logger.debug(f"{person2} is already matched")
                    continue

                if person1.get_home().get_location().is_near(center2, distance):
                    matches.append((person1, person2))
                    logger.debug(f"{person1} and {person2} appended to matches")
                    matched_people.update([person1, person2])
                    logger.debug(f"{person1} and {person2} updated in matched people")

        return matches

    @staticmethod
    def _filter_people_near_centers(far_people: Dict[Person, Location]) -> Dict[Person, Location]:
        """Remove people whose homes are already near their work centers"""
        to_remove = [
            person for person, center in far_people.items() if person.get_home().get_location().is_near(center, 30)
        ]
        logger.debug(f"Found {len(to_remove)} people whose homes are near their work centers")
        # Remove the filtered people from the far_people dictionary
        for person in to_remove:
            far_people.pop(person, None)
        logger.debug(f"Removed people whose homes are near their work centers")
        return far_people

    def _get_peoples_centers(self) -> Dict[Person, Location]:
        """Return a dictionary of people and the center of their work locations"""
        far_people: Dict[Person, Location] = {}

        for person in self._people:
            if not person.get_spouse():
                logger.debug(f"{person.get_name()} has no spouse")
                center = self._calculate_center(person.get_work_structures())
                if center:
                    far_people[person] = center
                    logger.debug(f"{person.get_name()} has {center} and added to far people")
                else:
                    logger.debug(f"{person.get_name()} has no work structures, therefore no center.")

        for person in self._people.get_married_people():
            person_center = self._calculate_center(person.get_work_structures())
            spouse_center = self._calculate_center(person.get_spouse().get_work_structures())
            if not person_center and not spouse_center:
                continue
            if not person_center:
                far_people[person] = spouse_center
            elif not spouse_center:
                far_people[person] = person_center
            else:
                combined_center = self._calculate_center([person_center, spouse_center])
                if combined_center:
                    far_people[person] = combined_center
                else:
                    continue
                logger.debug(
                    f"{person.get_name()} has spouse, and combined center {combined_center} and added to far people"
                )

        return far_people

    @staticmethod
    def _calculate_center(locations: List[Location]) -> Optional[Location]:
        """Calculate the average location of a list of structures"""
        if not locations:
            logger.debug("No structures found to find center")
            return None

        total_x, total_y = sum(location.x for location in locations), sum(location.y for location in locations)
        logger.debug(f"total x: {total_x}, total y: {total_y}, number of structures: {len(locations)}")
        avg_x, avg_y = total_x // len(locations), total_y // len(locations)
        logger.debug(f"avg x: {avg_x}, avg y: {avg_y}")

        return Location(avg_x, avg_y)
