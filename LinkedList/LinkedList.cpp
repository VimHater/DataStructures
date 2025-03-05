#include "LinkedList.h"

#include <string>
using std::string;
template <typename datatype>
Linked_list<datatype>::Linked_list() : head(nullptr) {}

template <typename datatype>
Linked_list<datatype>::~Linked_list() {}

template <typename datatype>
void Linked_list<datatype>::print() {}

template <typename datatype>
void Linked_list<datatype>::push_back(datatype data) {}

template <typename datatype>
void Linked_list<datatype>::push_front(datatype data) {}

template <typename datatype>
node<datatype> *Linked_list<datatype>::search_for(datatype data) {}

template <typename datatype>
void Linked_list<datatype>::insert_at(int position, datatype this_data) {}

template class Linked_list<int>;
template class Linked_list<double>;
template class Linked_list<float>;
template class Linked_list<char>;
template class Linked_list<string>;
template class Linked_list<long long>;
template class Linked_list<long double>;
