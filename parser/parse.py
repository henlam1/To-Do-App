# import utils.commands here
import sys, os
sys.path.insert(1, os.path.join(os.getcwd(), 'part2'))
from utils.commands import *

# parse the command line arguments and execute the appropriate commands.
def parseArgs(args):
    argc = len(args)
    if(argc == 1): 
        return("Missing Required argument. Type -h to seek help")
    cmd = args[1]
    if(cmd in ["-h", "--help"]):
        showhelp()
    elif(cmd in ["-l", "--list"]):
        return string_list_tasks_cmd()
    elif(cmd in ["-a", "--add"]):
        if(argc == 2): return ("Missing description. Type -h to seek help")
        if(argc == 3): return ("Error: Cannot add a task with empty priority")
        if(argc > 3): 
            desc = args[2]
            pflag = args[3]
            if(not isinstance(desc, str)): return ("Description must be a string")
            if(not isinstance(pflag, str) or not pflag in ["-p", "--priority"]): return ("Error: Incorrect priority option")  
        if(argc == 4): return ("Error: Cannot add a task with empty priority")
        if(argc == 5): 
            priority = args[4]
            if(not isinstance(priority, int)): return("Priority must be integer")
            return add_task_cmd(desc, priority)
        if(argc > 5): return ("Error: Found extraneous options")
    elif(cmd in ["-r", "--remove"]):
        if(argc == 2): return ("Task ID missing")
        if(argc == 3): 
            id = args[2]
            if(not isinstance(id, int)): return("Task ID must be a number")
            id = int(id)
        if(argc > 3):
            return ("Error: Found extraneous options")
        return remove_task_cmd(id)
    elif(cmd in ["-c", "--complete"]):
        if(argc == 2): return ("Task ID missing")
        if(argc == 3): 
            id = args[2]
            if(not isinstance(id, int)): return("Task ID must be a number")
            id = int(id)
        if(argc > 3):
            return ("Error: Found extraneous options")
        return complete_task_cmd(id)
    elif(cmd in ["-cp", "--changepriority"]):
        if(argc > 4): return ("Error: Found extraneous options")
        if(argc == 2): return ("Task ID or priority missing")
        if(argc >= 3): 
            tnum = args[2]
            if(not isinstance(tnum, int)): return ("Task ID must be a number")
        if(argc == 4):
            pnum = args[3]
            if(not isinstance(pnum, int)): return ("Priority must be a number")
            return change_priority_cmd(tnum, pnum)
    elif(cmd in ["-u","--update"]):
        if(argc < 4): return ("Task ID or description missing")
        if(argc == 4):
            tnum = args[2]
            desc = args[3]
            if(not isinstance(tnum, int)): return ("Task ID must be a number")
            if(not isinstance(desc, str)): return ("Description must be a string")
            return update_cmd(tnum, desc)
        if(argc > 4): return ("Error: Found extraneous options")
    elif(cmd in ["-s","--search"]):
        #stop when out of flags, all conditions are found, invalid flag, or if a flag is repeated
        flaglist = [["-i", "--id"],["-dp", "--description"],["-p", "--priority"]]
        values = [None, None, None]
        if(argc == 2): return ("Search Criteria Missing")
        if(argc < 4): return ("Error: At least one search criteria must be present")
        if(argc >= 4):
            stop = 8 if argc > 8 else argc
            # loops until args end or 3 times max
            for i in range(2, stop, 2):
                # check if flag is valid
                if(any(args[i] in tasks for tasks in flaglist)):
                    value = args[i+1]
                    # sets value of id
                    if(args[i] in flaglist[0]):
                        if(values[0] == None):
                            if(not isinstance(value, int)):
                                return("search ID and priority must be integer.")
                            values[0] = value
                        else: return search_cmd(values[0], values[1], values[2])
                    # sets value of descr
                    elif(args[i] in flaglist[1]):
                        if(values[1] == None):
                            values[1] = value
                        else: return search_cmd(values[0], values[1], values[2])
                    # sets value of priority
                    elif(args[i] in flaglist[2]):
                        if(values[2] == None):
                            if(not isinstance(value, int)):
                                return("search ID and priority must be integer.")
                            values[2] = value
                        else: return search_cmd(values[0], values[1], values[2])
                else: 
                    break
            return search_cmd(values[0], values[1], values[2])  
    elif(cmd in ["-t","--sort"]):
        if(argc == 2): return sort_cmd("")
        if(argc == 3):
            if(args[2] in ["-d", "--desc"]):
                return sort_cmd(args[2])
        if(argc > 3): return ("Error: Found extraneous options")
        return sort_cmd("")
    else:
        print("'Invalid argument. Type -h to seek help'")

# task controls

# -h ignore
# -l ignore
# -a string description +int prionum
# -r +int tasknum
# -c +int tasknum
# -cp +int tasknum +int prionum
# -u +int string description
# -s +int id/string description/+int priority
# -t -d/none