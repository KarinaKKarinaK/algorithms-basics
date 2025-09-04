# INsertion sort

# How it works:

# 1. Take the first value from the unsorted part of the array.
# 2. Move the value into the correct place in the sorted part of the array.
# 3. Go through the unsorted part of the array again as many times as there are values.


def insertion_Sort(list):
    n = len(list)
    for i in range (1, n):
        insert_index = i
        current_value = list.pop(i)