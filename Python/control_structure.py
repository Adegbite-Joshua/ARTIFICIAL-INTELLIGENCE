# Control Structure

# Conditional statement
# 1. If 
# 2. If else
# 3. Nested condition

# Loop
# 1. For loop
# 2. While loop
# 3. Break and continue

 
# if 5 > 2:
#     print(" Creater ")
# else:
#     print(" Lesser")



# if 5 > 2:
#     print(" Creater ")
# elif 5 == 5:
#     print(" Equal ")
# else:
#     print(" Lesser")



# if 5 > 2:
#     print(" Creater ")
# if 5 == 5:
#     print(" Equal ")
# else:
#     print(" Lesser")
    



if 5 > 12:
    print(" Creater ")  
    if 5 > 2:
        print(" Inner Creater ")
    else:
        print(" Inner Lesser")
elif 5 == 5:
    if 5 > 2:
        print(" Second Creater ")
    else:
        print(" Second Lesser")
else:
    print(" Lesser")
    
    
"""
Python loop
for, while
"""

count = 0
list_of_names = "Tolu", "Kunle", "Bola", "Malik"
for name in list_of_names:
    count += 1
    print(f"{count}- {name}")
    
for num in range(1, 10):
    print("Number", num)


for first_num in range(1, 13):
    print(f"Multiplication Table {first_num}")
    for second_num in range(1, 13):
        print(f"{first_num} * {second_num} = {first_num * second_num}")
    
    print()
    



count = 0
while 5 > count:
    print("Hello")
    count += 1
    
    
starting_num = int(input("Enter num 1"))
ending_num = int(input("Enter num 2"))
    
for first_num in range(1, starting_num):
    print(f"Multiplication Table {first_num}")
    for second_num in range(1, ending_num):
        print(f"{first_num} * {second_num} = {first_num * second_num}")
    
    print()
    

passwd = "12wer"
usernm = "abdulB"
while True:
    count = 3
    pwd = input("Enter your name: ")
    username = input("Enter your name: ")
    if passwd != pwd or usernm != username:
      count -= 1
      if count == 0:
        print("You have exceeded your login attempt, try again after one year")
        break
    else:
      print("Welcome to SQI")
      break
    