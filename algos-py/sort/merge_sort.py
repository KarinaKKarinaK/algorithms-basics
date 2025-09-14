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

    leftHalf = list[:mid] # Slicing the list from the start to the middle index
    rightHalf = list[mid:] # Slicing the list from the middle index to the end

    if length == 1:
        return list # Base case: if the list has only one element, it is already sorted
    
    sortedLeft = merge_sort(leftHalf) # Recursively calling merge_sort on the left half
    sortedRight = merge_sort(rightHalf) # Recursively calling merge_sort on the right half

    return merge(sortedLeft, sortedRight) #Merging the two sorted halves


def merge(left, right): # This i s a helper function that merges two sorted lists into one sorted list
    result = [] # This will hold the merged list
    i = j = 0 # i is the index for the left list, j is the index for the right list

    while i < len(left) and j < len(right): # While there are still elements in both lists
        if left[i] < right[j]: # If the current element in the left list is less than the current element in the right list
            result.append(left[i]) # We add the element from the left list to the result
            i += 1 # We increment the index for the left list
        else:
            result.append(right[j]) # We add the element from the right list to the result
            j += 1 # We increment the index for the right list

        result.extend(left[i:]) # If there are any remaining elements in the left list, we add them to the result
        result.extend(right[j:]) # If there are any remaining elements in the right list, we add them to the result
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