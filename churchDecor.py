tasks = [
    "Clean the pews",
    "Dust the altar",
    "Sweep the floor",
    "Decorate the altar with flowers",
    "Clean the windows",
    "Set up chairs for service",
    "Organize church supplies"
]

task_assignments = {task: [] for task in tasks}

def show_tasks():
    print("\nList of Tasks that Need to be Done:")
    for i, task in enumerate(tasks, 1):
        assigned_volunteers = task_assignments[task]
        if assigned_volunteers:
            print(f"{i}. {task} - Assigned to: {', '.join(assigned_volunteers)}")
        else:
            print(f"{i}. {task} - No volunteers assigned yet.")

def sign_up_for_task():
    show_tasks() 
    task_choice = int(input("\nEnter the number of the task you want to sign up for: "))
    
    if 1 <= task_choice <= len(tasks):
        task = tasks[task_choice - 1]
        volunteer_name = input(f"Enter your name to sign up for the task: '{task}': ")
        
        if volunteer_name in task_assignments[task]:
            print(f"{volunteer_name}, you've already signed up for this task.")
        else:
            task_assignments[task].append(volunteer_name)
            print(f"Thanks, {volunteer_name}! You are now signed up for '{task}'. ")
    else:
        print("Invalid task number! Please try again.")

def mark_task_as_completed():
    show_tasks()  
    task_choice = int(input("\nEnter the number of the task you want to mark as completed: "))
    
    if 1 <= task_choice <= len(tasks):  
        task = tasks[task_choice - 1]
        
        if task_assignments[task]:
            print(f"Task '{task}' completed by: {', '.join(task_assignments[task])} ")
            task_assignments[task] = []  
        else:
            print(f"No one has signed up for '{task}' yet. You need volunteers for this task.")
    else:
        print("Invalid task number! Please try again.")

while True:
    print("\nWhat would you like to do?")
    print("1. View tasks and volunteers")
    print("2. Sign up for a task")
    print("3. Mark a task as completed")
    print("4. Exit")

    action = input("Enter the number of your choice: ")

    if action == "1":
        show_tasks()  

    elif action == "2":
        sign_up_for_task()  

    elif action == "3":
        mark_task_as_completed()  

    elif action == "4":
        print("Thanks for using the Church Cleaning & Decoration Manager! ")
        break  

    else:
        print("Invalid choice! Please choose a valid option (1, 2, 3, or 4).")