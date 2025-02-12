#include "Array.h"
#include <iostream>
#include <string>
using std::string;


template <typename datatype>
Array<datatype>::Array(size_t len) {
    size = len;
    data = new datatype[size]();
}

template <typename datatype>
Array<datatype>::~Array() {
    delete[] data;
}

template <typename datatype>
datatype& Array<datatype>::at(unsigned index) {
    if (index >= size) {
        throw std::out_of_range("Index out of range");
    }
    return data[index];
}

template<typename datatype>
void Array<datatype>::fill(datatype filler) {
    for (size_t i=0; i<size; i++) {
        data[i] = filler;
    }
}

template<typename datatype>
void Array<datatype>::del(unsigned index) {
    if (index >= size) {
        throw std::out_of_range("out of range");
    }
    for (size_t i=0; i<size - 1; i++) {
        if (i >= index) data[i] = data[i+1];
    }
    size--;
}

template<typename datatype>
size_t Array<datatype>::getsize() {
    return size;
}

template<typename datatype>
void Array<datatype>::print() {
    std::cout << "[";
    for (size_t i=0; i<size - 1; i++) {
        std::cout << data[i] << " ";
    }
    std::cout << data[size - 1];
    std::cout << "]";
}

template<typename datatype>
Array<datatype> Array<datatype>::Clone() {
    Array newArray(size);
    for (size_t i=0; i<size; i++) {
        newArray.data[i] = data[i];
    }
    return newArray;
}


template class Array<int>;
template class Array<double>;
template class Array<float>;
template class Array<char>;
template class Array<string>;
template class Array<long long>;
template class Array<long double>;