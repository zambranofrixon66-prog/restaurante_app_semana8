from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente


class Restaurante:
    def __init__(self) -> None:
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        for producto_guardado in self.productos:
            if producto_guardado.codigo == producto.codigo:
                return False

        self.productos.append(producto)
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        for cliente_guardado in self.clientes:
            if cliente_guardado.identificacion == cliente.identificacion:
                return False

        self.clientes.append(cliente)
        return True

    def listar_productos(self) -> None:
        if not self.productos:
            print("No hay productos registrados.")
            return

        print("\nLISTA DE PRODUCTOS")
        for producto in self.productos:
            print(producto.mostrar_informacion())

    def listar_clientes(self) -> None:
        if not self.clientes:
            print("No hay clientes registrados.")
            return

        print("\nLISTA DE CLIENTES")
        for cliente in self.clientes:
            print(cliente.mostrar_informacion())