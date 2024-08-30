# Here is the documentation on Python Dictionaries:
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# and
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

# to warm up (and use for future refence) create an example usage for each method in the documentation

# clear

# copy

# get

# keys

# values

# items

# pop

# popitem

# update

# and some of the other primary ways that we interact with dictionaries:

# len

# iterating over keys

# iterating over values

# iterating over key-value pairs

# in

# d[key] (accessing/setting)

# del del[key]

########## Problems ##########

# Write a function that counts the frequency of each character in a given string and returns a dictionary with characters as keys and their frequencies as values.
# The 'frequency' of a character just means how many times it appears in the string.

def count_char_freqs(s: str) -> dict[str,int]:
  pass

# Write a function that takes in two strings and checks if they are anagrams of each other.
def are_anagrams(s1: str, s2: str) -> bool:
  pass

# Write a function that groups anagrams from a list of words. 
# Anagrams are words that have the same characters in a different order.
# It should return a dictionary where each key is the charcters of the anagram in alphebetical order and the value is a list of words that are anagrams.
# For example, if the input is ['cat', 'dog', 'tac', 'god', 'act'], then the output should be {'act': ['cat', 'tac', 'act'], 'dgo': ['dog', 'god']}.

def group_anagrams(lst: list[str]) -> dict[str, list[str]]:
  pass

# Write a function that inverts a given dictionary, swapping keys and values. 
# Assume all values are unique.
# Bonus Question: what goes wrong if values are not unique?

def invert_dict(d: dict) -> dict:
  pass

# Write a function that merges two dictionaries, combining values of common keys into a list.
# For example, if the input is {'a': 1, 'b': 2, 'c': 3} and {'b': 4, 'c': 5, 'd': 6}, then the output should be {'a': 1, 'b': [2, 4], 'c': [3, 5], 'd': 6}.

def merge_dicts(d1: dict, d2: dict) -> dict:
  pass

# Given a list of integers, write a function that returns the k most frequent elements.

def top_k_frequent(lst: list, k: int) -> list:
  pass

# Write a function that takes a list of names and phone numbers (as strings) and returns a dictionary representing a phonebook.

def create_phonebook(entries: tuple[str, str]) -> dict[str, int]:
  pass

# Write a function that finds the key with the maximum value in a dictionary.

def key_with_max_value(d: dict[str, int]) -> str:
  pass

# Write a function that takes in a list of integers and an integer n. 
# It should a pair of indices i and j such that the sum of the integers at indices i and j is n.

def pair_sum(lst: list[int], n: int) -> tuple[int, int]
  pass
