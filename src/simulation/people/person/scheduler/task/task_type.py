from enum import Enum, auto


class TaskType(Enum):
    EAT = auto()
    FIND_HOME = auto()
    FIND_SPOUSE = auto()
    # TODO add the rest of the tasks
    FIND_FARM = auto()
    FIND_MINE = auto()
    FIND_TREE = auto()
    FIND_BARN = auto()

    WORK_FARM = auto()
    WORK_MINE = auto()
    CHOP_TREE = auto()
    STORE_STUFF = auto()

    BUILD_HOME = auto()
    BUILD_FARM = auto()
    BUILD_MINE = auto()
    BUILD_BARN = auto()    
