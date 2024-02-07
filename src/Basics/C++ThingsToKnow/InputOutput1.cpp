#include <iostream> //input and output
#include <math.h> //mathematical functions
#include <string> //string functions

int main() {
    std::cout << "Hello World\n"; //cout allows you to give an output
    std::cout << "Hello World" << "\n" << "Next line" << "\n"; //this way is faster
    std::cout << "Hello World" << std::endl; //just like \n, but also flushes output buffer, which cann be a costly operation
    return 0;
}