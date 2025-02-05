cmake_minimum_required(VERSION 3.30)
project(DataStructures)

set(CMAKE_CXX_STANDARD 20)

include_directories(Array LinkedList Queue Stack Tree)

add_executable(DataStructures main.cpp Array/Array.cpp LinkedList/LinkedList.cpp LinkedList/Node.cpp Queue/Queue.cpp Stack/Stack.cpp Tree/Tree.cpp)
