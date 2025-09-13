#include <vector>
#include <iostream>
using namespace std;

int linear_search(const vector<int>& array, int x){
    for (int i = 0; i < array.size(); i++){
        if (array[i] == x){
            return i
        }
    }
    return -1
}