#include <iostream>

int main() {
    int num1, num2, suma;

    std::cout << "Ingrese el primer número: ";
    std::cin >> num1;

    std::cout << "Ingrese el segundo número: ";
    std::cin >> num2;

    suma = num1 + num2;

    std::cout << "La suma de " << num1 << " + " << num2 << " es " << suma << std::endl;

   
    return 0;
}
