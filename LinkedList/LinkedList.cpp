#include "LinkedList.h"

#include <iostream>
#include <string>
using std::string;
template <typename datatype>
Linked_list<datatype>::Linked_list() : head(nullptr) {}

template <typename datatype>
Linked_list<datatype>::~Linked_list() {
    node<datatype> *current = head;
    while (current != nullptr) {
        node<datatype> *newnode = current->next;
        delete[] current;
        current = newnode;
    }
}

template <typename datatype>
void Linked_list<datatype>::print() {
    node<datatype> *current = head;
    while (current != nullptr) {
        node<datatype> *newnode = current->next;
        std::cout << current->data << ", " << std::flush;
        current = newnode;
    }
}

template <typename datatype>
void Linked_list<datatype>::push_back(datatype data) {}

template <typename datatype>
void Linked_list<datatype>::push_front(datatype data) {
    node<datatype> newnode;
    newnode.data = data;
    node<datatype> *current_head = head;
    newnode.next = head;
    head = &newnode;
}

template <typename datatype>
node<datatype> *Linked_list<datatype>::search_for(datatype data) {
    node<datatype> *current = head;
    node<datatype> *pos;
    while (current != nullptr) {
        pos = current;
        node<datatype> *newnode = current->next;
        if (current->data == data) {
            return pos;
        }
    }
    return nullptr;
}
template <typename datatype>
void Linked_list<datatype>::insert_at(int position, datatype this_data) {}
template <typename datatype>
std::size_t Linked_list<datatype>::getsize() {
    return size;
}
template class Linked_list<int>;
template class Linked_list<double>;
template class Linked_list<float>;
template class Linked_list<char>;
template class Linked_list<string>;
template class Linked_list<long long>;
template class Linked_list<long double>;
