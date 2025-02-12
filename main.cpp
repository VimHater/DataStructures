#include <iostream>
#include "Array/Array.h"
#include "Array/Array2D.h"
int main() {
    Array2D<int> data(10, 10);
    data.fill(10);
    data.print();
}