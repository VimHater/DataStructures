#pragma once
#include <cstddef>

template <typename datatype>
struct Node {
    datatype data;
    Node<datatype> *next;
};

template <typename datatype>
class Linked_list {
   public:
    Linked_list();
    //~Linked_list();
    void append(datatype data);
    void push_front(datatype data);
    std::size_t getsize();
    Node<datatype> *search_for(datatype data);
    void print();
    void insert_at(int position, datatype this_data);

   private:
    Node<datatype> *head;
};
