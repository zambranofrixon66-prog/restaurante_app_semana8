from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def solicitar_precio() -> float:
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
                continue
            return precio
        except ValueError:
            print("Ingrese un precio válido.")


def mostrar_menu() -> None:
    print("\n===================================")
    print("        SISTEMA DE RESTAURANTE")
    print("===================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-----------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-----------------------------------")
    print("6. Salir")


def main() -> None:
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código del producto: ")
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría: ")
            precio = solicitar_precio()

            producto = Producto(codigo, nombre, categoria, precio)

            if restaurante.registrar_producto(producto):
                print("Producto registrado correctamente.")
            else:
                print("Ya existe un producto con ese código.")

        elif opcion == "2":
            codigo = input("Código de la bebida: ")
            nombre = input("Nombre de la bebida: ")
            categoria = input("Categoría: ")
            precio = solicitar_precio()
            tamano = input("Tamaño o presentación: ")

            bebida = Bebida(
                codigo,
                nombre,
                categoria,
                precio,
                tamano
            )

            if restaurante.registrar_producto(bebida):
                print("Bebida registrada correctamente.")
            else:
                print("Ya existe un producto con ese código.")

        elif opcion == "3":
            identificacion = input("Identificación del cliente: ")
            nombre = input("Nombre del cliente: ")
            correo = input("Correo del cliente: ")

            cliente = Cliente(identificacion, nombre, correo)

            if restaurante.registrar_cliente(cliente):
                print("Cliente registrado correctamente.")
            else:
                print("Ya existe un cliente con esa identificación.")

        elif opcion == "4":
            restaurante.listar_productos()

        elif opcion == "5":
            restaurante.listar_clientes()

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()