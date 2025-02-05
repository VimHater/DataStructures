#include <iostream>

#include "Array/Array.h"

int main() {
    Array<int> data(10);
    data.asign(0, 10);
    std::cout<< data.value_at(0);
}