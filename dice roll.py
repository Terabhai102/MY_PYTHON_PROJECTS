import random

def rolling_dice():
    while True:
        print("\n1. To roll dice")
        print("2. Exit")
        # Keep choice as a string to match the conditions easily
        choice = input("What's your choice? ")
        
        if choice == '1':
            # randint(1, 6) gives a number between 1 and 6 inclusive
            print(f"You rolled a: {random.randint(1, 6)}")
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Call the function
rolling_dice()
