# 🛒 Sistema de Gestión de Ventas e Inventario

Una aplicación de consola robusta desarrollada en **Python** diseñada para la administración de inventarios y el procesamiento de ventas en tiempo real. Este proyecto destaca por su enfoque en la arquitectura limpia, la optimización algorítmica y una experiencia de usuario (UX) mejorada mediante feedback visual en la terminal.

---

### 🚀 Características Destacadas

*   **Validación Temprana (Guard Clauses):** Flujo lógico optimizado mediante cláusulas de guarda en el procesamiento de ventas. Elimina el anidamiento innecesario (`else`), mejorando drásticamente la legibilidad y el mantenimiento del código.
*   **Procesamiento Eficiente:** Cálculo instantáneo de reportes financieros mediante el uso de la función integrada `sum()` combinada con expresiones de comprensión (*comprehension expressions*).
*   **Integridad de Datos:** Gestión segura del flujo del programa mediante el uso de tuplas y desempaquetado (*unpacking*) para el manejo de múltiples valores de retorno.
*   **Experiencia de Usuario Profesional (UX):** Interfaz interactiva por línea de comandos con sanitización estricta de entradas de usuario (`.strip().title()`) e integración de códigos de color para jerarquizar la información (Éxitos en Cian, Errores en Rojo, Reportes en Verde).
*   **Documentación Rigurosa:** Código completamente documentado utilizando *Docstrings* detallados que especifican el propósito, parámetros tipados (`list`, `int`, `float`) y valores de retorno de cada función.

---

### 🛠️ Stack Tecnológico

*   **Lenguaje:** Python 3.x
*   **Librerías:** [Colorama](https://pypi.org) (Estilizado y formateo de color en terminal)

---

### 📂 Estructura y Arquitectura del Código

El proyecto está diseñado bajo principios de modularidad y separación de responsabilidades:


| Componente | Descripción Técnica |
| :--- | :--- |
| `procesar_venta()` | Motor lógico autónomo que encapsula la validación de stock y el cálculo de montos. |
| `resumen_jornada()` | Generador de reportes optimizado con formateo financiero (`$:,.2f`) para alta precisión en cifras. |
| **Ciclo Principal** | Orquestador de la interfaz de usuario con sanitización activa de datos de entrada. |

---

### ⚙️ Instalación y Uso

Sigue estos pasos para clonar y ejecutar el sistema localmente en tu terminal:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com
   cd gestor_de_stock
   ```

2. **Instalar las dependencias:**
   ```bash
   pip install colorama
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```
   *(Nota: Reemplaza `main.py` por el nombre real de tu archivo principal si es diferente).*

---

### 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consúltala para más detalles.
