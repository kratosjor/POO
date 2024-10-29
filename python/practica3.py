"""Con la ayuda de la IA, desarrollar en Python, Java y C# los siguientes ejercicios:
Ejercicio nº 1 (Creando un Perro Virtual):
Crea una clase llamada "
Perro" que tenga los siguientes atributos: nombre, raza, edad.
Define los siguientes métodos:
• ladrar(): Imprime un mensaje indicando que el perro está ladrando.
• jugar(): Imprime un mensaje indicando que el perro quiere jugar.
• comer(): Imprime un mensaje indicando que el perro está comiendo.
Crea un objeto de la clase Perro y utiliza sus métodos.
"""
class Perro:
    def __init__(self, nombre, raza, edad):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad

    def ladrar(self):
        return f"{self.__nombre} está ladrando"

    def jugar(self):
        return f"{self.__nombre} quiere jugar"

    def comer(self):
        return f"{self.__nombre} está comiendo"
    
    def __str__(self):
        return f"Perro(nombre={self.__nombre}, raza={self.__raza}, edad={self.__edad} años)"

        
mi_perro = Perro("Juan Carlos","Pastor Aleman", 5)
print(mi_perro.ladrar())
print(mi_perro.jugar())
print(mi_perro.comer())
print("##########################################################")
"""
-Ejercicio nº 2 (Diseñando un Coche):
Crea una clase llamada "
Coche" que tenga los siguientes atributos: marca, modelo, año, color,
velocidad_maxima.
Define los siguientes métodos:
• acelerar(cantidad): Incrementa la velocidad actual del coche en la cantidad indicada.
• frenar(): Establece la velocidad actual del coche a 0.
• mostrar_info(): Imprime la información del coche en pantalla.
Crea un objeto de la clase Coche y utiliza sus métodos para simular un viaje.
"""
class Coche:
    def __init__(self, marca, modelo, año, color, velocidad_maxima):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__color = color
        self.__velocidad_maxima = velocidad_maxima
        self.__velocidad_actual = 0

    def acelerar(self, cantidad):
        if self.__velocidad_actual + cantidad > self.__velocidad_maxima:
            self.__velocidad_actual = self.__velocidad_maxima
            print(f"¡Has alcanzado la velocidad máxima de {self.__velocidad_maxima} km/h!")
        else:
            self.__velocidad_actual += cantidad
            print(f"Velocidad actual: {self.__velocidad_actual} km/h")

    def frenar(self):
        self.__velocidad_actual = 0
        print("El coche se ha detenido.")

    def mostrar_info(self):
        print(f"Coche: {self.__marca} {self.__modelo} ({self.__año}), Color: {self.__color}, Velocidad máxima: {self.__velocidad_maxima} km/h")
        print(f"Velocidad actual: {self.__velocidad_actual} km/h")

    # Métodos getter (accesores)
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_año(self):
        return self.__año

    def get_color(self):
        return self.__color

    def get_velocidad_maxima(self):
        return self.__velocidad_maxima

    def get_velocidad_actual(self):
        return self.__velocidad_actual

# Crear una instancia de la clase Coche
mi_coche = Coche("Toyota", "Corolla", 2020, "Rojo", 180)

# Simular un viaje
mi_coche.mostrar_info()
mi_coche.acelerar(60)
mi_coche.acelerar(80)
mi_coche.acelerar(50)  # Alcanzará la velocidad máxima
mi_coche.frenar()
mi_coche.mostrar_info()
print("##########################################################")
"""
-Ejercicio nº 3 (Gestionando una Cuenta Bancaria):
Crea una clase llamada "
CuentaBancaria" que tenga los siguientes atributos: titular, número_cuenta,
saldo.
Define los siguientes métodos:
• ingresar_dinero(cantidad): Incrementa el saldo de la cuenta en la cantidad indicada.
• retirar_dinero(cantidad): Decrementa el saldo de la cuenta en la cantidad indicada, siempre y cuando haya suficiente saldo.
• mostrar_saldo(): Imprime el saldo actual de la cuenta.
"""
class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo):
        self.__titular = titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo

    def ingresar_dinero(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Has ingresado {cantidad}. Tu saldo actual es {self.__saldo}."
        else:
            return "La cantidad a ingresar debe ser positiva."

    def retirar_dinero(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Has retirado {cantidad}. Tu saldo actual es {self.__saldo}."
        else:
            return "No tienes suficiente saldo o la cantidad no es válida."

    def mostrar_saldo(self):
        return f"Tu saldo actual es {self.__saldo}."

# Crear una instancia de la clase CuentaBancaria
mi_cuenta = CuentaBancaria("Jordan Espinoza", "178988779-8", 1500000)

# Ejemplos de uso
print(mi_cuenta.mostrar_saldo())         # Mostrar saldo inicial
print(mi_cuenta.ingresar_dinero(500000)) # Ingresar dinero
print(mi_cuenta.retirar_dinero(200000))  # Retirar dinero
print(mi_cuenta.mostrar_saldo())         # Mostrar saldo final
