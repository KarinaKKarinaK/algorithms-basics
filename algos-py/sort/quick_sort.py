# QUICK SORT
# As the name suggests, Quicksort is one of the fastest sorting algorithms.
# The Quicksort algorithm takes an array of values, chooses one of the values as 
# the 'pivot' element, and moves the other values so that lower values are on the 
# left of the pivot element, and higher values are on the right of it.

import time
# How it works:

# 1. Choose a value in the array to be the pivot element.
# 2. rder the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
# 3. Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
# 4. Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.

def quick_sort(list):
    length = len(list) 

    if length <= 1: # BAse case: if the list has 0 or 1 element, it is already sorted
        return list
    
    pivot = list.pop() # Settoing the pivot element to be the last element of the list
    # pop() is a list method that removes and returns the element of a list (if no argument is passed into ())
    high, low = [], [] # Creating two empty lists to hold the higher and lower values than the pivot element

    for item in list: # Looping through each element in the list
        if item > pivot: # If the currently looped through item is larger than teh pivot element then it is appeneded to the "highy" list
            high.append(item)
        else: # Else it is appended to teh "low" list
            low.append(item)
    
    return quick_sort(low) + [pivot] + quick_sort(high) # Recursively calling quick_sort on the low and high lists and 
  #concatenating them with the pivot element in between


mylist = [
    64, 34, 25, 12, 22, 11, 90, 5, 78, 45, 32, 67, 89, 23, 56, 99, 1, 77, 88, 100,
    54, 31, 29, 73, 81, 2, 9, 17, 38, 41, 60, 70, 85, 97, 13, 27, 49, 53, 62, 76,
    3, 8, 19, 21, 24, 28, 33, 36, 39, 42, 44, 46, 47, 50, 52, 55, 57, 59, 61, 63,
    65, 66, 68, 69, 71, 72, 74, 75, 79, 80, 82, 83, 84, 86, 87, 91, 92, 93, 94, 95,
    96, 98, 4, 6, 7, 10, 14, 15, 16, 18, 20, 26, 30, 35, 37, 40, 43, 48, 51, 58
]
start_time = time.time()
sorted_list = quick_sort(mylist)
end_time = time.time()

print(sorted_list)
print("Time taken:", end_time - start_time, "seconds")