palabra = input(": Ingresar una palabra")

def contar_vocales(palabra):
    
    vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    contador = 0
    
    for caracter in palabra:
        
        if caracter in vocales:
        
            contador += 1
    
    
    return contador



numero_de_vocales = contar_vocales(palabra)
print(f"El número de vocales en '{palabra}' es: {numero_de_vocales}")







