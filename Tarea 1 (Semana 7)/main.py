from servicios.gestion_reporte import ServicioGestion

def principal():
    print("=== SISTEMA DE GESTIÓN DE RECURSOS ===\n")
    
    servicio = ServicioGestion()
    
    # 1. Creamos un primer reporte
    print("Acción: Iniciando Reporte de Ventas...")
    resultado = servicio.procesar_reporte("Ventas_Enero.txt", "Ventas totales: $5000")
    print(resultado)
    
    print("\n" + "-"*40 + "\n")
    
    # 2. Creamos otro reporte para ver el ciclo de nuevo
    print("Acción: Iniciando Reporte de Inventario...")
    servicio.procesar_reporte("Inventario_Stock.txt", "Productos en bodega: 120")

if __name__ == "__main__":
    principal()
    print("\n[PROGRAMA]: Finalizado correctamente.")