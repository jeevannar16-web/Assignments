#include <iostream>
using namespace std;

int main() {
    int arr[5] = {5, 3, 1, 4, 2};
    int n = 5, i, temp;

    // Display (Creation)
    cout << "Array: ";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    // Insertion (add at end)
    arr[n] = 6;
    n++;

    cout << "\nAfter insertion: ";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    // Deletion (remove last element)
    n--;

    cout << "\nAfter deletion: ";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    // Searching (find 4)
    for(i = 0; i < n; i++) {
        if(arr[i] == 4) {
            cout << "\n4 found at index " << i;
        }
    }

    // Sorting (simple bubble sort)
    for(i = 0; i < n - 1; i++) {
        for(int j = 0; j < n - i - 1; j++) {
            if(arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    cout << "\nAfter sorting: ";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}