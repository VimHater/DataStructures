#include "Array2D.h"
#include<string>

using std::string;

template <typename datatype>
Array2D<datatype>::Array2D(size_t rows, size_t cols) : rows(rows), cols(cols) {
    data = new datatype*[rows];

    for (size_t i = 0; i < rows; i++) {
        data[i] = new datatype[cols]();
    }
}

template <typename datatype>
Array2D<datatype>::~Array2D() {
    delete[] data;
}

template<typename datatype>
void ::Array2D<datatype>::fill(datatype filler) {
    for (size_t i=0; i<rows; i++) {
        for (size_t j=0; j<cols; j++) {
            data[i][j] = filler;
        }
    }
}


template<typename datatype>
datatype& Array2D<datatype>::at(unsigned row_index, unsigned col_index) {
    if (row_index > rows || col_index > cols) {
        throw std::out_of_range("Index out of range");
    }
    return data[row_index][col_index];
}


template<typename datatype>
std::pair<size_t, size_t> Array2D<datatype>::getsize() {
    return {rows, cols};
}


template<typename datatype>
Array2D<datatype> Array2D<datatype>::Clone() {
    Array2D newArray2D(rows, cols);
    for (size_t i=0; i<rows; i++) {
        for (size_t j=0; j<cols; j++) {
            newArray2D.data[i][j] = data[i][j];
        }
    }
    return newArray2D;
}

template<typename datatype>
void Array2D<datatype>::print() {
    for (size_t i=0; i<rows; i++) {
        std::cout << "[";
        for (size_t j=0; j<cols - 1; j++) {
            std::cout << data[i][j] << " ";
        }
        std::cout << data[i][cols - 1];
        std::cout << "]\n";
    }
}



template class Array2D<int>;
template class Array2D<double>;
template class Array2D<float>;
template class Array2D<char>;
template class Array2D<string>;
template class Array2D<long long>;
template class Array2D<long double>;