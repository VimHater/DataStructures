#pragma once

template <typename datatype>
class Array {
public:
    int size;
    explicit Array(int size);
    ~Array();
    datatype value_at(int index);
    void asign(int index, datatype data);
private:
    datatype* arr;
};
