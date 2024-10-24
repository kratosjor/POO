# Solicita la edad al usuario
edad = input("Por favor, ingresa tu edad: ")

# Convierte el valor ingresado a un número entero
try:
    edad = int(edad)
    
    # Verifica en qué rango de edad se encuentra el usuario
    if edad < 13:
        print("Eres un niño.")
    elif 13 <= edad <= 17:
        print("Eres un adolescente.")
    elif 18 <= edad <= 64:
        print("Eres un adulto.")
    elif edad >= 65:
        print("Eres un adulto mayor.")
    else:
        print("Por favor, ingresa una edad válida.")
except ValueError:
    print("Por favor, ingresa un número válido.")
