#pragma once
#include "Node.h"

template<typename datatype>
class LinkedList {
public:
    LinkedList();
    ~LinkedList();
    void push_back();
    void insert_at(int index);
    void delete_node_at(int index);
    void delete_first();
    void delete_last();
    void print();
private:
    Node<datatype> *head;
};
