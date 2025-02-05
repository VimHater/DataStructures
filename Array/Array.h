#pragma once


template <typename Arr>
class Array {
public:
    int size;
    explicit Array(int n);
    ~Array();
private:
    Arr *A;
};

