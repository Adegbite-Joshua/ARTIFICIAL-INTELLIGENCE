print("Odd and Even Algorithm".center(100, "*"))
number = int(input("Enter a number: "))
if number % 2 == 0:
  print(f"The number {number} is even")
else:
  print(f"The number {number} is odd")
  
  
  
print("Alcronym Generator Algorithm".center(100, "*"))
name = input("Enter your name: ")
name = name.split(" ")
name_length = len(name)
if name_length == 1:
  print(f"Acronym: {name[0][0].upper()}")
elif name_length == 2:
  print(f"Acronym: {name[0][0].upper()}{name[1][0].upper()}")
elif name_length == 3:
  print(f"Acronym: {name[0][0].upper()}{name[1][0].upper()}{name[2][0].upper()}")
elif name_length == 4:
  print(f"Acronym: {name[0][0].upper()}{name[1][0].upper()}{name[2][0].upper()}{name[3][0].upper()}")
elif name_length == 5:
  print(f"Acronym: {name[0][0].upper()}{name[1][0].upper()}{name[2][0].upper()}{name[3][0].upper()}{name[4][0].upper()}")
elif name_length == 6:
  print(f"Acronym: {name[0][0].upper()}{name[1][0].upper()}{name[2][0].upper()}{name[3][0].upper()}{name[4][0].upper()}{name[5][0].upper()}")
else:
  print("Words too long")
  
  
  
print("Love Calculator Algorithm".center(100, "*"))
boyfriend_name = input("Enter boyfriend name: ")
girlfriend_name = input("Enter girlfriend name: ")
count = 0
char_map = {
    "a": 12,
    "b": 15,
    "c": 3,
    "d": 15,
    "e": 7,
    "f": 15,
    "g": 2,
    "h": 15,
    "i": 8,
    "j": 15,
    "k": 5,
    "l": 15,
    "m": 12,
    "n": 15,
    "o": 10,
    "p": 15,
    "q": 15,
    "r": 5,
    "s": 15,
    "t": 7,
    "u": 11,
    "v": 13,
    "x": 15,
    "y": 9,
    "z": 5,
}

count += (char_map[boyfriend_name[0].lower()] + char_map[girlfriend_name[0].lower()] + char_map[boyfriend_name[-1].lower()] + char_map[girlfriend_name[-1].lower()])
print(f"The love between {boyfriend_name.title()} and {girlfriend_name.title()} is {count}%")


