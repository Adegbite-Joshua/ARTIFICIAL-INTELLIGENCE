try:
    text = "Hello"
    print(int(text))
except ValueError:
    print("ValueError: Cannot convert string to integer.")


try:
    val1 = int(input("Enter first number: "))
    val2 = int(input("Enter second number: "))

except ValueError:
    print("Can not convert letter to int")
except ZeroDivisionError:
    print("Value cannot be divisible by zero")
finally:
    print("The execution is successful")