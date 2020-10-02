# Function with positional parameter

def gretting(first_name, last_name):
    print(f"Hi {first_name} {last_name}, welcome.")


gretting("ankan", "leo")
gretting("tousif", "rahman")

# Two types of function : function that returns a value or function that perform a task

# *args: variable number of non-keyword arguments, returns tuples


def multiply(*numbers):
    product = 1
    for number in numbers:
        product *= number
    return product


print(multiply(2, 3, 4, 5, 6))

# **args: variable number of keyword arguments, returns dictionary


def save_user(**user):
    print(user["password"])


save_user(id="ankanleo", password=12345)

# Fizz-Buzz game: when given number is divisible by 3 output 'fizz', if the number is divisible by 5 then print 'buzz'
# if the number is divisible by both 3 and 5 then print 'fizz-buzz', otherwise print the number


def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "fizz-buzz"
    if number % 3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "buzz"
    return number


print(fizz_buzz(7))
