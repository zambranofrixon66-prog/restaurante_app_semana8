# Sistema de Restaurante

## Estudiante

**Nombre:** Frixon Zambrano

---

## Descripción del proyecto

Este proyecto presenta un sistema básico para administrar los productos y usuarios de un restaurante. Fue desarrollado con Programación Orientada a Objetos en Python y funciona mediante un menú interactivo en la consola.

El sistema permite registrar, buscar, actualizar, eliminar y listar productos. También permite registrar usuarios, consultar la lista de usuarios y mostrar las categorías únicas utilizadas.

---

## Estructura del proyecto

```text
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   ├── bebida.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
├── .gitignore
└── README.md
```

Los archivos `bebida.py` y `cliente.py` se conservan como parte del trabajo realizado en las semanas anteriores.

---

## Responsabilidad de los componentes

### Producto

Representa un producto del restaurante y almacena su código, nombre, categoría y precio.

### Usuario

Representa a una persona registrada en el sistema. Guarda su identificación, nombre y correo electrónico.

### Restaurante

Administra las colecciones de productos y usuarios. Contiene las operaciones de registro, búsqueda, actualización, eliminación y listado.

### main.py

Es el punto de inicio del programa. Presenta el menú, solicita los datos y llama a los métodos de la clase `Restaurante`.

---

## Estructuras de datos utilizadas

### Lista

Se utilizan listas para almacenar los productos y usuarios porque permiten agregar y eliminar objetos durante la ejecución del programa.

### Tupla

Se utiliza una tupla para guardar las categorías permitidas: entrada, plato fuerte, postre y bebida. Esta información se mantiene estable durante la ejecución.

### Diccionario

Se utiliza un diccionario para relacionar el código de cada producto con su objeto. Esto permite buscar productos rápidamente mediante su código.

### Conjunto

Se utilizan conjuntos para almacenar categorías únicas y evitar identificaciones de usuarios duplicadas.

---

## Funcionalidades

- Registrar productos.
- Buscar productos mediante su código.
- Actualizar productos.
- Eliminar productos.
- Listar los productos registrados.
- Registrar usuarios.
- Listar los usuarios registrados.
- Evitar códigos de productos duplicados.
- Evitar identificaciones de usuarios duplicadas.
- Mostrar las categorías únicas de los productos.
- Validar que los campos no estén vacíos.
- Validar que el precio sea numérico y mayor que cero.
- Mostrar un menú interactivo en la consola.

---

## Menú del sistema

```text
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
6. Registrar usuario
7. Listar usuarios
8. Mostrar categorías
9. Salir
```

---

## Requisitos

- Python 3.10 o superior.
- Visual Studio Code o cualquier editor compatible con Python.

---

## Ejecución del proyecto

1. Abrir la carpeta del proyecto.
2. Abrir una terminal en la carpeta principal.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

4. Seleccionar una opción del menú y seguir las indicaciones mostradas en la consola.

---

## Conclusión

Esta actividad permitió mejorar el sistema del restaurante mediante el uso de listas, tuplas, diccionarios y conjuntos. Cada estructura cumple una función específica y ayuda a organizar la información de manera sencilla. Además, la separación entre modelos, servicios y el archivo principal mantiene el código ordenado y facilita su mantenimiento.