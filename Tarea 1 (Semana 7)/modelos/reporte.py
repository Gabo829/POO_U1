class Reporte:
    def __init__(self, nombre_archivo: str, contenido_inicial: str):
        """
        CONSTRUCTOR: Inicializa los atributos del objeto.
        Se ejecuta automáticamente cuando creamos la instancia.
        """
        self.nombre_archivo: str = nombre_archivo
        self.estado: str = "Abierto"
        # Simulamos la apertura de un recurso
        print(f"[CONSTRUCTOR]: Creando el reporte '{self.nombre_archivo}'.")
        print(f"[SISTEMA]: Inicializando datos: {contenido_inicial}")

    def __del__(self):
        """
        DESTRUCTOR: Realiza la limpieza antes de que el objeto sea destruido.
        Se ejecuta cuando el objeto ya no tiene referencias o el programa termina.
        """
        self.estado = "Cerrado"
        print(f"\n[DESTRUCTOR]: Liberando recursos del reporte '{self.nombre_archivo}'.")
        print(f"[SISTEMA]: Conexión al archivo finalizada y cambios guardados.")