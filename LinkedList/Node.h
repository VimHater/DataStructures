#pragma once
#include <string>

template <typename datatype>
class Node {
    public:
    Node(datatype store);
    private:
    datatype data;
    datatype *next;
};
