

def contact_book():
    contact = {}
    while True:
        print("\n1. TO ADD PH NO.")
        print("2. TO REMOVE PH NO.")
        print("3. TO SHOW ALL PH NO.")
        print("4. QUIT")
        choice = input("Choice please: ")

        if choice == "1":
            name = input("Write the name: ")
            ph = input("Write the number: ")
            contact[name] = ph
            print("Contact added!")
        
        elif choice == "2":
            remove = input("Write the name to remove: ")
            if remove in contact:
                del contact[remove]
                print(f"{remove} removed.")
            else:
                print("Contact not found.")
        
        elif choice == "3":
            print("\n--- CONTACT LIST ---")
            for name, ph in contact.items():
                print(f"{name}: {ph}")
                
        elif choice == "4":
            print("Bye!")
            break
            
        else:
            print("Invalid choice!")

contact_book()
