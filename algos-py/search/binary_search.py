import time
# Binary search

# How it works:

# 1. Check the value in the center of the array.
# 2. If the target value is lower, search the left half of the array. If the target value is higher, search the right half.
# 3. Continue step 1 and 2 for the new reduced part of the array until the target value is found or until the search area is empty.
# 4. If the value is found, return the target value index. If the target value is not found, return -1.


def binary_search(array, x):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] < x:
            low = mid + 1
        elif array[mid] > x:
            high = mid -1
        else:
            return mid

    return -1

array1 = [
    2187, 142, 2012, 1847, 1203, 229, 1732, 2123, 187, 2056, 1567, 2222, 198, 110, 2220, 1456, 172, 2099, 1345, 2100,
    1789, 222, 1999, 1234, 201, 1890, 210, 2200, 145, 2001, 178, 2300, 199, 1200, 2101, 189, 200, 2011, 1457, 2120,
    1788, 2221, 1346, 2102, 1787, 2223, 1347, 2103, 1786, 2224, 1348, 2104, 1785, 2225, 1349, 2105, 1784, 2226, 1350,
    2106, 1783, 2227, 1351, 2107, 1782, 2228, 1352, 2108, 1781, 2229, 1353, 2109, 1780, 2230, 1354, 2110, 1779
]
start_time = time.time()
searched_item = binary_search(array1, 2229)
end_time = time.time()

print(searched_item)
print("Time taken:", end_time - start_time, "seconds")


