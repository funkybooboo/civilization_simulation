from random import Random


class Person:
    def __init__(self):
        self.health: int = 100
        self.hunger: int = 100  # when your hunger gets below 25, health starts going down; when it gets above 75, health starts going up
        self.age = 0
        self.home = None
        self.spouse = None
        self.scheduler = self.Scheduler()
        # TODO: add a memory; it's a list of tuples

    def takeTurn(self, task):
        tasks = []
        # TODO: Check hunger and other stuff to see if you need to do a task, and add those tasks to the tasks list
        for task in tasks:
            self.scheduler.addTask(task)

    def move():
        # TODO: Move around and remember things as you move
        pass

    class Scheduler:
        def __init__(self):
            # TODO: maybe change how tasks is being stored?
            self.tasks = []

        def addTask(self, task):
            # TODO: add task to the queue using a scheduling algorithm
            pass

# ======== NOTES ON HOW THIS SHOULD WORK ==========

# task is an abstract class; scheduler uses its fields
# when a task is on the front of the queue, [scheduler?] calls task.getLocation() 
    # and if the person isn't there, then task.moveTo(), 
    # and if the person is there, then task.execute()
# when a task is done, scheduler pops the task off the queue 
    # and calls task.execute([reference to that person], [reference to the environment])
# task.execute() will update the person and environment as necessary, depending on what task it is

# SCHEDULER
# check if there's a task currently running
# get its priority
# check the task scheduled next on the queue
# see if you should swap the two tasks
# execute the task that you're doing
