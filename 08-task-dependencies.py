import collections
import copy
import heapq

# Given a list of tasks, determine if there is a valid schedule to complete
# them and the total running time (duration) to complete all tasks. 

# TODO: cycle detection (ordered dictionary)
# TODO: add priority queue to execution plan

class Task:
    def __init__(self, id, duration, dependencies):
        self.id = id
        self.dependencies = dependencies 
        self.duration = duration

def dfs(task : Task, graph, current_path, all_paths, visited):
    if task.id in visited: 
        return False
    else:
        visited.add(task.id)
    adj_nodes = graph[task.id]
    if len(adj_nodes) == 0:
        # we found a terminal path
        all_paths.append(copy.deepcopy(current_path))
    else:
        for next_task in adj_nodes:
            current_path.append(next_task)
            if not dfs(next_task, graph, current_path, all_paths, visited):
                #loop detected
                return False
            current_path.pop()
            visited.remove(next_task.id)
    return True

# Return the total runtime to complete all tasks assuming unlimited 
# concurrency. Return -1 if no valid schedule exists. 
def calculate_runtime(task_list):

    start_tasks = list()
    task_graph = collections.defaultdict(list)

    for task in task_list:
        if len(task.dependencies) == 0:
            start_tasks.append(task)
        else:
            for d in task.dependencies:
                task_graph[d].append(task)

    all_paths = list()

    loop_free = True
    for task in start_tasks:
        current_path = list()
        current_path.append(task)
        if not dfs(task, task_graph, current_path, all_paths, visited=set()):
            # loop was detected
            return -1
    
    max_duration = 0

    for path in all_paths:
        path_duration = 0
        for task in path:
            path_duration+= task.duration
            print("{}-> ".format(task.id), end="")
        print("Total: {}".format(path_duration))
        max_duration = max(max_duration, path_duration)
    
    return max_duration

def show_execution_plan(task_list): # consider using a priority list to show start-times
    start_tasks = list()
    task_graph = collections.defaultdict(list)

    for task in task_list:
        if len(task.dependencies) == 0:
            start_tasks.append(task)
        else:
            for d in task.dependencies:
                task_graph[d].append(task)

    ready_to_run = list()
    ready_to_run.extend(start_tasks)
    completed = set()

    while len(ready_to_run) > 0:
        for task in ready_to_run:
            completed.add(task.id)
            print(task.id, end=" ")
        print()
        ready_children = list()
        for task in ready_to_run:
            for child in task_graph[task.id]:
                if completed >= set(child.dependencies):
                    # the operation above is a set comparison.
                    # it is true if all members of the right-hand 
                    # set are also members of the left-hand set.
                    # https://docs.python.org/3/library/stdtypes.html#set
                    ready_children.append(child)
        ready_to_run.clear()
        ready_to_run.extend(ready_children)

def show_execution_plan_2(task_list): # consider using a priority list to show start-times
    start_tasks = list()
    task_graph = collections.defaultdict(list)

    for task in task_list:
        if len(task.dependencies) == 0:
            start_tasks.append(task)
        else:
            for d in task.dependencies:
                task_graph[d].append(task)

    completed = set()
    priority_q = list()

    while(len(start_tasks) > 0):
        # print tasks that are starting in this round
        for task in start_tasks:
            print(task.id, end=" ")
            heapq.heappush(priority_q, (task.duration, task))
        start_tasks.clear()
        print()

        # find all running tasks with earliest duration
        completed_tasks_round = list()
        t = heapq.heappop(priority_q)
        completed_tasks_round.append(t[1])
        completed.add(t[1].id)
        while(len(priority_q) > 0 and t[0] == priority_q[0][0]):
            t = heapq.heappop(priority_q)
            completed_tasks_round.append(t[1])
            completed.add(t[1].id)

        # process completed tasks 
        for task in completed_tasks_round:
            for child in task_graph[task.id]:
                if completed >= set(child.dependencies):
                    # the operation above is a set comparison.
                    # it is true if all members of the right-hand 
                    # set are also members of the left-hand set.
                    # https://docs.python.org/3/library/stdtypes.html#set
                    start_tasks.append(child)
  

task_list = list()
task_list.append(Task(1, 1, []))
task_list.append(Task(2, 2, [1]))
task_list.append(Task(3, 1, [2, 5]))
task_list.append(Task(4, 3, [1]))
task_list.append(Task(5, 1, [2]))

run_time = calculate_runtime(task_list)
if(run_time >= 0):  
    print("Total RunTime: {}".format(calculate_runtime(task_list)))
    print("Execution Plan:")
    show_execution_plan(task_list)
    print("Execution Plan:")
    show_execution_plan_2(task_list)
else:
    print("Invalid Task Graph! Loop Detected")


