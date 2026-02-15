# -------------------------------------------------------
# Programa: Promedio semanal del clima (POO)
# Autor: Gabo
# Descripción:
#   Este programa modela las temperaturas usando una clase
#   que encapsula los datos y métodos necesarios para
#   gestionar la información y calcular el promedio.
# -------------------------------------------------------

class ClimaSemanal:
    def __init__(self):
        self.__temperaturas = []
        self.__dias = ["Lunes", "Martes", "Miércoles", "Jueves",
                       "Viernes", "Sábado", "Domingo"]

    def ingresar_datos(self):
        print("Ingrese las temperaturas de la semana:\n")
        for dia in self.__dias:
            temp = float(input(f"Temperatura del {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    clima = ClimaSemanal()
    clima.ingresar_datos()
    clima.mostrar_promedio()
