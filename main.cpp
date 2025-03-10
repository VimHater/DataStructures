#include "Headers/Data_Structures.h"
#include "LinkedList/LinkedList.h"
int main() {
    Linked_list_t<std::string> list;
    while (true) {
        std::string n;
        std::cin >> n;
        list.push_front(n);
        list.print();
    }
}
