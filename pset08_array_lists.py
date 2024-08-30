# Linked Lists

# A linked list is a linear data structure consisting of nodes, where each node contains data and a reference (or link) to the next node in the sequence. Unlike arrays, linked lists don't store elements in contiguous memory locations.

# Key features:
# 1. Dynamic size
# 2. Efficient insertion and deletion
# 3. No random access

# The start of the linked list is called the 'head'.
# To access an element in list, we start at the head and then follow the links/references until we reach the element that we want.
# The last node in the list has a reference to 'null' or 'None' in Python to indicate it is the final node.

# There are several types:
# 1. Singly linked list: Each node points to the next node
# 2. Doubly linked list: Each node points to both the next and previous nodes
# 3. Circular linked list: The last node points back to the first node


# TODO: implement a singly linked list by filling out the methods
# what is the time complexity of each method with respect to the length of the list?

class SinglyLinkedNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next_node = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None # when the head is 'None' the list is empty

    # Normal Methods
    def append(self, val) -> None:
        # adds an item to the end of the list
        pass

    def pop(idx=-1) -> object:
        # removes and returns the value at the specific index
        pass
    
    def insert(self, idx, val) -> None:
        # inserts a value at the specified index
        pass

    def remove(self, val) -> None:
        # removes the first occurence of a value
        pass

    def index(val, start=0, end=-1) -> int:
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
    
    # Magic/Dunder methods
    def __len__(self) -> None:
        # allows use of len() function
        pass

    def __repr__(self) -> str:
        # returns a string representation of the list
        pass

    def __getitem__(self, index) -> object:
        # enables indexing and slicing like 'list[3]'
        pass

    def __delitem__(self, index) -> object:
        # enables item deletion, like 'del list[2]'
        pass
    
    def __setitem__(self, index, value) -> object:
        # enables item assignment, like 'list[1] = 10'
        pass

    def __contains__(self, item) -> bool:
        # allows use of the 'in' operator to check if the list contains a value
        pass

    def __add__(self, other) -> SinglyLinkedList:
        # allows use of the '+' operation between lists for concatenation
        pass

    def __eq__(self, other) -> bool:
        # allows use of the '==' operation to check if two lists are the same
        pass

# TODO: implement a double linked list by filling out the methods
# what is the time complexity of each method with respect to the length of the list?

class DoublyLinkedNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next_node = None
        self.prev_node = None
        

class DoublyLinkedList:
    def __init__(self) -> None:
        # self.head and self.tail are both 'None' when the list is empty
        self.head = None
        self.tail = None 
    
    # Normal Methods
    def append(self, val) -> None:
        # adds an item to the end of the list
        pass

    def pop(idx=-1) -> object:
        # removes and returns the value at the specific index
        pass

    def insert(self, idx, val) -> None:
        # inserts a value at the specified index
        pass

    def remove(self, val) -> None:
        # removes the first occurence of a value
        pass

    def index(val, start=0, end=-1) -> int:
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

    # Magic/Dunder methods
    def __len__(self) -> None:
        # allows use of len() function
        pass

    def __repr__(self) -> str:
        # returns a string representation of the list
        pass

    def __getitem__(self, index) -> object:
        # enables indexing and slicing like 'list[3]'
        pass

    def __delitem__(self, index) -> object:
        # enables item deletion, like 'del list[2]'
        pass

    def __setitem__(self, index, value) -> object:
        # enables item assignment, like 'list[1] = 10'
        pass

    def __contains__(self, item) -> bool:
        # allows use of the 'in' operator to check if the list contains a value
        pass

    def __add__(self, other) -> DoublyLinkedList:
        # allows use of the '+' operation between lists for concatenation
        pass

    def __eq__(self, other) -> bool:
        # allows use of the '==' operation to check if two lists are the same
        pass

