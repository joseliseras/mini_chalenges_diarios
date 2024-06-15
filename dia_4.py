lista = []

while True:
    try:
        valor = int(input("Ingresar valor (Presione una letra para finalizar): "))
        lista.append(valor)
    except ValueError:
        break

print("Número de elementos en la lista:", len(lista))

# algoritmo de burbuja
n = len(lista)
for i in range(n):
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]


print("Lista ordenada:", lista)
