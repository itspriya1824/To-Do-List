tasks = []
while True:
    print("\nAdd Task")
    print("View Task")
    print("Delete Task")
    print("Exit")
    Choice = input("Enter Choice(1-5):")
    if Choice == "1":
        task = input("Enter task:")
        tasks.append(task)
        print("Task added successfully")
    elif Choice == "2":
        if len(tasks) == 0:
            print("No task available")
        else:
            print("\nYour Task")   
            i = 0
            while i < len(tasks) :
                print(i + 1,".",tasks[i])
                i += 1
    elif Choice == "3":
        if len(tasks) == 0:
            print("no tasks to delete")
        else:
            print("\nYour tasks:")
            i = 0 
            while i < len(tasks):
                print(i + 1,".",tasks[i])  
                i += 1
            num = int(input("Enter task number to delete:"))
            if num >=1 and num <= len(tasks):
                tasks.pop(num - 1)
                print("task deleted successfully")
    elif Choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")                          

   