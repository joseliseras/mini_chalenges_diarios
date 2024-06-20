import random

opciones = ['piedra', 'papel', 'tijeras']
eleccion_computadora = random.choice(opciones)

eleccion_usuario = input("Elige piedra, papel o tijeras: ").lower()
while eleccion_usuario not in opciones:
    eleccion_usuario = input("Opción inválida. Por favor elige piedra, papel o tijeras: ").lower()

print(f"La computadora eligió: {eleccion_computadora}")

if eleccion_usuario == eleccion_computadora:
    print("¡Es un empate!")
elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijeras') or \
     (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
     (eleccion_usuario == 'tijeras' and eleccion_computadora == 'papel'):
    print("¡Ganaste!")
else:
    print("¡Perdiste!")
