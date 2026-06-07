# 🛒 Sistema de Gestión de Ventas

Este proyecto es una aplicación de consola desarrollada en **Python** para la administración de inventarios y procesamiento de ventas en tiempo real. La aplicación destaca por su enfoque en la **modularidad**, la **eficiencia algorítmica** y una interfaz de usuario optimizada mediante **feedback visual coloreado**.

## 🚀 Características Técnicas

*   **Lógica de Negocio con Guard Clauses**: Implementación de "Cláusulas de Guarda" en la función de procesamiento para validar el stock de forma temprana, mejorando la legibilidad y eliminando bloques `else` innecesarios.
*   **Procesamiento de Alta Eficiencia**: Uso de la función integrada `sum()` con expresiones de comprensión para el cálculo instantáneo del reporte financiero de la jornada.
*   **Gestión de Datos Robusta**: Manejo de múltiples valores de retorno mediante **tuplas** y desempaquetado (unpacking) para garantizar la integridad del flujo del programa.
*   **Interfaz Profesional (UX)**: Integración de la librería **Colorama** para jerarquizar la información (éxitos en cian, errores en rojo, reportes en verde) y validación estricta de entradas de usuario.
*   **Documentación Técnica**: Implementación de **Docstrings** detallados que describen el propósito, parámetros con tipos de datos (`float`, `int`, `list`) y valores de retorno de cada función.

## 🛠️ Tecnologías Utilizadas

*   **Python 3.x**
*   **Colorama**: Estilizado de terminal y mejora de la interacción.

## 📂 Estructura del Código

1.  **`procesar_venta()`**: Motor lógico que encapsula la validación de stock y el cálculo de montos de forma autónoma.
2.  **`resumen_jornada()`**: Generador de reportes optimizado con formateo financiero (`$:,.2f`) para mayor claridad en grandes cifras.
3.  **Ciclo Principal**: Interfaz interactiva con sanitización de datos mediante `.strip().title()`.
