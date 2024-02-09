#include <bits/stdc++.h>
using namespace std;

void count(int a) {
    int counter = 0;
    while (a > 0)
    {
        a = a/10;
        counter++;
    }
    cout << counter << "\n";
    
} 
int main() {
    int n;
    cin >> n;
    cout << to_string(n).length() << "\n";
    count(n);

}

