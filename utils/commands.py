# import db/manager here.
import sys, os
sys.path.insert(1, os.path.join(os.getcwd(), 'part2'))
from db.manager import *

def showhelp():
    print('usage: python main.py <options>')
    print('===== options =====')
    print('-h or --help to print this menu.')
    print('-l or --list to list all tasks.')
    print('-a or --add <DESCRIPTION> to add a new task')
    print('-p or --priority <NUMBER> to assign a priority to a new task. Must use with -a or -s.')
    print('-r or --remove <ID> remove a task.')
    print('-c or --complete <ID> mark a task as complete.')
    print('-cp or --changepriority <ID> <NUMBER> change an existing task\'s priority.')
    print('-u or --update <ID> <DESCRIPTION> update an existing task\'s description.')
    print('-s or --search <OPTIONS> search a task by options.')
    print('-t or --sort show sorted list of tasks by increasing order of priority.')
    print('-d or --desc decreasing order of priority. Must use with -t.')
    print('-i or --id <ID> task ID. Must use with -s for search task with ID.')
    print('-dp or --description <TEXT> task description. Must use with -s for search task with description.')


# command to list all tasks
def list_all_tasks_cmd():
    if(not is_tasks_file_exists()): return ("TODO List empty. Add some tasks.")
    else:
        accum = ""
        tasks = get_all_tasks()
        for task in tasks:
            parts = task.split(",")
            accum += "ID: {id} DESC: {desc} PRIORITY: {priority} STATUS: {status}".format(id = parts[0], desc = parts[1], priority = parts[2], status = parts[3])
    return accum

# command to list all tasks but in string form
def string_list_tasks_cmd():
    accum = ""
    tasks = get_all_tasks()
    for task in tasks:
        accum += task
    return accum

# command to add a task
def add_task_cmd(task, priority):
    if(task == "" or priority <= 0): return ("Failed to add task")
    else:
        id = add_task(task, priority)
        return("Task added and assigned ID {id}".format(id = id))

# command to delete a task
def remove_task_cmd(id):
    removed = remove_task(id)
    if(removed):
        return ("Removed task ID {id}".format(id = id))
    else:
        return ("Failed to remove task ID {id}".format(id = id))

# command to complete a task
def complete_task_cmd(id):
    #return boolean
    completed = complete_task(id)
    if(completed):
        return ("Task {id} completed".format(id = id))
    else:
        return ("Task {id} could not be completed".format(id = id))

# command to edit task priority
def change_priority_cmd(id, priority):
    #return boolean
    changed = change_priority(id, priority)
    if(changed):
        return ("Changed priority of task {id} to {priority}".format(id = id, priority = priority))
    else:
        return ("Priority of task {id} could not be changed".format(id = id))

# command to edit task description
def update_cmd(id, desc):
    #return boolean
    updated = update_desc(id, desc)
    if(updated):
        return ("Task {id} updated".format(id = id))
    else:
        return ("Failed to update task {id}".format(id = id))

# command to search a task by id, description, or priority
def search_cmd(id, desc, priority):
    if(id == None and desc == None and priority == None):
        tasks = "".join(get_all_tasks())
        return tasks
    search_results = search(id, desc, priority)
    if(search_results != ""):
        return search_results
    else:
        return ("Task not found")

# command to sort the tasks in specified order
def sort_cmd(order):
    if(order == "-d" or order == "--desc"):
        return sort(-1)
    return sort()
