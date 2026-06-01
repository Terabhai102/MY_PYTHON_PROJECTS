def calculate_average():
    total_sum = 0
    count = 0
    
    with open("Average.txt", "r") as file:
        for line in file:
            parts = line.split(",")
            value = float(parts[1].strip())
            
            total_sum += value
            count += 1
    
    if count > 0:
        print(f"Average: {total_sum / count}")
    else:
        print("No data to process.")

calculate_average()
