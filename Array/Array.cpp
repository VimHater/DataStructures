#include "Array.h"
#include<string>

template class Array<int>;
template class Array<double>;
template class Array<std::string>;
template class Array<char>;
template class Array<long double>;
template class Array<long long>;
template class Array<unsigned>;
template class Array<unsigned long long>;

template <typename datatype>
Array<datatype>::Array(int size) : size(size) {
    arr = new datatype[size];
}

template <typename datatype>
Array<datatype>::~Array() {
    delete[] arr;
}

template <typename datatype>
datatype Array<datatype>::value_at(int index) {
    return arr[index];
}

template<typename datatype>
void Array<datatype>::asign(int index, datatype data) {
    arr[index] = data;
}


