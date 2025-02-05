#pragma once
#include <Node.h>
#include <string>

template<typename datatype>
class LinkedList {
public:
    LinkedList<datatype>();
    ~LinkedList<datatype>();
private:
    Node<datatype> *Head;
};

