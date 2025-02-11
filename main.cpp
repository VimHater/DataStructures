#include <iostream>
#include "Array/Array.h"

int main() {
    Array<int> data(10);
    data.fill(10);
    std::cout << data.at(9);
    data.print();
}