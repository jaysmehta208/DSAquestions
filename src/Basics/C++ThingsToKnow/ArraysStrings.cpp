#include <bits/stdc++.h>
using namespace std;

int main() {
    // 1D array
    int a[5];
    cin >> a[0] >> a[1] >> a[2] >> a[3] >> a[4]; 
    a[3] += 5; // mutable
    cout << *(a + 1); // normal pointers
    for (int i = 0; i < 5; i++) {
        cout << a[i];
    }

    //2D array
    int arr[3][5];
    arr[1][3] = 10;

    string s = "Jay Mehta";
    cout << s[1] << "\n";
    int size = s.size();
    cout << s[size - 1] << "\n"; 
    cout << s.length() << "\n";
    s[5] = 'z'; //have to use characters
    cout << s[5];
}