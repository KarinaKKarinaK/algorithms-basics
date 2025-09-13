#include <iostream>   // For input/output
using namespace std; // Avoids writing std:: everywhere

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