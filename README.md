# gestor_de_stock
Sistema interactivo de gestión de inventario desarrollado en Python. Implementa lógica de bucles controlados, validación de stock en tiempo real y normalización de entradas de usuario (Data Cleaning).

# 📦 Gestor de Inventario - Tienda Tech

Este proyecto es una solución interactiva desarrollada en **Python** para la gestión de ventas y control de stock de una tienda. El objetivo principal es garantizar la integridad de los datos mediante validaciones lógicas y normalización de entradas.

## 🚀 Funcionalidades
*   **Normalización de Datos:** Limpieza de espacios y formateo de nombres mediante métodos de strings (`.strip()`, `.title()`, `.lower()`).
*   **Control de Stock:** Validación en tiempo real que impide ventas superiores a la existencia física.
*   **Lógica de Negocio:** Cálculo automático de recaudación basado en precios unitarios y actualización de estados mediante acumuladores.
*   **Interfaz de Consola:** Flujo continuo de trabajo mediante bucles `while` con condiciones de salida dinámicas.

## 🛠️ Conceptos Aplicados
*   **Estructuras de Control:** `while`, `if-elif-else`, `break` y `continue`.
*   **Tipos de Datos:** Casting robusto de `int` y `float`.
*   **Interpolación de Strings:** Formateo avanzado con `f-strings` para moneda (dos decimales).
*   **Data Cleaning:** Procesamiento de inputs para evitar errores por ingreso de usuario.

## 📋 Ejemplo de Uso
Al ejecutar el script, el sistema solicitará el nombre del vendedor y permitirá procesar ventas hasta que se agote el stock o el usuario decida finalizar la jornada.

---
*Proyecto desarrollado como parte del trayecto formativo en **Talento Tech** - Consolidación de Base (Guías 1-5).*
