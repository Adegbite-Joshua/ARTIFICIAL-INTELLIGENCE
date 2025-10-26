# import colorama
# from colorama import Fore, Back, Style
# colorama.init(autoreset=True)

# print(f"{Back.YELLOW}{Fore.RED}" + "Colorama".center(50, "*"))
# print(f"{Back.YELLOW}{Fore.RED}{Style.BRIGHT}" + "Colorama".center(50, "*"))


# from py_mini_racer import MiniRacer
# ctx = MiniRacer()

# print(dir(ctx))
# js_code = """
# function factorial(n) {
#     if (n === 0) return 1;
#     return n * factorial(n - 1);
# }
# factorial(5)
# """
# result = ctx.execute(js_code)
# print("Factorial of 5 is:", result)

from py_mini_racer import MiniRacer

ctx = MiniRacer()

js_coode = """
    (function() {
        function factorial(n) {
            if (n === 0) return 1;
            return n * factorial(n - 1);
        }
        return factorial(5);
    })()
"""

result3 = ctx.execute(js_coode)
print("Wrapped factorial:", result3)