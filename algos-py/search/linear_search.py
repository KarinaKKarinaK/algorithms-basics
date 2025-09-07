import time

def linear_search(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
        

array1 = [
    2187, 142, 2012, 1847, 1203, 229, 1732, 2123, 187, 2056, 1567, 2222, 198, 110, 2220, 1456, 172, 2099, 1345, 2100,
    1789, 222, 1999, 1234, 201, 1890, 210, 2200, 145, 2001, 178, 2300, 199, 1200, 2101, 189, 200, 2011, 1457, 2120,
    1788, 2221, 1346, 2102, 1787, 2223, 1347, 2103, 1786, 2224, 1348, 2104, 1785, 2225, 1349, 2105, 1784, 2226, 1350,
    2106, 1783, 2227, 1351, 2107, 1782, 2228, 1352, 2108, 1781, 2229, 1353, 2109, 1780, 2230, 1354, 2110, 1779
]
start_time = time.time()
searched_item = linear_search(array1, 2229)
end_time = time.time()

print(searched_item)
print("Time taken:", end_time - start_time, "seconds")
