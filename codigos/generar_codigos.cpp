#include <iostream>
#include <string>
#include <set>
#include <cstdlib>
#include <ctime>

// Función para generar un código aleatorio
std::string generarCodigo() {
    std::string codigo = "XV-";
    
    // Generar 5 números aleatorios
    for (int i = 0; i < 5; i++) {
        codigo += std::to_string(rand() % 10);
    }
    
    // Generar 2 letras aleatorias (puedes personalizar esta parte)
    for (int i = 0; i < 2; i++) {
        char letra = 'A' + (rand() % 26);
        codigo += letra;
    }
    
    return codigo;
}

int main() {
    // Inicializar la semilla para generar números aleatorios
    srand(time(0));
    
    // Crear un conjunto para almacenar códigos únicos
    std::set<std::string> codigos;
    
    // Generar 1000 códigos únicos
    while (codigos.size() < 1000) {
        std::string codigo = generarCodigo();
        
        // Verificar si el código ya existe en el conjunto
        if (codigos.find(codigo) == codigos.end()) {
            codigos.insert(codigo);
        }
    }
    
    // Imprimir los códigos generados
    for (const std::string& codigo : codigos) {
        std::cout << codigo << std::endl;
    }
    
    return 0;
}
