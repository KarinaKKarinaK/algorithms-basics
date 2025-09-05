# Merge Sort
import time

# The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first 
# breaking it down into smaller arrays, and then building the array back together the 
# correct way so that it is sorted.

# How it works:

# 1. Divide the unsorted array into two sub-arrays, half the size of the original.
# 2. Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
# 3. Merge two sub-arrays together by always putting the lowest value first.
# 4. Keep merging until there are no sub-arrays left.

def merge_sort(list):
    length = len(list)

    mid = length // 2

    leftHalf = list[:mid]
    rightHalf = list[mid:]

    if length == 1:
        return list
    
    sortedLeft = merge_sort(leftHalf)
    rightLeft = merge_sort(rightHalf)

    return merge(leftHalf, rightHalf)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(left[j])
            j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        # .extend() adds multiple elements from an iterable (such as a list, tuple, set, or string) 
        # to the end of an existing list.

        return result

# Testing merge sort

mylist = [
    64, 34, 25, 12, 22, 11, 90, 5, 78, 45, 32, 67, 89, 23, 56, 99, 1, 77, 88, 100,
    54, 31, 29, 73, 81, 2, 9, 17, 38, 41, 60, 70, 85, 97, 13, 27, 49, 53, 62, 76,
    3, 8, 19, 21, 24, 28, 33, 36, 39, 42, 44, 46, 47, 50, 52, 55, 57, 59, 61, 63,
    65, 66, 68, 69, 71, 72, 74, 75, 79, 80, 82, 83, 84, 86, 87, 91, 92, 93, 94, 95,
    96, 98, 4, 6, 7, 10, 14, 15, 16, 18, 20, 26, 30, 35, 37, 40, 43, 48, 51, 58
]
start_time = time.time()
sorted_list = merge_sort(mylist)
end_time = time.time()

print(sorted_list)
print("Time taken:", end_time - start_time, "seconds")