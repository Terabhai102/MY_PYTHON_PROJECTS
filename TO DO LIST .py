def to_do_list():
    tasks = []
    while True:
        print("\n--- MENU ---")
        print("1. ADD TASK")
        print("2. REMOVE TASK")
        print("3. SHOW ALL TASKS")
        print("4. QUIT")
        
        choice = input("Enter your choice: ")
        
        # Everything below this line must be indented
        if choice == "1":
            task = input("ENTER THE TASK: ")
            tasks.append(task)
        elif choice == "2":
            task = input("ENTER THE TASK TO REMOVE: ")
            if task in tasks:
                tasks.remove(task)
            else:
                print("TASK NOT FOUND") 
        elif choice == "3":
            print("\nTASKS:")
            for task in tasks:
                print("- " + task)
        elif choice == "4":
            print("Goodbye!")
            break  # Now this is correctly inside the loop
        else:
            print("INVALID!!")   

to_do_list()

