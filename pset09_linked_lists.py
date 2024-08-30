# ArrayList

# An ArrayList is a dynamic array implementation that allows elements to be added or removed.
# It provides the advantage of random access (like arrays) while still being dynamically sized (like linked lists).

# Key features:
# 1. Dynamic size
# 2. Random access
# 3. Efficient for accessing elements by index
# 4. May require resizing when capacity is reached

# The ArrayList has an underlying array that stores the elements.
# When the array is full and a new element needs to be added, a new, larger array is created,
# and all elements are copied over. This operation is called resizing.

# Advantages over linked lists:
# 1. Constant-time access to any element by index
# 2. Better cache locality and memory efficiency

# Disadvantages compared to linked lists:
# 1. Insertion and deletion in the middle of the list can be slower
# 2. Resizing operation can be costly when it occurs

# > When we insert or delete in the middle, all elements to the right must be shifted over.
# > The size of the array used to store elements may be different from the size of the ArrayList. For example, the initial size of the array may be 10, but the ArrayList may only use 3 of those slots.
# > When we reach the capacity of the ArrayList, we need to create a new, bigger array and copy all elements over.

# TODO: implement an ArrayList by filling out the methods
# what is the time complexity of each method with respect to the number of elements in the list?

from arrays import Array

class ArrayList:
    def __init__(self, initial_capacity=10):
        self.array = Array(initial_capacity)
        self.size = 0
        self.capacity = initial_capacity

    # Normal Methods
    def append(self, val) -> None:
        # adds an item to the end of the list
        pass

    def pop(self, idx=-1) -> object:
        # removes and returns the value at the specific index
        pass

    def insert(self, idx, val) -> None:
        # inserts a value at the specified index
        pass

    def remove(self, val) -> None:
        # removes the first occurence of a value
        pass

    def index(self, val, start=0, end=-1) -> int:
        # returns the index of the first occurence of 'val' (between start and end)
        pass

    def count(self, val) -> int:
        # returns the number of times the value appears in the list
        pass

    def reverse(self) -> None:
        # reverses the elements of the list in-place
        pass

    def extend(self, vals):
        # adds all items from an iterable to the end of the list
        pass

    def _resize(self, new_capacity):
        # internal method to resize the underlying array
        pass

    # Magic/Dunder methods
    def __len__(self) -> int:
        # allows use of len() function
        pass

    def __repr__(self) -> str:
        # returns a string representation of the list
        pass

    def __getitem__(self, index) -> object:
        # enables indexing and slicing like 'list[3]'
        pass

    def __delitem__(self, index) -> None:
        # enables item deletion, like 'del list[2]'
        pass

    def __setitem__(self, index, value) -> None:
        # enables item assignment, like 'list[1] = 10'
        pass

    def __contains__(self, item) -> bool:
        # allows use of the 'in' operator to check if the list contains a value
        pass

    def __add__(self, other) -> 'ArrayList':
        # allows use of the '+' operation between lists for concatenation
        pass

    def __eq__(self, other) -> bool:
        # allows use of the '==' operation to check if two lists are the same
        pass

