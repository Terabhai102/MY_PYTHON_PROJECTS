#PASSWORD MANAGER
import random
import string

def password_gen():
    while True:
        print("\n1. Add a password")
        print("2. Show all passwords")
        print("3. Generate password")
        print("4. EXIT")
        choice = input("Your choice: ")

        if choice == "1":
            site = input("Write the website: ")
            password = input("Password: ")
            with open("password.txt", 'a') as f:
                f.write(f"{site}:{password}\n")
            print("Saved!")

        elif choice == '2':
            try:
                with open("password.txt", 'r') as f:
                    print("\n--- Saved Passwords ---")
                    print(f.read())
            except FileNotFoundError:
                print("No passwords saved yet.")

        elif choice == '3':
            # Simple generator logic
            chars = string.ascii_letters + string.digits
            special = input("Any special character to add? ")
            password = ''.join(random.choice(chars) for _ in range(8)) + special
            print(f"Generated password: {password}")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

password_gen()

    
      
    