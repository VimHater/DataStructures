#pragma once
#include <iostream>
#include <cstddef>

template <typename datatype>
class Array2D {
public:
    Array2D(size_t rows ,size_t cols);
    ~Array2D();
    Array2D Clone();
    datatype &at(unsigned row_index, unsigned col_index);
    std::pair<size_t, size_t> getsize();
    void fill(datatype filler);
    void print();

private:
    datatype **data;
    size_t rows;
    size_t cols;
};