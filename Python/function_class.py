import os
# Function
def landing_page():
    """Return the home page of todo algorithm to the user"""
    print("""
        1. Create todo
        2. Update todo
        3. Delete todo
        4. Exit
        """)


def multiplication_table():
    """
    Print Multiplication table from 1 to 12
    """
    for first_num in range(1, 13):
        print(f"Multiplication Table {first_num}")
        for second_num in range(1, 13):
            print(f"{first_num} * {second_num} = {first_num * second_num}")
    
    
    os.system("cls")
    print("Cleared")
multiplication_table()


