# Dashboard de Gestión de Proyectos POO - V5

Este proyecto consiste en un sistema profesional de gestión, visualización y ejecución de scripts de Python, desarrollado bajo los principios de la **Programación Orientada a Objetos (POO)**. Ha sido diseñado para organizar y ejecutar las tareas del curso de manera jerárquica e interactiva.

## Mejoras de Ingeniería y Solución de Errores

A diferencia de versiones anteriores, esta entrega final incluye soluciones técnicas a problemas comunes de ejecución en terminales de IDEs como VS Code:

* **Aislamiento de Procesos:** Se implementó el uso de `os.system(f'start cmd /k ...')`. Esto soluciona el conflicto donde el proceso hijo bloqueaba la terminal del Dashboard, permitiendo que el menú principal siga funcionando de forma independiente.
* **Manejo de Rutas Robustas:** El sistema convierte todas las direcciones en **rutas absolutas** y las encapsula en comillas. Esto evita fallos al navegar por carpetas con nombres largos o espacios (ej. *"2.1. Programacion tradicional frente a POO"*).
* **Interfaz Autoadaptable:** El diseño visual calcula el ancho máximo de los nombres de los archivos dinámicamente, garantizando que el marco de la interfaz siempre se vea alineado.



## Arquitectura POO y Patrones de Diseño

El software utiliza una arquitectura modular basada en patrones de diseño industriales:

1.  **Patrón Strategy (Estrategia):** Desacopla la lógica de navegación de la ejecución. La clase `EjecutorPython` encapsula la complejidad de lanzar comandos al sistema operativo.
2.  **Patrón Singleton (Instancia Única):** La clase `InterfazConsola` asegura que solo exista un objeto encargado de la gestión de pantalla, optimizando el uso de recursos.
3.  **Abstracción y Encapsulamiento:** Se utilizan clases base abstractas (`ABC`) para definir contratos de comportamiento, mientras que la clase `ScriptPython` encapsula la lógica de lectura y metadatos del archivo.



## Funcionalidades Clave

* **Navegación Multinivel:** Estructura jerárquica: Unidad > Subcarpeta > Script.
* **Lector de Código Integrado:** Visualización previa del contenido con soporte para codificación `UTF-8` (tildes y caracteres especiales).
* **Log de Actividad:** Registro automático en `log_actividad.txt`, documentando fecha y hora de cada ejecución para control de avances.
* **Validación de Entradas:** Sistema que evita cierres inesperados ante ingresos de datos no numéricos.

## Instrucciones de Uso

1.  Coloque el archivo `Dashboard.py` en la carpeta raíz de sus proyectos.
2.  Ejecute el programa:
    ```bash
    python Dashboard.py
    ```
3.  Navegue por el menú usando los números indicados.
4.  Al elegir ejecutar un script (`s`), este se abrirá en una **nueva ventana de comandos**. Al terminar, simplemente cierre esa ventana y presione **Enter** en la terminal principal para volver al menú.


## Autor:
Proyecto elaborado por Gabo.
