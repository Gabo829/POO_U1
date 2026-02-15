# Proyecto: Constructores y Destructores en Python
Este programa es un **Sistema de Gestión de Reportes** desarrollado bajo el paradigma de Programación Orientada a Objetos (POO). El objetivo es demostrar el manejo del ciclo de vida de un objeto en Python, utilizando:
- **Constructores (`__init__`)**: Para la inicialización de estado y recursos.
- **Destructores (`__del__`)**: Para la limpieza y liberación de recursos.

# Estructura del Proyecto
El proyecto sigue una arquitectura modular (Modelos/Servicios) para una mejor organización del código:

<img width="492" height="256" alt="image" src="https://github.com/user-attachments/assets/cca465c7-db25-4197-9113-44e38314a51e" />


# Implementación de Conceptos Clave

### 1. Constructor (`__init__`)
Ubicado en `modelos/reporte.py`. Se activa automáticamente al instanciar un objeto. En este proyecto, se encarga de:
- Inicializar el nombre del reporte.
- Establecer el estado inicial del recurso como "Abierto".
- Simular la carga de datos obligatorios.

### 2. Destructor (`__del__`)
Ubicado en `modelos/reporte.py`. Se activa cuando el objeto ya no es referenciado o el programa termina. Su función es:
- Simular el cierre seguro de un archivo o conexión.
- Garantizar que no queden recursos "colgados" en memoria.

# Cómo Ejecutar el Programa
1. Abra una terminal en la carpeta raíz del proyecto.
2. Ejecute el siguiente comando:
   ```bash
   python main.py

# Autor
Proyecto elaborado por Gabo.
