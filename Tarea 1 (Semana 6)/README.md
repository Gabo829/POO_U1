# Tarea: Clases, objetos, herencia, encapsulamiento y polimorfismo
Este proyecto ha sido desarrollado como parte del aprendizaje de los pilares de la Programación Orientada a Objetos (POO) en Python. La aplicación simula un sistema de gestión bibliográfica que permite administrar recursos y libros de manera eficiente. El enfoque principal es demostrar cómo la organización modular del código y el uso de clases permiten crear software escalable, seguro y fácil de mantener, siguiendo los estándares de la industria y las mejores prácticas de desarrollo.

# Objetivos de la Actividad
- **Herencia:** Implementación de una jerarquía de clases donde `Libro` hereda atributos y métodos de la clase base `Recurso`.
- **Encapsulación:** Protección del estado interno de los objetos mediante el uso de atributos privados (`__estado`).
- **Polimorfismo:** Sobrescritura de métodos para que objetos de distintas clases respondan de forma específica al mismo llamado.
- **Estructura Modular:** Separación de responsabilidades en paquetes de `modelos` y `servicios`.

# Estructura del Proyecto
El programa se organiza de acuerdo a la arquitectura trabajada en clase para garantizar el orden y la claridad:

<img width="531" height="252" alt="image" src="https://github.com/user-attachments/assets/3790fe62-f7a2-4b10-9755-bc2d6640306b" />

# Conceptos de POO Aplicados
- **Herencia:** La clase `Libro` extiende la funcionalidad de `Recurso`, reutilizando código y añadiendo especialización (como el ISBN).
- **Encapsulación:** Se restringió el acceso directo al atributo `__estado`. Para interactuar con él, se utilizan métodos públicos, asegurando que el flujo de datos sea controlado.
- **Polimorfismo:** El método `obtener_info()` se comporta de manera distinta dependiendo de si el objeto es un recurso genérico o un libro, permitiendo flexibilidad en la salida de datos.

# Conlusión
La implementación de este proyecto permitió consolidar el uso de los pilares de la POO en un entorno modular. La aplicación de la **herencia** facilitó la reutilización de código, mientras que la **encapsulación** aseguró la integridad de los datos internos de las clases. Finalmente, el uso de **polimorfismo** demostró cómo una arquitectura bien diseñada permite manejar distintos tipos de objetos de manera uniforme, mejorando la escalabilidad del sistema.

# Autor
Proyecto elaborado por Gabo.
