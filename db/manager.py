from array import array
import os
from re import X

tasks_file = os.path.join(os.getcwd(), 'part2','db', 'tasks.csv')

# get list of tasks
def get_all_text():
    f = open(tasks_file, "r")
    all_tasks = f.readlines()
    f.close()
    return all_tasks

# rewrites file with new list of strings
def rewrite_file(newlist):
    f = open(tasks_file, "w")
    f.writelines(newlist)
    f.close()

# creates tasks file is none exists
def create():
    if(is_tasks_file_exists()):
        return False
    else:
        f = open(tasks_file, "x")
        f.write("ID,DESCRIPTION,PRIORITY,STATUS\n")
        return True

# check if tasks file exists
def is_tasks_file_exists():
    return os.path.exists(tasks_file)

# adds a task to the task file and returns the task id.
def add_task(desc, priority):
    create()
    f = open(tasks_file, "a")
    lasttask = get_all_tasks()[-1]
    taskid = int(lasttask[0])
    taskid += 1
    task = "{taskid},{desc},{priority},Incomplete\n".format(taskid = taskid, desc = desc, priority = priority)
    f.write(task)
    f.close()
    return taskid

# returns list of tasks in the task file.
def get_all_tasks():
    create()
    f = open(tasks_file, "r")
    all_tasks = f.readlines()
    f.close()
    return all_tasks[1:]

# remove a task from the task file.
def remove_task(id):
    #reorder ids, return boolaen
    create()
    newlist = []
    all_tasks = get_all_text()
    # check if in valid range
    if(len(all_tasks) - 1 < id): return False
    del all_tasks[id]
    # uses enumerate to re-configure task numbers
    for index, task in enumerate(all_tasks):
        if(index == 0): 
            newlist.append(task)
            continue
        newlist.append(str(index) + task[1:])
    rewrite_file(newlist)
    return True

# complete a task in the task file.
def complete_task(id):
    #return boolean
    create()
    all_tasks = get_all_text()
    # check if in valid range
    if(len(all_tasks) - 1 < id): return False
    # remake task into a List of Strings -> change to complete -> put back in list
    task = all_tasks[id].split(",")
    task[3] = "Complete\n"
    completed_task = ','.join(task)
    all_tasks[id] = completed_task
    rewrite_file(all_tasks)
    return True

# change the priority of a task in the task file.
def change_priority(id, priority):
    #return boolean
    create()
    all_tasks = get_all_text()
    # check if in valid range
    if((len(all_tasks) - 1 < id) or priority <= 0 or id <= 0): return False
    task = all_tasks[id].split(",")
    task[2] = str(priority)
    changed_task = ','.join(task)
    all_tasks[id] = changed_task
    rewrite_file(all_tasks)
    return True

# update the task description of a task in the task file.
def update_desc(id, desc):
    #return boolean
    create()
    all_tasks = get_all_text()
    # check if in valid range
    if((len(all_tasks) - 1 < id) or desc == "" or id <= 0): return False
    task = all_tasks[id].split(",")
    task[1] = desc
    changed_task = ','.join(task)
    all_tasks[id] = changed_task
    rewrite_file(all_tasks)
    return True

# search for a task in the task file.
def search(id, desc, priority):
    create()
    all_tasks = get_all_tasks()
    tasks = ""
    for task in all_tasks:
        task_array = task.split(",")
        if(id != None):
            # Criteria doesn't match -> go next
            if(int(task_array[0]) != id):
                continue
            # Criteria does match -> check next criteria
        if(desc != None):
            # Criteria doesn't match -> go next
            if(task_array[1].lower() != desc.lower()):
                continue
            # Criteria does match -> check next criteria
        if(priority != None):
            # Criteria doesn't match -> go next
            if(int(task_array[2]) != priority):
                continue
            # Criteria does match -> check next criteria
        tasks += task
    return tasks

# sort the tasks in the task file. Default order is 1.
def sort(order = 1):
    create()
    accum = ""
    reverse = True if (order != 1) else False
    all_tasks = get_all_tasks()
    # List of Tasks -> List of list of task parts
    for i in range(len(all_tasks)):
        all_tasks[i] = all_tasks[i].split(",")
    # Sort by priority string value
    all_tasks.sort(reverse = reverse, key = lambda x : x[2])
    #List of list of task parts + join -> List of Tasks -> rewrite
    for array_task in all_tasks:
        task = ",".join(array_task)
        accum += task
    return accum
