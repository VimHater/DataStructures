#pragma once
#include <cstddef>

template <typename datatype>
class Array {
public:
    Array(size_t len);
    ~Array();
    Array Clone();
    datatype &at(unsigned index);
    void fill(datatype filler);
    void del(unsigned index);
    size_t getsize();
    void print();
private:
    datatype *data;
    size_t size;
};
