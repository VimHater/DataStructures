#include "Headers/Data_Structures.h"
#include "LinkedList/LinkedList.h"
int main() {
    Linked_list_with_tail<int> list;
    while (true) {
        int n;
        std::cin >> n;
        list.push_front(n);
        list.print();
    }
}
