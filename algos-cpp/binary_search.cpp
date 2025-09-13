#include <iostream>   // For input/output
using namespace std; // Avoids writing std:: everywhere

#include <iostream>
#include <vector>
#include <chrono>

int binary_search(const vector<int>& array, int x) {
    int left = 0;
    int right = array.size() - 1;

    while (left <= right) {
        int mid = (left + right) / 2;

        if (array[mid] < x) {
            left = mid + 1;
        } else if (array[mid] > x){
            right = mid - 1;
        } else {
            return mid;
        }
    }
    return -1
}

int main() {
    std::vector<int> array1 = {
        2187, 142, 2012, 1847, 1203, 229, 1732, 2123, 187, 2056, 1567, 2222, 198, 110, 2220, 1456, 172, 2099, 1345, 2100,
        1789, 222, 1999, 1234, 201, 1890, 210, 2200, 145, 2001, 178, 2300, 199, 1200, 2101, 189, 200, 2011, 1457, 2120,
        1788, 2221, 1346, 2102, 1787, 2223, 1347, 2103, 1786, 2224, 1348, 2104, 1785, 2225, 1349, 2105, 1784, 2226, 1350,
        2106, 1783, 2227, 1351, 2107, 1782, 2228, 1352, 2108, 1781, 2229, 1353, 2109, 1780, 2230, 1354, 2110, 1779
    };

    auto start_time = std::chrono::high_resolution_clock::now();
    int searched_item = binary_search(array1, 2229);
    auto end_time = std::chrono::high_resolution_clock::now();

    std::cout << searched_item << std::endl;
    std::cout << "Time taken: "
              << std::chrono::duration<double>(end_time - start_time).count()
              << " seconds" << std::endl;

    return 0;
}