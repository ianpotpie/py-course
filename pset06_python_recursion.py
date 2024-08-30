# Recursive Functions Assignment

# Recursion is a programming technique where a function calls itself to solve a problem.
# It's particularly useful for problems that can be broken down into smaller, similar subproblems.

# Here are some key points to remember about recursive functions:
# 1. Base case: Every recursive function must have a condition to stop the recursion.
# 2. Recursive case: The function calls itself with a modified input.
# 3. Progress towards the base case: Each recursive call should bring the problem closer to the base case.

# For more information on recursion in Python, check out:
# https://docs.python.org/3/faq/programming.html#how-do-i-write-a-recursive-function

########## Problems ##########

# NOTE: For each problem, try to find the time complexity formula (this formula may also be recursively defined)

# 1. Write a recursive function to calculate the factorial of a number.
# Remember, factorial(n) = n * factorial(n-1), and factorial(0) = 1


def factorial(n: int) -> int:
    pass


# 2. Implement a recursive function to compute the nth Fibonacci number.
# The Fibonacci sequence is defined as: fib(n) = fib(n-1) + fib(n-2), with fib(0) = 0 and fib(1) = 1


def fibonacci(n: int) -> int:
    pass


# 3. Create a recursive function to calculate the sum of all numbers from 1 to n.


def sum_to_n(n: int) -> int:
    pass


# 4. Write a recursive function to reverse a string.


def reverse_string(s: str) -> str:
    pass


# 5. Implement a recursive binary search function.
# Assume the input list is sorted in ascending order.


def binary_search(arr: list, target: int) -> int:
    pass


# 6. Create a recursive function to calculate the power of a number (x^n).


def power(x: float, n: int) -> float:
    pass


# 7. Implement a recursive function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
#
# The Euclidean algorithm for finding the GCD of two numbers a and b is based on the principle that
# the greatest common divisor of two numbers does not change if the smaller number is subtracted
# from the larger number. See if you can take it from there (what are the base cases?).


def gcd(a: int, b: int) -> int:
    pass


# 8. Write a recursive function to generate all possible permutations (ways of ordering the elements) of a string.


def permutations(s: str) -> list[str]:
    pass


# 9. Create a recursive function to solve the Tower of Hanoi puzzle.
# The function should print the steps to move n disks from source to destination using an auxiliary peg.
#
# The Tower of Hanoi is a classic problem in computer science and mathematics:
# - There are three pegs (usually labeled A, B, and C) and n disks of different sizes.
# - Initially, all disks are stacked on the source peg (A) in order of decreasing size, with the largest at the bottom.
# - The goal is to move all disks to the destination peg (C) while following these rules:
#   1. Only one disk can be moved at a time.
#   2. Each move consists of taking the upper disk from one stack and placing it on top of another stack or an empty peg.
#   3. No larger disk may be placed on top of a smaller disk.
#
# This problem is tricky, don't spend too much time attempting it along.


def tower_of_hanoi(n: int, start: str, end: str, aux: str) -> None:
    pass


# 10. Implement a recursive function to check if a given string is a palindrome.


def is_palindrome(s: str) -> bool:
    pass
