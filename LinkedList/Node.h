#pragma once
#include <cstddef>
#include <iostream>
#include <string>

template <typename datatype>
class Node {
    public:
    Node(datatype store);
    private:
    datatype data;
    datatype *next;
};
