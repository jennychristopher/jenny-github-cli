#include <iostream>

int add(int a, int b) {
    return a + b;
}

int multiply(int a, int b) {
    return a * b;
}

int main() {
    std::cout << "Add(2, 3) = " << add(2, 3) << std::endl;
    std::cout << "Multiply(2, 3) = " << multiply(2, 3) << std::endl;
    return 0;
}

