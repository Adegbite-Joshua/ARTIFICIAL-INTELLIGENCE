# String 

short_story = "Short story here"
print(type(short_story))
print(len(short_story))

# Slice
print(short_story[0:10])
print(short_story[5:10])

# Methods of string
print(short_story.lower())
print(short_story.capitalize())
print(short_story.split())
print(short_story.center(100, "*"))
# print(short_story.strip())

# Type Conversion
num1 = "12"
num2 = 6
# print(int(num1) + num2)



# Data Types
"""
list
tuple
set
number
dictionary
boolean
"""


list_of_names = ["Baith", "Joshua"]
set_itm = {"orange", "grape", "melon"}
# dict_itm = 

boolean_itm = False

# print(int(boolean_itm))
# print(type(int(boolean_itm)))


# Concatenation
first_name = "John"
last_name = "Doe"

print("Hello", first_name, last_name)
print("Hello " + first_name + " " + last_name)
print(f"Hello {first_name} {last_name}")


# Operators
num1 = 9
num2 = 5
print(num1 + num2)
print(num1 - num2)  
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)  # Floor division
print(num1 % num2)   # Modulus(Remainder)


# Logical Operators
condition1 = True

print(not condition1)

list_item = ["mango", "banana", "orange"]
if "mango" in list_item:
    print("Yes, mango is in the list")
else:
    print("No, mango is not in the list")



# Conditional Statements
if 5 > 3:
    print("5 is greater than 3")