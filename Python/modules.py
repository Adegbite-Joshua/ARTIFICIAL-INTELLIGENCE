import datetime
# print(dir(datetime))


date = datetime.datetime.today()
# print(date)
# print(date.microsecond)
# print(date.year)
# print(date.weekday())

# print(date.strftime("%c"))
# print(date.strftime("%B %d, %Y"))
# print(date.strftime("%I:%M %p"))


# import time
# st = time.time()
# time.sleep(5)
# print("5 seconds later")
# sto = time.time()
# print("Time taken to execute the code is", sto - st, "seconds")
# print(time.time())


import random
import string as st

# print(random.random())
print(random.randint(1000, 9999))
# print(st.ascii_letters)
# print(st.octdigits)

# Creating a new password
# input = int(input("Enter the length of password: "))
# all_char = st.ascii_letters + st.digits + st.punctuation
# password = "".join(random.sample(all_char, input))
# print("Your new password is:", password)


import math
# print(len(dir(math)))
a = 100
b=15
# print(math.sqrt(a))
# print(math.ceil(a/b))
# print(math.pow(b, a))

import custom_module
print(dir(custom_module))
custom_module.greet("Alice")

import colorama as cm

print(dir(cm))
