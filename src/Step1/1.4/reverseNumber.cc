#include <bits/stdc++.h>
using namespace std;

void reverseNum(int a) {
    int b = 0;
    while (a > 0) {
        b = b*10 + a%10;
        a = a/10;
    }
    cout << b;
}

int main() {
    int a;
    cin >> a;
    string b = to_string(a);
    reverse(b.begin(), b.end());
    cout << b << "\n";
    reverseNum(a);
}

