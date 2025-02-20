#include "Node.h"
using std::string;
template <typename datatype>
Node<datatype>::Node(datatype store) {
    data = store;
    next = nullptr;
}

template class Node<int>;
template class Node<double>;
template class Node<float>;
template class Node<char>;
template class Node<string>;
template class Node<long long>;
template class Node<long double>;
