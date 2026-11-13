tasks=[]
print("=====TO-DO LIST APPLICATION=====")
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({
            "name":task,
            "completed":False
        })
        print("Task added successfully!")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                if task["completed"]:
                    status="completed"
                else:
                    status="pending"
                print(i, ".", task["name"],"-",status)
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task["name"])

            num = int(input("Enter task number to complete: "))

            if 1 <= num <= len(tasks):
                tasks[num - 1]["completed"]=True
                print("test marked as completed!")
            else:
                print("Invalid task number!")
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task["name"])

            num = int(input("Enter task number to delete: "))

            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print("Deleted task:", removed["name"])
            else:
                print("Invalid task number!")

    elif choice == "5":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice!")