#include "LinkedList.h"
#include <stdexcept>
#define tem template<typename datatype>
#include <iostream>
#include <string>
using std::string;
tem
Linked_list<datatype>::Linked_list() : head(nullptr) {}

tem
Linked_list<datatype>::~Linked_list() {
    Node<datatype> *temp = head;
    while (temp) {
        Node<datatype> *nextNode = temp->next;
        delete temp;
        temp = nextNode;
    }
}

tem
void Linked_list<datatype>::append(datatype data) {
    Node<datatype> *newNode = new Node<datatype>;
    newNode->data = data;
    newNode->next = nullptr;
    if(head == nullptr) {
        head = newNode;
        return;
    }
    
    Node<datatype> *temp = head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = newNode;
}

tem
void Linked_list<datatype>::push_front(datatype data) {
    Node<datatype> *newNode = new Node<datatype>;
    newNode->data = data;
    newNode->next = head;
    head = newNode;
}

tem
size_t Linked_list<datatype>::getsize() {
    size_t size = 0;
    Node<datatype> *temp = head;
    while (temp->next) {
        temp = temp->next;
        size++;
    }
    return size;
}
tem
void Linked_list<datatype>::print() {
    Node<datatype> *temp = head;
    while (temp) {
        std::cout << temp->data << " -> ";
        temp = temp->next;
    }
    std::cout << "null" << std::endl;
}
tem
Node<datatype> *Linked_list<datatype>::search_for(datatype data) {
    Node<datatype> *temp = head;
    while (temp->next) {
        if(temp->data == data) {
            return temp;
        }
        temp = temp->next;
    }
    return nullptr;
}

tem
void Linked_list<datatype>::insert_at(int position, datatype this_data) {
    if (position < 0) {
        std::out_of_range("out of range");
    }
}

tem
Linked_list_with_tail<datatype>::Linked_list_with_tail() : head(nullptr) , tail(nullptr), size(0){}

tem
Linked_list_with_tail<datatype>::~Linked_list_with_tail() {
    if(size == 0) {
        delete head;
        delete tail;
    }
    else {
        Node<datatype> *front = head;
        Node<datatype> *back = tail;
        while (front && back && front != back->next) {
            Node<datatype> *nextFront = front->next;
            Node<datatype> *prevBack = back->prev;
            if (front == back) {
                delete front;
                break;
            }

            delete front;
            delete back;
            
            front = nextFront;
            back = prevBack;
        }

        head = tail = nullptr;
    }
}

tem
void Linked_list_with_tail<datatype>::insert_at(int position, datatype this_data) {

}

tem
void Linked_list_with_tail<datatype>::push_front(datatype data) {
    Node<datatype> *newNode = new Node<datatype>;
    newNode->data = data;
    newNode->next = head;
    head = newNode;
    size++;
}

tem
void Linked_list_with_tail<datatype>::append(datatype data) {
    Node<datatype> *newNode = new Node<datatype>;
    newNode->data = data;
    newNode->next = tail;
    tail = newNode;
    size++;
}

tem
void Linked_list_with_tail<datatype>::print() {
    Node<datatype> *temp = head;
    while (temp) {
        std::cout << temp->data << " <-> ";
        temp = temp->next;
    }
    std::cout << "null" << std::endl;
}

template class Linked_list<int>;
template class Linked_list<double>;
template class Linked_list<float>;
template class Linked_list<char>;
template class Linked_list<string>;
template class Linked_list<long long>;
template class Linked_list<long double>;



template class Linked_list_with_tail<int>;
template class Linked_list_with_tail<double>;
template class Linked_list_with_tail<float>;
template class Linked_list_with_tail<char>;
template class Linked_list_with_tail<string>;
template class Linked_list_with_tail<long long>;
template class Linked_list_with_tail<long double>;
