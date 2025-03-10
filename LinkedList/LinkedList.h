#pragma once
#include <cstddef>
#include <iterator>

template <typename datatype>
struct Node {
    datatype data;
    Node<datatype> *next;
};

template <typename datatype>
class Linked_list {
   public:
    Linked_list();
    ~Linked_list();
    void append(datatype data);
    void push_front(datatype data);
    std::size_t getsize();
    Node<datatype> *search_for(datatype data);
    void print();
    void insert_at(int position, datatype this_data);

   private:
    Node<datatype> *head;
};

template<typename datatype>
class Linked_list_t {
    public:
    Linked_list_t();
    ~Linked_list_t();
    void append(datatype data);
    void push_front(datatype data);
    std::size_t getsize();
    Node<datatype> *search_for(datatype);
    void print();
    void insert_at(int position,datatype this_data);
    private:
    size_t size;
    Node<datatype> *head;
    Node<datatype> *tail;
};
