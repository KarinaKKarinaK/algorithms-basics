# QUICK SORT
import time
# How it works:

# 1. Choose a value in the array to be the pivot element.
# 2. rder the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
# 3. Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
# 4. Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.

def quick_sort(list):
    length = len(list)

    if length <= 1:
        return list
    
    pivot = list.pop()
    # pop() is a list method that removes and returns the element of a list (if no argument is passed into ())
    high, low = [], []

    for item in list:
        if item > pivot:
            high.append(item)
        else:
            low.append(item)
    
    return quick_sort(low) + pivot + quick_sort(high)


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