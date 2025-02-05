#pragma once
template <typename datatype>
class Node {
public:
    datatype data;
    Node *next;
    Node(datatype val);
};

