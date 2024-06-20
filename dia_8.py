import random
import string

mayusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = string.punctuation

todos_los_caracteres = mayusculas + minusculas + numeros + simbolos

longitud = int(input("Elige la longitud de la contraseña (entre 8 y 16 caracteres): "))
while longitud < 8 or longitud > 16:
    longitud = int(input("Longitud invalida. Favor ingrese una longitud de 8 a 16 caracteres: "))


contraseña = [
    random.choice(mayusculas),
    random.choice(minusculas),
    random.choice(numeros),
    random.choice(simbolos),
]

contraseña += random.choices(todos_los_caracteres, k = longitud - 4)

random.shuffle(contraseña)

contraseña = ''.join(contraseña)

print(f"Tu contraseña segura es: {contraseña}")
