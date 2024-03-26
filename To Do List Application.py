#Mini-Project

print("\nWelcome to the To-Do List App!\n\n")
print("Menu:")
print("1. Add a task")
print("2. View Tasks")
print("3. Mark a task as complete")
print("4. Delete a task")
print("5. Quit\n")

task_dict = {} #Dictionary is empty until the user adds to it
list_of_options = ['1', '2', '3', '4', '5'] # List of options that we want the user to input

'''#This function takes the name that the user will input to create a task in a dictionary of tasks 
    that will have the default 'Incomplete' until the user changes it'''
def add_task(name, status= 'Incomplete'): 
    global task_dict
    if name not in task_dict: #Checking that the task hasnt already been added
        task_dict[name]= []
        print(f'Task: {name} has been added.')
        task_dict[name]=status
    else:
        print(f"Task: {name} already exists.") #Telling the user they already have a task named that way.
        
'''function used to view the current task inputs'''
def view_tasks(task_dict):
    if not task_dict: #Checking if the dictionary is currently empty
        print("To Do List is empty")
    for task, status in task_dict.items(): #Outputs the dictionary line by line for a friendlier view
        print(f"{task}: {''.join(status)}")

'''This function is being used to change the default status of 'incomplete' to complete as the user wants'''
def status_update(task_dict, task, status): 
    task_dict[task]=status
    print(f"Status of task, {task} has been changed to: {status}")    


'''This function is deleting the task that the user wants to be deleted'''
def delete_task(list, task):
    task_dict.pop(task)
    print(f"Task {task} has been removed from the To-Do List")


while True:
    '''Using try and excepts all throughout this block to make sure the inputs by the user are valid and can be used in the code.'''
    try:
        user_input = input("Please select a menu option from the list. ")
        if user_input == '5':
            print("Exiting To-Do List...")
            break
        elif user_input not in list_of_options:
            raise ValueError
    except ValueError:
        print("Entry is invalid. Please enter a menu option.(1-5) ")

    if user_input == '1':
        try:
            task_name = input("What is the name of the task being added? ").upper()
            add_task(task_name, 'Incomplete')
        except:
            print("Invalid task name.")
    elif user_input == '2':
        view_tasks(task_dict)
    elif user_input == '3':
        try:
            user_task = input("Which task from the list do you want to mark complete? ").upper()
            if user_task not in task_dict:
                raise ValueError
        except ValueError:
            print(f"Task: {user_task} doesn't exist. Please select a valid task.")    
        
        else:
            status_update(task_dict, user_task, 'Complete')
    elif user_input == '4':
        try:
            user_task = input("Which task from the list do you want to delete? ").upper()
            if user_task not in task_dict:
                raise ValueError
        except ValueError:
            print(f"Task: {user_task} doesn't exist. Please select a valid task.")    
        
        else:
            delete_task(task_dict, user_task)
        
            

