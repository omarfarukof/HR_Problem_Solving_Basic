#include "bits/stdc++.h"

int solveMeFirst(int a, int b) {
    return a + b;
}

int main() {
    int num1, num2;
    int sum;
    std::cin >> num1 >> num2;
    sum = solveMeFirst(num1, num2);
    std::cout << sum;
    return 0;
}