class Automovil:

    def __init__(self, marca_a ,modelo, velocidad_max):
        self.__marca = marca_a
        self.__modelo = modelo
        self.__velocidad = 0
        self.__color = "Blanco"
        self.__velocidad_maxima = velocidad_max

    def set_color(self, color_nuevo):
        self.__color = color_nuevo
    def get_color(self):
        return self.__color
    
    def acelerar(self, kms):
        velocidad_aux = self.__velocidad  + kms
        if velocidad_aux <= self.__velocidad_maxima: #aca se le pasa una velocidad maxima
            self.__velocidad = velocidad_aux
        else:
            self.__velocidad = self.__velocidad_maxima
    def get_velocidad(self):
        return self.__velocidad



fordka = Automovil("Ford","Ka",170)
print(fordka.get_velocidad())
print(fordka.get_color())
fordka.set_color("Rojo") #asi se cambiaria el color
print(fordka.get_color())
fordka.acelerar(20)#las velocidades se irian sumando
print(fordka.get_velocidad())
fordka.acelerar(60)
print(fordka.get_velocidad())
fordka.acelerar(30)
print(fordka.get_velocidad())
fordka.acelerar(-10)
print(fordka.get_velocidad())

