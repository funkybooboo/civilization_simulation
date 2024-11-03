class Scheduler:
    def __init__(self):
        # TODO: maybe change how tasks is being stored?
        self.tasks = []

    def add(self, task):
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
