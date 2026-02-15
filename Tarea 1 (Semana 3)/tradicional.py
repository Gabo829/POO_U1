# -----------------------------------------------
# Programa: Promedio semanal del clima (Tradicional)
# Autor: Gabo
# Descripción:
#   Este programa solicita al usuario las temperaturas
#   diarias de una semana y calcula el promedio usando
#   funciones (programación tradicional).
# -----------------------------------------------

def ingresar_temperaturas():
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("Ingrese las temperaturas de la semana:\n")

    for dia in dias:
        temp = float(input(f"Temperatura del {dia}: "))
        temperaturas.append(temp)

    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
