#include "Array.h"

template<typename Arr>
Array<Arr>::Array(int n) {
    size = n;
    A = new Arr[size];
}

template<typename Arr>
Array<Arr>::~Array() {
    delete[] A;
}


