class ServicioConversor:
    def convertir_a_fahrenheit(self, celsius: float) -> float:
        return (celsius * 9/5) + 32
        
    def obtener_reporte_estado(self, es_congelacion: bool) -> str:
        return "Punto de congelación" if es_congelacion else "Temperatura normal"