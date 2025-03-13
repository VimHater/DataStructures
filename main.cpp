#include "Headers/Data_Structures.h"
#include "LinkedList/LinkedList.h"
int main() {
    Linked_list_t<std::string> list;
    while (true) {
        std::cout << "insert to list:";
        std::string n;
        std::cin >> n;
        list.append(n);
        list.print();
    }
}

