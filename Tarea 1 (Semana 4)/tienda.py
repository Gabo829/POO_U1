# Ejemplo del Mundo Real: Sistema de Tienda

class Producto:
    """
    Clase que representa un producto en la tienda
    """
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        """
        Muestra la información del producto
        """
        print(f"Producto: {self.nombre} - Precio: ${self.precio}")


class Carrito:
    """
    Clase que representa el carrito de compras
    """
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        """
        Agrega un producto al carrito
        """
        self.productos.append(producto)
        print(f"{producto.nombre} agregado al carrito.")

    def calcular_total(self):
        """
        Calcula el total de la compra
        """
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total


class Cliente:
    """
    Clase que representa a un cliente de la tienda
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = Carrito()

    def comprar(self):
        """
        Muestra el total de la compra del cliente
        """
        total = self.carrito.calcular_total()
        print(f"{self.nombre}, el total de tu compra es: ${total}")


# -------------------------
# Uso del sistema (objetos)
# -------------------------

# Creación de productos
producto1 = Producto("Laptop", 1200)
producto2 = Producto("Mouse", 25)
producto3 = Producto("Teclado", 45)

# Creación de cliente
cliente = Cliente("Carlos")

# Cliente agrega productos al carrito
cliente.carrito.agregar_producto(producto1)
cliente.carrito.agregar_producto(producto2)
cliente.carrito.agregar_producto(producto3)

# Cliente realiza la compra
cliente.comprar()