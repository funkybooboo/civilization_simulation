from enum import Enum, auto


class TaskType(Enum):
    EAT = auto()
    FIND_HOME = auto()
    FIND_SPOUSE = auto()

    WORK_FARM = auto()
    WORK_MINE = auto()
    CHOP_TREE = auto()
    STORE_STUFF = auto()

    BUILD_HOME = auto()
    BUILD_FARM = auto()
    BUILD_MINE = auto()
    BUILD_BARN = auto()

    EXPLORE = auto()
