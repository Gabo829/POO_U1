from modelos.temperatura import Temperatura
from servicios.conversor import ServicioConversor

def principal():
    print("=== SISTEMA DE TEMPERATURA ===")
    
    # Entrada de datos
    nombre = input("Nombre del técnico: ")
    grado = float(input("Ingrese grados Celsius: "))
    
    # Creamos el objeto modelo
    medicion = Temperatura(valor_celsius=grado, tecnico_nombre=nombre)
    servicio = ServicioConversor()
    
    # Procesamiento
    fahrenheit = servicio.convertir_a_fahrenheit(medicion.valor_celsius)
    estado = servicio.obtener_reporte_estado(medicion.es_congelacion())
    
    # Salida 
    print(f"\nREPORTE: {medicion.tecnico_nombre}")
    print(f"Resultado: {fahrenheit:.2f} °F")
    print(f"Estado: {estado}")

if __name__ == "__main__":

    principal()