cmake_minimum_required(VERSION 3.14)
project(MyCppProject)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/release-1.12.1.zip
)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_library(myLib src/muladd.h src/muladd.cpp)
add_executable(myexe src/main.cpp)
target_link_libraries(myexe myLib)

add_executable(my_test tests/test_main.cpp)
target_link_libraries(my_test myLib gtest_main gmock_main)

include(GoogleTest)
gtest_discover_tests(my_test)




