#include "LinkedList.h"
#include "Node.h"
#include <string>
using std::string;

template <typename datatype>
LinkedList<datatype>::LinkedList() : head(nullptr){};

template <typename datatype>
LinkedList<datatype>::~LinkedList() {
    
}

template <typename datatype>
void LinkedList<datatype>::push_back() {
    
}

template <typename datatype>
void LinkedList<datatype>::insert_at(int index) {
    
}

template <typename datatype>
void LinkedList<datatype>::delete_node_at(int index) {
    
}

template <typename datatype>
void LinkedList<datatype>::delete_first() {

}

template <typename datatype>
void LinkedList<datatype>::delete_last() {
    
}
template <typename datatype>
void LinkedList<datatype>::print() {
    
}


template class LinkedList<int>;
template class LinkedList<double>;
template class LinkedList<float>;
template class LinkedList<char>;
template class LinkedList<string>;
template class LinkedList<long long>;
template class LinkedList<long double>;