# Merge Sort

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

    # list1, list2 = [], []

    # for i in range(length/2):
    #     if i != (length/2):
    #         list1.append(list[i])