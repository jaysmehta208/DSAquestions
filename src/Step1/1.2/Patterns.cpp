#include <bits/stdc++.h>
using namespace std;

void pattern4() {
    for (int i = 1; i < 6; i++) {
        for (int j = 1; j <= i; j++) {
            cout << i;
        }
        cout << "\n";
    }
}

void pattern12() {
    for (int i = 1; i < 5; i++) {
        for (int j = 1; j < 9; j++) {
            if (min(j, 9 - j) <= i) {
                cout << min(j, 9 - j);
            } else {
                cout << " ";
            }
        }
        cout << "\n";
    }
}

void pattern18() {
    for (int i = 1; i < 6; i++) {
        for (int j = 1; j < 6; j++) {
            if (j <= i) {
                cout << char('E' - i + j);
            } else {
                break;
            }
        }
        cout << "\n";
    }
}

void pattern21() {
    int x = 8;
    int min = 1;
    int max = x - 1;
    for (int i = 1; i < x; i++) {
        for (int j = 1; j < x; j++) {
            if (i == min || j == min || i == max || j == max) {
                cout << ("*");
            } else {
                cout << " ";
            }
        }
        cout << "\n";

    }
}

void pattern22() {
    int x = 8;
    for (int i = 1; i <= x/2; i++) {
        for (int j = 1; j < x; j++) {
            if (j <= i) {
                cout << x/2 + 1 - j;
            } else if (j <= x/2){
                cout << x/2 + 1 - i;
            } else if (x - j >= i) {
                cout << x/2 + 1 - i;
            } else {
                cout << j - x/2 + 1;
            }
        }
        
        cout << "\n";
    }
}

int main() {
    pattern22();
    return 0;
}

