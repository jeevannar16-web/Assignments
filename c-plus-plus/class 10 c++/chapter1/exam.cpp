#include <iostream>
using namespace std;

int main() {
    int arr[100], n, i, pos, value, item;

    // Creation
    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter elements:\n";
    for(i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Display
    cout << "\nArray: ";
    for(i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    // Insertion
    cout << "\nEnter position to insert: ";
    cin >> pos;
    cout << "Enter value: ";
    cin >> value;

    for(i = n; i > pos; i--) {
        arr[i] = arr[i - 1];
    }
    arr[pos] = value;
    n++;

    cout << "After insertion: ";
    for(i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    // Deletion
    cout << "\nEnter position to delete: ";
    cin >> pos;

    for(i = pos; i < n - 1; i++) {
        arr[i] = arr[i + 1];
    }
    n--;

    cout << "After deletion: ";
    for(i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    // Searching (Linear Search)
    cout << "\nEnter element to search: ";
    cin >> item;

    for(i = 0; i < n; i++) {
        if(arr[i] == item) {
            cout << "Element found at position " << i << endl;
            break;
        }
    }
    if(i == n) {
        cout << "Element not found\n";
    }

    // Sorting (Ascending - Bubble Sort)
    for(i = 0; i < n - 1; i++) {
        for(int j = 0; j < n - i - 1; j++) {
            if(arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    cout << "After sorting: ";
    for(i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}