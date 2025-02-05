#include "Node.h"
#include <string>
template class Node<int>;
template class Node<double>;
template class Node<std::string>;
template class Node<char>;
template class Node<long double>;
template class Node<long long>;
template class Node<unsigned>;
template class Node<unsigned long long>;


template<typename datatype>
Node<datatype>::Node(datatype val) {
    data = val;
    next = nullptr;
}