# Given a list of tasks, determine the total running time (duration) to 
# complete all tasks. Assume there is no limit to the number of concurrent
# tasks you can run. 
#
# Example: 
# [ 
#   {'id': 1, 'duration': 1, 'dependencies': []}, 
#   {'id': 2, 'duration': 2, 'dependencies': [1]}, 
#   {'id': 3, 'duration': 1, 'dependencies': [2,5]}, 
#   {'id': 4, 'duration': 3, 'dependencies': [1]}, 
#   {'id': 5, 'duration': 1, 'dependencies': [2]}, 
# ]
# 
# ANSWER: 5
# Why? Execution sequence 1->2->5->3 is longest with total duration of 5
#  

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

task_list_2 = [ 
  {'id': 1, 'duration': 1, 'dependencies': []}, 
  {'id': 2, 'duration': 2, 'dependencies': [1]}, 
  {'id': 3, 'duration': 1, 'dependencies': [2,5]}, 
  {'id': 4, 'duration': 3, 'dependencies': [1]}, 
  {'id': 5, 'duration': 1, 'dependencies': [2]}, 
]
