#include "LinkedList.h"
#include <stdexcept>
#include <iostream>
#include <string>
using std::string;

template <typename datatype>
Linked_list<datatype>::Linked_list() : head(nullptr) {}

template <typename datatype>
Linked_list<datatype>::~Linked_list() {
    Node<datatype> *temp = head;
    while (temp) {
        Node<datatype> *nextNode = temp->next;
        delete temp;
        temp = nextNode;
    }
}

template <typename datatype>
void Linked_list<datatype>::append(datatype data) {
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

template <typename datatype>
void Linked_list<datatype>::push_front(datatype data) {
    Node<datatype> *newNode = new Node<datatype>;
    newNode->data = data;
    newNode->next = head;
    head = newNode;
}

template <typename datatype>
size_t Linked_list<datatype>::getsize() {
    size_t size = 0;
    Node<datatype> *temp = head;
    while (temp->next) {
        temp = temp->next;
        size++;
    }
    return size;
}

template <typename datatype>
void Linked_list<datatype>::print() {
    Node<datatype> *temp = head;
    while (temp) {
        if (temp == head) {
            std::cout << "(head)" <<temp->data << " -> ";
        }
        else {
            std::cout << temp->data << " -> ";
        }
        temp = temp->next;
    }
    std::cout << "null" << std::endl;
}

template <typename datatype>
Node<datatype> *Linked_list<datatype>::search_for(datatype data) {
    Node<datatype> *temp = head;
    while (temp->next) {
        if (temp->data == data) {
            return temp;
        }
        temp = temp->next;
    }
    return nullptr;
}

template <typename datatype>
void Linked_list<datatype>::insert_at(int position, datatype this_data) {
    if (position < 0) {
        throw std::out_of_range("Position out of range");
    }
    if (position == 0) {
        push_front(this_data);
        return;
    }
    Node<datatype> *newNode = new Node<datatype>;
    newNode->data = this_data;
    
    Node<datatype> *temp = head;
    int currentPos = 0;
    
    while (temp != nullptr && currentPos < position - 1) {
        temp = temp->next;
        currentPos++;
    }
    
    if (temp == nullptr) {
        delete newNode;
        throw std::out_of_range("Position out of range");
    }
    
    newNode->next = temp->next;
    temp->next = newNode;
}

template <typename datatype>
Linked_list_t<datatype>::Linked_list_t() : head(nullptr), tail(nullptr), size(0) {}

template <typename datatype>
Linked_list_t<datatype>::~Linked_list_t() {
    Node<datatype> *temp = head;
    while (temp) {
        Node<datatype> *nextNode = temp->next;
        delete temp;
        temp = nextNode;
    }
}

template <typename datatype>
void Linked_list_t<datatype>::append(datatype data) {
    Node<datatype> *newNode = new Node<datatype>;
    newNode->data = data;
    newNode->next = nullptr;
    
    if (head == nullptr) {
        head = newNode;
        tail = newNode;
    } else {
        tail->next = newNode;
        tail = newNode;
    }
    size++;
}

template <typename datatype>
void Linked_list_t<datatype>::push_front(datatype data) {
    Node<datatype> *newNode = new Node<datatype>;
    newNode->data = data;
    newNode->next = head;
    head = newNode;
    
    if (tail == nullptr) {
        tail = newNode;
    }
    size++;
}

template <typename datatype>
size_t Linked_list_t<datatype>::getsize() {
    return size;
}

template <typename datatype>
void Linked_list_t<datatype>::print() {
    Node<datatype> *temp = head;
    while (temp) {
        if (temp == head) {
            std::cout << "(head)" << temp->data << " -> ";
        }
        else if (temp == tail) {
            std::cout << "(tail)" << temp->data << " -> ";
        }
        else {
            std::cout << temp->data << " -> ";
        }
        temp = temp->next;
    }
    std::cout << "null" << std::endl;
}

template <typename datatype>
Node<datatype> *Linked_list_t<datatype>::search_for(datatype data) {
    Node<datatype> *temp = head;
    while (temp) {
        if (temp->data == data) {
            return temp;
        }
        temp = temp->next;
    }
    return nullptr;
}

template <typename datatype>
void Linked_list_t<datatype>::insert_at(int position, datatype this_data) {
    if (position < 0 || position > size) {
        throw std::out_of_range("Position out of range");
    }
    if (position == 0) {
        push_front(this_data);
        return;
    }
    if (position == size) {
        append(this_data);
        return;
    }
    Node<datatype> *newNode = new Node<datatype>;
    newNode->data = this_data;

    Node<datatype> *temp = head;
    for (int i = 0; i < position - 1; i++) {
        temp = temp->next;
    }
    
    newNode->next = temp->next;
    temp->next = newNode;
    
    size++;
}
template class Linked_list<int>;
template class Linked_list<double>;
template class Linked_list<float>;
template class Linked_list<char>;
template class Linked_list<string>;
template class Linked_list<long long>;
template class Linked_list<long double>;

template class Linked_list_t<int>;
template class Linked_list_t<double>;
template class Linked_list_t<float>;
template class Linked_list_t<char>;
template class Linked_list_t<string>;
template class Linked_list_t<long long>;
template class Linked_list_t<long double>;

