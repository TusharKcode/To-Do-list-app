tasks=[]

def add_task():
    task=input("Enter a Task: ")
    tasks.append(task)
    print(f"Task",{task},"added.")

def remove_task():
    task_index=int(input("Enter the index of the task to remove: "))
    if 0<=task_index<len(tasks):
        removed_task=tasks.pop(task_index)
        print(f"Task",{removed_task},"removed.")
    else:
        print("Invalid index.")

def view_task():
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks):
            print(f"{index+1}.{tasks}")

while True:
    print("To-Do list app")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Task")
    print("4. Exit")

    choice=input("Enter your choice: ")

    if choice=='1':
        add_task()
    elif choice=='2':
        remove_task()
    elif choice=='3':
        view_task()
    elif choice=='4':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")



