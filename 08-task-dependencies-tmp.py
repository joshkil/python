# Given a list of tasks, determine if there is a valid schedule to complete
# them and the total running time (duration) to complete all tasks. 

class Task:
    def __init__(self, id, duration, dependencies):
        self.id = id
        self.dependencies = dependencies 
        self.duration = duration

# Return the duration of the schedule assuming unlimited concurrency 
# of tasks and return the duration of the schedule
# Return -1 if no valid schedule exists. 
def calculateSchedule(task_list):
    return 0

task_list = list()
task_list.append(Task(1, 1, []))
task_list.append(Task(2, 2, [1]))
task_list.append(Task(3, 1, [2, 5]))
task_list.append(Task(4, 3, [1]))
task_list.append(Task(5, 1, [2]))

