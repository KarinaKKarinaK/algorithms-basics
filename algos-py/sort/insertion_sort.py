import time
# INSERTION SORT
# How it works:

# 1. Take the first value from the unsorted part of the array.
# 2. Move the value into the correct place in the sorted part of the array.
# 3. Go through the unsorted part of the array again as many times as there are values.


def insertion_sort(list):
    for i in range (1, len(list)): # Starting from teh second element of teh list we loop through the entire list
        j = i # We set j to the current index of i which is the second element of the list
        # Here j is used as the index of the element we are currently comparing
        while j > 0 and list[j - 1] > list[j]: # While j is greater than 0 and the previous element is greater than the current element
            # We swap teh elements
            list[j], list[j - 1] = list[j - 1], list[j] 
            j -= 1 # Now we decrement j by 1 to check the next element
    
    return list

# This is different than bubble sort because in bubble sort we compare adjacent elements and swap them if they are in the wrong order
# In insertion sort we take the current element and compare it to all the previous elements until we find the correct position for it


mylist = [
    64, 34, 25, 12, 22, 11, 90, 5, 78, 45, 32, 67, 89, 23, 56, 99, 1, 77, 88, 100,
    54, 31, 29, 73, 81, 2, 9, 17, 38, 41, 60, 70, 85, 97, 13, 27, 49, 53, 62, 76,
    3, 8, 19, 21, 24, 28, 33, 36, 39, 42, 44, 46, 47, 50, 52, 55, 57, 59, 61, 63,
    65, 66, 68, 69, 71, 72, 74, 75, 79, 80, 82, 83, 84, 86, 87, 91, 92, 93, 94, 95,
    96, 98, 4, 6, 7, 10, 14, 15, 16, 18, 20, 26, 30, 35, 37, 40, 43, 48, 51, 58
]
start_time = time.time()
sorted_list = insertion_sort(mylist)
end_time = time.time()

print(sorted_list)
print("Time taken:", end_time - start_time, "seconds")