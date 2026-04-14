"""
Create a TODO app.
It should display a list of tasks.
It should provide the ability to add tasks to the list.
It should provide the ability to delete tasks from the list.
You should be able to quit.
"""

# Initial Screen
"""
====================
A. Add Task
D. Delete Task
Q. Quit
====================
TODO LIST
----------------------------------------
----------------------------------------
>
"""

# Add Task Screen
"""
====================
A. Add Task
D. Delete Task
Q. Quit
====================
TODO LIST
----------------------------------------
0 | take out the trash
----------------------------------------
> A
Please enter the task details
> do homework
"""

# Delete Task Screen
"""
====================
A. Add Task
D. Delete Task
Q. Quit
====================
TODO LIST
----------------------------------------
0 | take out the trash
1 | do homework
2 | clean room
----------------------------------------
> d
Please enter the task id to delete
> 1
"""

# If an invalid option is entered display the following
"""
> blah blah blah
'blah blah blah' is not a valid option
press any key to continue ...
"""

#################################
# YOUR CODE HERE
tasks = []

def show_menu():
    print("====================")
    print("A. Add Task")
    print("D. Delete Task")
    print("Q. Quit")
    print("====================")
    print("TODO LIST")
    print("----------------------------------------")
    for i, task in enumerate(tasks,start=1): # stuck here
        print(f"{i} | {task}")
    print("----------------------------------------")

def display_menu():
    print("====================")
    print("A. Add Task")
    print("D. Delete Task")
    print("Q. Quit")
    print("====================")

def to_do_list():
    print("TODO LIST")
    print("----------------------------------------")
    for i, task in enumerate(tasks,start=1): # stuck here
        print(f"{i} | {task}")
    print("----------------------------------------")

def is_valid_indx(tsk_id):
    if tsk_id.isdigit() == False:
        return False
    tsk_id = int(tsk_id)
    if tsk_id < 1:
        return False
    if tsk_id > len(tasks):
        return False
    else:
        return True

def delete_task(task_id):
    if is_valid_indx(task_id) == False:
        inv_input(task_id)
    else:
        tasks.pop(int(task_id) - 1)

def inv_input(value):
    print(f"'{value}' is not a valid option")
    input("press any key to continue ...")

def user_input():
    choice = input("> ").lower()
    if choice == "a":
        task = input("Please enter the task details\n> ")
        tasks.append(task)
    elif choice == "d":
        task_id = input("Enter the task id to delete\n>")
        delete_task(task_id)
    elif choice == "q":
        print("Goodbye!!!")
        exit()
    else:
        inv_input(choice)

while True:
    display_menu()
    to_do_list()
    user_input()

# while True:
    # 1. display_menu
    # 2. display the to do list
    # 3. Process input
    # show_menu()
    # choice = input("> ").lower()

    # if choice == "a":
    #     task = input("Please enter the task details\n> ")
    #     tasks.append(task)

    # elif choice == "d":
    #     task_id = input("Please enter the task id to delete\n> ")
    #     if task_id.isdigit() == False :
    #         print("Invalid task id")
    #         input("Press any key to continue ...")
    #     else:
    #         tasks.pop(int(task_id) - 1)

    #     # try:
    #     #     task_id = int(input("Please enter the task id to delete\n> "))
    #     #     tasks.pop(task_id - 1)
    #     # except:
    #     #     print("Invalid task id")
    #     #     input("press any key to continue ...")

    # elif choice == "q":
    #     print("Goodbye!")
    #     break

    # else:
    #     print(f"'{choice}' is not a valid option")
    #     input("press any key to continue ...")
#################################