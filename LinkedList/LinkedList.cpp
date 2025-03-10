#include "LinkedList.h"

#include <stdexcept>
#define tem template <typename datatype>
#include <iostream>
#include <string>
using std::string;
tem Linked_list<datatype>::Linked_list() : head(nullptr) {}

tem Linked_list<datatype>::~Linked_list() {
    Node<datatype> *temp = head;
    while (temp) {
        Node<datatype> *nextNode = temp->next;
        delete temp;
        temp = nextNode;
    }
}

tem void Linked_list<datatype>::append(datatype data) {
    Node<datatype> *newNode = new Node<datatype>;
    newNode->data = data;
    newNode->next = nullptr;
    if (head == nullptr) {
        head = newNode;
        return;
    }

    Node<datatype> *temp = head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = newNode;
}

tem void Linked_list<datatype>::push_front(datatype data) {
    Node<datatype> *newNode = new Node<datatype>;
    newNode->data = data;
    newNode->next = head;
    head = newNode;
}

tem size_t Linked_list<datatype>::getsize() {
    size_t size = 0;
    Node<datatype> *temp = head;
    while (temp->next) {
        temp = temp->next;
        size++;
    }
    return size;
}
tem void Linked_list<datatype>::print() {
    Node<datatype> *temp = head;
    while (temp) {
        std::cout << temp->data << " -> ";
        temp = temp->next;
    }
    std::cout << "null" << std::endl;
}
tem Node<datatype> *Linked_list<datatype>::search_for(datatype data) {
    Node<datatype> *temp = head;
    while (temp->next) {
        if (temp->data == data) {
            return temp;
        }
        temp = temp->next;
    }
    return nullptr;
}

tem void Linked_list<datatype>::insert_at(int position, datatype this_data) {
    if (position < 0) {
        std::out_of_range("out of range");
    }
}

template class Linked_list<int>;
template class Linked_list<double>;
template class Linked_list<float>;
template class Linked_list<char>;
template class Linked_list<string>;
template class Linked_list<long long>;
template class Linked_list<long double>;

