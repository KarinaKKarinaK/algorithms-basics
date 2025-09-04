# BUBBLE SORT
# How it works:

# 1. Go through the array, one value at a time.
# 2. For each value, compare the value with the next value.
# 3. If the value is higher than the next one, swap the values so that the highest value comes last.
# 4. Go through the array as many times as there are values in the array.

def bubble_sort(list):
    n = len(list)
    for i in range(n-1):
        for j in range(n-i-1):
            if list[j] > list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]
    
    return list


# Example
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

print(bubble_sort(mylist))