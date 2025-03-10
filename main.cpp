#include "Headers/Data_Structures.h"
int main() {
    Linked_list<int> list;
    while (true) {
        int n;
        std::cin >> n;
        list.append(n);
        list.print();
    }
}
