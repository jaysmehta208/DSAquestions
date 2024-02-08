#include <bits/stdc++.h>
using namespace std;
/*
 types of functions
 - void
 - return
 - parameterised
 - non parameterised
*/ 
// pass by value: int, string, vector, map, list
// pass by reference: array
//parameterised void function
void printName(string name) {
    cout << "Hello " << name << "\n";
}

//paramterised and returns
int sum(int a, int b) {
    return a + b;
}

// passs by value
void change(string a) {
    a[1] = 'r';
}

void changeString(string &s) {
    s[0] = 'z';
}

// pass by reference
void changearr(int arr[]) {
    arr[2] = 5;
}

void changeInt(int* s) {
    *s = 0;
}

int main() {
    string name;
    cin >> name;
    printName(name);
    cout << sum(4, 5) << "\n";
    cout << min(5,6) << "\n";
    change(name);
    cout << name << "\n";
    int arr[] = {1,2,3,4,5};
    changearr(arr);
    cout << arr[3] << "\n";
    
    changeString(name);
    cout << name << "\n";
    int x = 6;
    cout << x << "\n";
    changeInt(&x);
    cout << x << "\n";
    return 0;
}