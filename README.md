# Sistema de Restaurante

## Estudiante

**Nombre:** Frixon Zambrano

---

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de restaurante utilizando Programación Orientada a Objetos en Python. El programa permite registrar productos, bebidas y clientes mediante un menú interactivo en la consola. Además, utiliza una estructura modular y aplica principios SOLID para mantener un código organizado, reutilizable y fácil de mantener.

---

## Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

---

## Responsabilidad de cada clase

### Producto
Representa la información general de un producto del restaurante, incluyendo su código, nombre, categoría y precio.

### Bebida
Hereda de la clase `Producto` y agrega el atributo correspondiente al tamaño o presentación de la bebida. También reutiliza el método para mostrar la información del producto.

### Cliente
Representa a un cliente del restaurante y almacena su identificación, nombre y correo electrónico.

### Restaurante
Administra el sistema. Se encarga de registrar productos y clientes, validar que no existan códigos o identificaciones repetidas y mostrar la información almacenada.

### main.py
Contiene el menú principal del programa, solicita los datos al usuario y permite interactuar con todas las funciones del sistema.

---

## Relación entre Producto y Bebida

La clase **Bebida** hereda de la clase **Producto**, ya que una bebida también es un producto del restaurante. Gracias a la herencia se reutilizan atributos y métodos, evitando repetir código y facilitando el mantenimiento del programa.

---

## Principios SOLID aplicados

### SRP (Single Responsibility Principle)
Cada clase tiene una única responsabilidad. Producto administra los datos de un producto, Cliente la información del cliente y Restaurante controla la administración del sistema.

### OCP (Open/Closed Principle)
El sistema permite agregar nuevos tipos de productos mediante herencia sin modificar la clase Producto.

### LSP (Liskov Substitution Principle)
Una instancia de la clase Bebida puede utilizarse como si fuera un Producto sin afectar el funcionamiento del programa.

---

## Funcionalidades

- Registrar productos.
- Registrar bebidas.
- Registrar clientes.
- Listar productos registrados.
- Listar clientes registrados.
- Validar códigos de productos duplicados.
- Validar identificaciones de clientes duplicadas.
- Menú interactivo mediante consola.

---

## Requisitos

- Python 3.10 o superior.
- Visual Studio Code (opcional).

---

## Ejecución del proyecto

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Abrir una terminal.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

4. Seleccionar una opción del menú para registrar o consultar la información.

---

## Conclusión

El desarrollo de este proyecto permitió aplicar los conceptos fundamentales de Programación Orientada a Objetos utilizando clases, herencia, encapsulamiento y polimorfismo. Además, la implementación de los principios SOLID contribuyó a obtener un código más organizado, reutilizable y fácil de mantener, demostrando la importancia de una buena estructura para el desarrollo de aplicaciones.
