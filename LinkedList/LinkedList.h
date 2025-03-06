#pragma once
#include <cstddef>

template <typename datatype>
struct node {
    datatype data;
    node<datatype> *next;
};

template <typename datatype>
class Linked_list {
   public:
    Linked_list();
    ~Linked_list();
    void push_back(datatype data);
    void push_front(datatype data);
    std::size_t getsize();
    node<datatype> *search_for(datatype data);
    void print();
    void insert_at(int position, datatype this_data);

   private:
    node<datatype> *head;
    size_t size;
};
