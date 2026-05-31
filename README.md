# 📦 Gestor de Inventario y Ventas - Tienda Tech

Sistema interactivo de gestión de inventario y control de caja desarrollado en Python. Implementa lógica de bucles controlados, validación de stock en tiempo real, persistencia en memoria mediante colecciones dinámicas y normalización estricta de entradas (Data Cleaning).

Este proyecto representa una solución integral para la gestión de jornadas comerciales, garantizando la integridad de los datos frente a errores de ingreso por parte del usuario y ofreciendo un reporte financiero detallado al finalizar las operaciones.

---

## 🚀 Funcionalidades Principales

* **Data Cleaning y Normalización**: Sanitización automática de espacios en blanco y formateo de texto (`.strip()`, `.title()`, `.lower()`) para homogeneizar los registros de usuarios y comandos.
* **Blindaje contra Excepciones (Crash-Proof)**: Validación de tipos mediante métodos de cadena (`.isdigit()`) que previene errores de ejecución (`ValueError`) si el usuario ingresa caracteres alfabéticos en campos numéricos.
* **Control de Stock en Tiempo Real**: Validación lógica de existencias que impide transacciones superiores al stock físico disponible.
* **Persistencia Indexada (Guía 7)**: Almacenamiento dinámico de los nombres de los vendedores operativos y los montos recaudados utilizando estructuras lineales (`Lists`).
* **Reportes Financieros de Jornada**: Módulo de auditoría final automatizado que utiliza funciones de agregación (`sum()`) para desglosar la recaudación neta, el total de unidades vendidas y el listado de personal activo. El reporte está condicionado para no mostrar datos si la jornada no registró movimientos.

---

## 🛠️ Conceptos y Herramientas Aplicadas

* **Estructuras de Control Avanzadas**: Bucles condicionales (`while`), iteración de colecciones (`if` de existencia), bifurcaciones (`if-elif-else`) y control de flujo mediante `break` y `continue`.
* **Estructuras de Datos (Guía 7)**: Manipulación de listas dinámicas y carga de elementos en memoria mediante mutación controlada (`.append()`).
* **Lógica Matemática y Buenas Prácticas**: Uso de constantes en mayúsculas (`PRECIO_PRODUCTO`) para facilitar la escalabilidad del software y formateo avanzado de strings (`f-strings`) para alineación y visualización de monedas con precisión decimal (`:.2f`).

---

## 📋 Ejemplo de Interfaz (Consola)

```text
=== SISTEMA DE GESTIÓN DE STOCK Y VENTAS ===

Ingresá tu nombre: Tomas
Hola Tomas, ¿querés realizar una venta? (si/no): si
¿Cuántas unidades desea vender? 3
Venta exitosa. Quedan 7 unidades.

Ingresá tu nombre: 
No ingresaste tu nombre, intentalo nuevamente.

Ingresá tu nombre: Ana
Hola Ana, ¿querés realizar una venta? (si/no): no
Cerrando turno del vendedor...

==============================
RESUMEN DE JORNADA
Vendedores que operaron hoy: ['Tomas']
Unidades totales vendidas: 3
Total recaudado: $7501.50
==============================
```

---

## 🎓 Trayecto Formativo
Proyecto desarrollado y refactorizado de forma incremental como parte del trayecto formativo en **Talento Tech - Consolidación de Base (Guías 1-7)**. Demuestra la transición desde la programación lineal básica hasta el desarrollo defensivo y la gestión de estructuras de datos lineales en Python.

