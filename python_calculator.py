
def calculator():
    print("--- Python Calculator ---")
    
    while True:
        print("\n1. Add | 2. Subtract | 3. Divide | 4. Multiply | 5. QUIT")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 5:
            print("Goodbye!")
            break

        # ADDITION
        if choice == 1:
            total = 0
            print("Keep entering numbers to add. Type anything else (like 'done') to finish.")
            while True:
                try:
                    num = float(input("Enter number: "))
                    total += num
                    print(f"Current Sum: {total}")
                except ValueError:
                    break
            print(f"Final Sum: {total}")

        # SUBTRACTION
        elif choice == 2:
            try:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter number to subtract: "))
                print(f"Result: {n1 - n2}")
            except ValueError:
                print("Invalid input!")

        # DIVISION
        elif choice == 3:
            try:
                n1 = float(input("Enter numerator: "))
                n2 = float(input("Enter denominator: "))
                if n2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    print(f"Result: {n1 / n2}")
            except ValueError:
                print("Invalid input!")

        # MULTIPLICATION
        elif choice == 4:
            total = 1.0 # Initialized to 1 so multiplication works correctly
            print("Keep entering numbers to multiply. Type anything else to finish.")
            while True:
                try:
                    num = float(input("Enter number: "))
                    total *= num
                    print(f"Current Product: {total}")
                except ValueError:
                    break
            print(f"Final Product: {total}")

        else:
            print("Invalid selection! Please try again.")

# Run the program
calculator()
