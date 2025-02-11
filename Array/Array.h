#pragma once
#include <cstddef>
template <typename datatype>
class Array {
public:
    size_t size;
    Array(size_t len);
    ~Array();
    Array *Arrcpy(Array &old);
    datatype &at(unsigned index);
    void fill(datatype filler);
    void del(unsigned index);
    size_t getsize();
    void print();
private:
    datatype *data;
};