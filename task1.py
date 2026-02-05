task=[]
while True:
    print("\n To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark task as completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice=="1":
        task_name= input("Enter your task: ")
        task.append([task_name,"Pending"])
        print("Task Added")
    
    elif choice == "2":
        if len(task)==0:
            print("No Taks Found")
        else:
            print("Your Tasks are: ")
            for i in range(len(task)):
                print(i+1,".",task[i][0],"-",task[i][1])
    elif choice == "3":
        num=int(input("Enter task number to mark as completed: "))
        if num > 0 and num <= len(task):
            task[num-1][1]="Completed"
            print("Task marked as completed")
        else:
            print("Invalid task number")

    elif choice =="4":
        num=int(input("Enter the task number to delete: "))
        if num > 0 and num <= len(task):
            task.pop(num-1)
            print("Task deleted")
        else:
            print("Invalid task number")
    elif choice=="5":
        print("Exiting To-Do List")
        break
    else:
        print("Please entera valid choice")