# Set in Python

# sets = set()
# print(type(sets))

setA = {1, 2, 3, 4, 5}
setB = {12, 23, 36, 4, 5}
# print(setA.union(setB))
setA.add(8)
set1 = setA.union(setB)




# Dictionary in Python
# A dictionary is a built-in data type that is unordered, changeable, and indexed. No duplicate members.
# Dictionaries are written with curly brackets, and they have keys and values.
person = {
    "first_name": "Baith",
    "last_name": "Joshua",
    "age": 23,
    "is_married": False,
    "skills": ["HTML", "CSS", "JavaScript", "Python"],
    "address": {
        "street": "Lekki",
        "city": "Lagos",
        "country": "Nigeria"
    },
    "phone_numbers": ("08012345678", "09098765432")
}

person.update({"first_name": ["Reading", "Traveling"]})

print(person)

accepted_details = {}
dict_key = input("Enter the dictionary key: ")
dict_value = input("Enter the dictionary value: ")
accepted_details[dict_key] = dict_value

print(accepted_details)

