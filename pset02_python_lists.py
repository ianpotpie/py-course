# Here is the documentation on Python Lists:
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# and
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

# to warm up (and use for future refence) create an example usage for each method in the documentation

# append

# extend

# insert

# remove

# pop

# clear

# index

# count

# sort

# reverse

# copy

# and some of the other primary ways that we interact with lists:

# len

# in

# + (concatenation)

# s[i] (indexing)

# s[i:j] (slicing)

# s[i:j:k] (slicing with step)

# del

# for v in s (iteration)

########## Problems ##########

# Reverse a list using any approach you please BUT out of the list methods, you can only use 'pop' and 'append' (using brackets/slicing on lists is also not allowed).


def reverse(lst: list) -> list:
  pass


# Write a function that removes duplicates from a sorted list of integers, returning the list with unique elements only.


def remove_duplicates(lst: list[int]) -> list[int]:
  pass


# Write a function that rotates a list to the right by k steps.
# 'Rotating' involves taking the items at the end of the list and moving them to the beginning.
# For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [4, 5, 6, 1, 2, 3].


def rotate_list(lst: list, k: int) -> list:
  pass


# merge two sorted lists into a single sorted list.


def merge_sorted_lists(lst1: list, lst2: list) -> list:
  pass


# Given a list containing n distinct numbers taken from 0, 1, 2, ..., n, write a function to find the one that is missing from the list.
# The list may be out of order!


def find_missing_number(lst: list[int]) -> int:
  pass


# Write a function that moves all zeroes in a list to the end while maintaining the relative order of the non-zero elements.


def move_zeroes(lst: list[int]) -> list[int]:
  pass


# Write a function to find the intersection of two lists i.e. return a list of unique elements that are present in both lists.


def intersection(lst1: list, lst2: list) -> list[int]:
  pass


# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


def longest_common_prefix(lst: list[str]) -> str:
  pass


# Write a function that takes in a list of lists that returns a new list of all the individual maxes from each list.


def maxes(lst: list[list[int]]) -> list[int]:
  pass


# Write a function that takes in a list of lists, and returns a new list made from “flattening” the lists (putting every element from each list into a single list)


def flatten_list(lst: list[list]) -> list:
  pass
