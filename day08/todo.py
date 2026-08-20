tasks = []

while True:
    print("\n---TO-DO LIST---")
    print("1. Add task")
    print("2. Mark task complete")
    print("3. Remove task")
    print("4. View all task")
    print("5. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"task": task, "Completed": False})
        print("Task added")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nTasks:")

            for i, item in enumerate(tasks):
                status = "good" if item ["Completed"] else ""
                print(f"{i + 1}. [{status}] {item['task']}")
                number = int(input("Enter the task number to mark complete: "))
                if 1 <= number <= len(tasks):
                    tasks[number - 1] ["completed"] = True
                    print("Task marked as complete")
                else:
                    print("Invalid task number.")

    elif choice == "3":
       if len(tasks) == 0:
         print("No tasks available.")
       else:
          print("\nTasks:")
          for i, item in enumerate(tasks):
              status = "good" if item["completed"] else ""
              print(f"{i + 1}, [{status}] {item['task']}")
          number = int(input("Enter the number to remove: "))
          if 1<= number <= len(tasks):
              tasks.pop(number - 1)
              print("Task removed")
          else:
              print("Invalid task number")
            
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n--- YOUR TASKS ---")
            for i, item in enumerate(tasks):
                status ="good" if item ["completed"] else ""
                print(f"{i + 1}, [{status}] {item['task']}")
    elif choice == "5":
        print("Goodbye")
        break
    else:
       print("Invalid choice. Try again.")

