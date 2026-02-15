# Ejemplo del Mundo Real: Sistema de Reservas de Hotel

class Habitacion:
    """
    Clase que representa una habitación del hotel
    """
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo


class Persona:
    """
    Clase que representa a una persona que hace reservas
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []

    def reservar_habitacion(self, habitacion):
        """
        La persona realiza una reserva
        """
        self.reservas.append(habitacion)
        print(f"{self.nombre} reservó la habitación {habitacion.numero} ({habitacion.tipo}).")

    def mostrar_reservas(self):
        """
        Muestra las habitaciones reservadas por la persona
        """
        print(f"\nReservas de {self.nombre}:")
        for habitacion in self.reservas:
            print(f"- Habitación {habitacion.numero} ({habitacion.tipo})")


# -------------------------
# Uso del programa
# -------------------------

# Crear habitaciones
habitacion1 = Habitacion(101, "Individual")
habitacion2 = Habitacion(202, "Doble")

# Crear persona
persona = Persona("Luis")

# La persona realiza reservas
persona.reservar_habitacion(habitacion1)
persona.reservar_habitacion(habitacion2)

# Mostrar reservas
persona.mostrar_reservas()