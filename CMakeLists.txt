cmake_minimum_required(VERSION 3.30)
project(DataStructures)

set(CMAKE_CXX_STANDARD 20)

target_include_directories(Array LinkedList Queue Stack Tree Headers)

add_executable(DataStructures
        Headers/Data_Structures.h

        main.cpp
        Array/Array.h
        Array/Array.cpp

        Array/Array2D.h
        Array/Array2D.cpp

        LinkedList/LinkedList.h
        LinkedList/LinkedList.cpp

        Queue/Queue.h
        Queue/Queue.cpp

        Stack/Stack.h
        Stack/Stack.cpp

        Tree/Tree.h
        Tree/Tree.cpp

)
