"""
Notes:

Besides the 'vanilla' method of defining a python function, there are some additional features of functions that you may see.

-------------------------------------------------------------------------------

1. Default/Keyword Arguments:
- Default arguments allow you to define default values for parameters in the function definition. 
  If no argument is provided for that parameter, the default value is used.
- Keyword arguments allow you to specify arguments by the parameter name, improving code readability.

Example:
def greet(name, message="Hello"):
    return f"{message}, {name}!"

# Using default argument
print(greet("Alice"))  # Output: Hello, Alice!

# Overriding default argument
print(greet("Alice", message="Hi"))  # Output: Hi, Alice!

# Using keyword arguments
print(greet(name="Bob", message="Hey"))  # Output: Hey, Bob!

-------------------------------------------------------------------------------

2. *args:
- Allows a function to accept any number of positional arguments. 
- Inside the function, args is a tuple of all the passed positional arguments.

Example:
def example(*args):
    for arg in args:
        print(arg)

example(1, 2, 3)

-------------------------------------------------------------------------------

3. **kwargs:
- Allows a function to accept any number of keyword arguments. 
- Inside the function, kwargs is a dictionary of all the passed keyword arguments.

Example:
def example(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

example(a=1, b=2, c=3)

-------------------------------------------------------------------------------

Example with regular parameters, *args, and **kwargs:
def example_function(param1, param2, *args, **kwargs):
    print(f"param1: {param1}")
    print(f"param2: {param2}")

    print("\n*args:")
    for arg in args:
        print(arg)

    print("\n**kwargs:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Usage
example_function(10, 20, 30, 40, 50, key1="value1", key2="value2")

These features make functions more flexible and able to handle varying numbers of arguments.
"""

########## Problems ##########

# replace 'pass' with your code.
# The 'pass' keyword prevents python from throwing an error when a function is defined with no code inside.

# Write a function that takes in a list of numbers and returns the product of the numbers


def product(nums: list[int]) -> int:
  pass


# Write a function that takes in a list of numbers and returns their average


def average(nums: list[int]) -> float | int:
  pass


# Write a function that takes in a word and a letter as input, and returns how many times that letter occurs in the word.


def count_letter(word: str, letter: str) -> int:
  pass


# Write a function that takes in an integer as input, and returns how many times a digit appears.

# This is a tricky problem with 2 common solutions:


# Solution #1 involves using the 'mod' operation (% in python) and a division trick to check each digit of 'num'.
# The double slash '//' in python performs whole-number division.
def count_digit_with_mod(num: int, digit: int) -> int:
  pass


# Solution #2 involves converting to a string and then doing the same code as 'count_letter'.
# You can convert from integer to string in python wrapping the value in 'str()'.
# For example 'str(178)' will return the string '178'.
def count_digit_with_str(num: int, digit: int) -> int:
  pass


# Write a function that takes in a number and returns its factorial. Recall that


def factorial(num: int) -> int:
  pass


# Write a function that takes in an integer, n, and returns the Hailstone sequence starting at n as a list.
# The Hailstone sequence is as follows:
#   As long as n is not equal to 1,
#     print n
#     if n is an even number, cut n in half
#     otherwise, make n equal to three times itself, plus one
# Ex: Given the number 10, the Hailstone sequence is 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1


def get_hailstone_seq(num: int) -> int:
  pass
