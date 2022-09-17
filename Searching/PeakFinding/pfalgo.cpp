#include<iostream>
using std::cout;
using std::endl;

int pfinder(int *array, int length);

int main() {
    int arr[] = {1,2,1,3,5,6,4};
    int len = sizeof(arr) / sizeof(int);
    cout << pfinder(arr, len) << endl;
}

int pfinder(int *array, int length) {
    int start = 0, end = length-1, mid;

    while (start <= end) {
        mid = (start + end) / 2;

        if ((mid == 0 || array[mid] > array[mid-1]) && (mid == length-1 || array[mid] > array[mid+1])) {
            return mid;
        } else if (array[mid + 1] > array[mid]) {
            start = mid + 1;
        } else {
            end = mid;
        }
    }

    return -1;
}