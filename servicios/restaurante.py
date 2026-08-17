from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    def __init__(self) -> None:
        # Listas para almacenar productos y usuarios
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []

        # Diccionario para buscar productos rápidamente por su código
        self.productos_por_codigo: dict[str, Producto] = {}

        # Tupla con información estable del sistema
        self.categorias_permitidas: tuple[str, ...] = (
            "Entrada",
            "Plato fuerte",
            "Postre",
            "Bebida"
        )

        # Conjuntos para evitar duplicados y guardar valores únicos
        self.categorias_registradas: set[str] = set()
        self.identificaciones_usuarios: set[str] = set()

    def normalizar_categoria(self, categoria: str) -> str | None:
        for categoria_permitida in self.categorias_permitidas:
            if categoria.strip().lower() == categoria_permitida.lower():
                return categoria_permitida
        return None

    def registrar_producto(self, producto: Producto) -> bool:
        codigo = producto.codigo.strip().upper()
        categoria = self.normalizar_categoria(producto.categoria)

        if codigo in self.productos_por_codigo or categoria is None:
            return False

        producto.codigo = codigo
        producto.categoria = categoria

        self.productos.append(producto)
        self.productos_por_codigo[codigo] = producto
        self.categorias_registradas.add(categoria)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        return self.productos_por_codigo.get(codigo.strip().upper())

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:
        producto = self.buscar_producto(codigo)
        categoria_normalizada = self.normalizar_categoria(categoria)

        if producto is None or categoria_normalizada is None:
            return False

        producto.nombre = nombre
        producto.categoria = categoria_normalizada
        producto.precio = precio
        self._actualizar_categorias()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)
        del self.productos_por_codigo[producto.codigo]
        self._actualizar_categorias()
        return True

    def listar_productos(self) -> None:
        if not self.productos:
            print("No hay productos registrados.")
            return

        print("\nLISTA DE PRODUCTOS")
        for producto in self.productos:
            print(producto.mostrar_informacion())

    def registrar_usuario(self, usuario: Usuario) -> bool:
        identificacion = usuario.identificacion.strip()

        if identificacion in self.identificaciones_usuarios:
            return False

        usuario.identificacion = identificacion
        self.usuarios.append(usuario)
        self.identificaciones_usuarios.add(identificacion)
        return True

    def listar_usuarios(self) -> None:
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return

        print("\nLISTA DE USUARIOS")
        for usuario in self.usuarios:
            print(usuario.mostrar_informacion())

    def mostrar_categorias_permitidas(self) -> None:
        print("Categorías permitidas:")
        for categoria in self.categorias_permitidas:
            print(f"- {categoria}")

    def mostrar_categorias(self) -> None:
        if not self.categorias_registradas:
            print("No hay categorías registradas.")
            return

        print("\nCATEGORÍAS REGISTRADAS")
        for categoria in sorted(self.categorias_registradas):
            print(f"- {categoria}")

    def _actualizar_categorias(self) -> None:
        self.categorias_registradas = {
            producto.categoria for producto in self.productos
        }