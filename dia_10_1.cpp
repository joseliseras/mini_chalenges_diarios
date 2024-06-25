#include <iostream>
#include <string>
#include <algorithm>

bool esPalindromo(const std::string& texto) {
    std::string textoLimpio;
    
    // Eliminar espacios y convertir a minúsculas
    for (char c : texto) {
        if (std::isalnum(c)) {
            textoLimpio += std::tolower(c);
        }
    }
    
    // Comparar la cadena con su reverso
    return textoLimpio == std::string(textoLimpio.rbegin(), textoLimpio.rend());
}

int main() {
    std::string entrada;
    
    std::cout << "Ingrese una cadena para verificar si es un palíndromo: ";
    std::getline(std::cin, entrada);
    
    if (esPalindromo(entrada)) {
        std::cout << "La cadena es un palíndromo." << std::endl;
    } else {
        std::cout << "La cadena no es un palíndromo." << std::endl;
    }
    
    return 0;
}
