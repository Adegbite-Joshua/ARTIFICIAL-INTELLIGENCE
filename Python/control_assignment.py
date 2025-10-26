starting_num = int(input("Enter num 1"))
ending_num = int(input("Enter num 2"))
    
for first_num in range(starting_num, ending_num):
    print(f"Multiplication Table {first_num}")
    for second_num in range(1, 13):
        print(f"{first_num} * {second_num} = {first_num * second_num}")
    
    print()
    