# Notes: stable vs unstable algorithms
# If two elements have the same value in a stable algorithm, they will be in the same order in the output as the input.
# In unstable sorting algorithms, the order of elements with the same value undefined.

# Algorithm 1: Bubble Sort
#
# Bubble Sort does several 'passes' through a list.
# In each pass, it proceeds element-by-element through the list.
# At each step in the pass, it compares adjacent elements and swaps them if they are in the wrong order.
# The passes continue until the list is sorted.
#
# What is the worst case scenario time complexity?
# What is the best case scenario time complexity?
# What is the average time complexity?


def bubble_sort(arr):
    pass


# Algorithm 2: Selection Sort
#
# Selection Sort divides the input list into two parts: the sublist of sorted items on the left and the sublist of unsorted items on the right,
# Initially, the sorted sublist is empty and the unsorted sublist is the entire input list.
# This algorithm also does a series of passes through the unsorted portion of the list.
# In each pass, it finds the smallest element in the unsorted sublist and swaps it with the leftmost unsorted element.
# The leftmost element in the unsorted list is now the greatest element in the sorted sublist.
# The sorted sublist grows by one element each time and the unsorted sublist shrinks by one element each time.
# This process continues until the entire list is sorted and the unsorted list is empty.
#
# What is the worst case scenario time complexity?
# What is the best case scenario time complexity?
# What is the average time complexity?

def selection_sort(arr):
    pass


# Algorithm 3: Insertion Sort
#
# Insertion Sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time.
# Like selection sort, it divides the input list into two parts: the sorted sublist on the left and the unsorted sublist on the right.
# It takes the first element of the unsorted sublist, and inserts it into the sorted sublist.
# If it needs to be inserted in the middle of the sorted sublist, it will have to shift all the following elements to the right. 
# Unlike selection sort, it takes the first unsorted element, instead of doing a pass to find the minimum.
#
# What is the worst case scenario time complexity?
# What is the best case scenario time complexity?
# What is the average time complexity?


def insertion_sort(arr):
    pass


# Algorith 4: Merge Sort
#
# Implement the Merge Sort algorithm.
# Merge Sort is a Divide and Conquer algorithm. 
# It divides the input array into two halves, and recursively calls itself on the two halves,
# The algorithm then merges the two sorted halves to produce the final sorted array.
#
# What is the time complexity of merging to pre-sorted lists?
#
# What is the worst case scenario time complexity?
# What is the best case scenario time complexity?
# What is the average time complexity?

def merge_sort(arr):
    pass


# Algorithm 5: Quick Sort
#
# Quick Sort is another Divide and Conquer algorithm.
# It picks an element as pivot and partitions the given array around the picked pivot.
# There are many different versions of quickSort that pick pivot in different ways.
# After partitioning, it recursively sorts the subarrays on each side of the pivot.
#
# What is the worst case scenario time complexity?
# What is the best case scenario time complexity?
# What is the average time complexity?

def quick_sort(arr):
    pass

# Algorithm 6: Bucket Sort
#
# Bucket Sort is mainly useful when input is uniformly distributed over a range.
# It creates a numbers of buckets/bins, each for a pre-defined range of values.
# It iterates through the inputs lists and places each value into its designated bucket, then sorts each bucket individually.
# Each bucket is sorted using another algorithm or by recursively applying bucket sort.
#
# What is the worst case scenario time complexity?
# What is the best case scenario time complexity? 
# What is the average time complexity?

def bucket_sort(arr):
    pass

# Algorithm 7: Counting Sort
#
# Counting Sort is an integer sorting algorithm.
# It is good for sorting elements that have a small number of possible values.
# It starts by creating a size k 'counts' array of zeros, where k is the range of input values ((max - min) + 1).
# For each value in the input array, it increments the corresponding 'counts' array element by 1.
# Once completed, it uses the 'count' array to create the sorted output array.
# It does os by decrementing the counts array by 1 and placing the corresponding input value into the output array.
#
# What is the worst case scenario time complexity?
# What is the best case scenario time complexity?
# What is the average time complexity?

def counting_sort(arr):
    pass

# Algorithm 8: Radix Sort
#
# Radix Sort is an integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value.
# It starts by creating bins for each digit value (0-9 in decimal).
# Starting from the least significant digit, it places each element into the appropriate bin.
# Then, it iterates through the bins and places each element back into a single large array.
# This process continues until we have gone through all nonzero-digits and the final array is sorted.
#
# What is the worst case scenario time complexity?
# What is the best case scenario time complexity?
# What is the average time complexity?

def radix_sort(arr):
    pass
