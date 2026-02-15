from modelos.reporte import Reporte

class ServicioGestion:
    def procesar_reporte(self, nombre: str, datos: str):
        # Aquí se instancia el modelo (llama al __init__)
        nuevo_reporte = Reporte(nombre, datos)
        print(f"--- Procesando información en el servicio... ---")
        
        # Al terminar esta función, la variable 'nuevo_reporte' deja de existir
        # por lo cual el Destructor (__del__) se activará automáticamente.
        return f"Reporte {nombre} procesado con éxito."