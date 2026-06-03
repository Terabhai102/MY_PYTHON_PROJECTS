import time
import pandas as pd
from datetime import datetime
import os

def initialize_data():
    if not os.path.exists("study_record.csv"):
        df = pd.DataFrame(columns=["Date", "Hours", "Topics"])
        df.to_csv("study_record.csv", index=False)

def smart_class():
    initialize_data()
    user_goal = 6.0 
    
    while True:
        print(f"\n--- SMART STUDY SYSTEM (Goal: {user_goal} hrs/day) ---")
        print("1. Set Reminder\n2. Add Study Log\n3. Show All Topics\n4. Weekly Report\n5. View Last Entry\n6. Change Goal\n7. QUIT")
        
        try:
            choice = int(input("Whats your move: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            hour = int(input("Hour (24h format): "))
            minute = int(input("Minutes: "))
            print(f"Reminder set for {hour}:{minute}")
            while True:
                now = datetime.now()
                if now.hour == hour and now.minute == minute:
                    print("\n!!! TIME TO STUDY! Keep up the progress! !!!")
                    break
                time.sleep(20)

        elif choice == 2:
            hours = float(input("How many hours studied: "))
            topics = input("Topics covered (comma separated): ")
            date = datetime.now().strftime("%Y-%m-%d")
            
            new_data = pd.DataFrame([[date, hours, topics]], columns=["Date", "Hours", "Topics"])
            new_data.to_csv("study_record.csv", mode='a', index=False, header=False)
            print("Record saved successfully!")

        elif choice == 3:
            df = pd.read_csv("study_record.csv")
            print("\n--- Topics Covered ---")
            print(df['Topics'].unique())

        elif choice == 4:
            df = pd.read_csv("study_record.csv")
            if len(df) == 0:
                print("No data available.")
            else:
                avg = df['Hours'].tail(7).mean()
                print(f"\nWeekly Average: {avg:.2f} hours/day")
                if avg >= user_goal: print(f"Excellent! You are hitting your {user_goal}-hour goal.")
                else: print(f"Keep pushing! You are below your {user_goal}-hour goal.")

        elif choice == 5:
            df = pd.read_csv("study_record.csv")
            if len(df) > 0:
                last = df.iloc[-1]
                print(f"\nLast session: {last['Date']} | {last['Hours']} hours")
            else:
                print("No records found.")
                
        elif choice == 6:
            user_goal = float(input(f"Enter new daily study goal (currently {user_goal}): "))
            print(f"Goal updated to {user_goal} hours/day!")

        elif choice == 7:
            print("System closing. Keep studying!")
            break

if __name__ == "__main__":
    smart_class()
    