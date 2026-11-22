# Quickly FrontEnd - Interfaz Web y Punto de Venta (POS)

Aplicación web desarrollada en **Python (Flask)**, **Jinja2** y **Bootstrap 5** que proporciona la interfaz de usuario para el sistema de administración y facturación electrónica **Quickly**, conectada en tiempo real mediante consumo de API REST (`requests`) con el Backend en MySQL.

---

## 🖥️ Módulos Implementados

* **Panel de Control (Dashboard):** Indicadores dinámicos en tiempo real con el conteo total de clientes, facturas emitidas, productos en inventario y usuarios activos.
* **Gestión de Clientes:** Registro, listado, edición y eliminación de clientes.
* **Gestión de Categorías:** Administración de categorías de inventario.
* **Gestión de Productos:** Control de catálogo con códigos de barras, precios, existencias y asignación dinámica de categorías.
* **Gestión de Usuarios:** Administración de colaboradores y roles del sistema.
* **Facturación / Punto de Venta (POS):** Emisión de facturas con autocompletado de clientes, selección dinámica de múltiples productos y descuento automático de inventario en MySQL, además de historial detallado de ventas.

---

## 📂 Estructura del Proyecto

```text
ADSO-25T4-FacturApp_FrontEnd/
├── src/
│   ├── __init__.py              # Configuración de la aplicación Flask y registro de Blueprints
│   ├── app.py                   # Servidor web local (Puerto 5005)
│   ├── controllers/             # Controladores que consumen la API del Backend (http://127.0.0.1:5002/api)
│   │   ├── home_controller.py
│   │   ├── clients_controller.py
│   │   ├── categories_controller.py
│   │   ├── producto_controller.py
│   │   ├── usuario_controller.py
│   │   └── factura_controller.py
│   └── templates/               # Vistas HTML dinámicas con Jinja2 y Bootstrap 5
│       ├── layout.html
│       ├── home.html
│       ├── clients/
│       ├── categories/
│       ├── productos/
│       ├── usuarios/
│       └── facturas/
└── README.md
```

---

## 🚀 Guía de Instalación y Ejecución Local

> **Requisito previo:** El servidor **Backend (`ADSO-25T4-Quickly_BackEnd`)** debe estar encendido en el puerto `5002` junto con **MySQL (XAMPP)**.

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/marioandresquecan33-code/ADSO-25T4-FacturApp_FrontEnd.git
   cd ADSO-25T4-FacturApp_FrontEnd
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate   # En Windows (Git Bash)
   ```

3. **Instalar dependencias:**
   ```bash
   pip install flask requests
   ```

4. **Ejecutar el servidor Frontend:**
   ```bash
   python -m src.app
   ```

5. **Abrir en el navegador:**
   Ingresar a `http://127.0.0.1:5005`

---

## 👨‍💻 Autor
**Mario Andrés Quecán Velásquez**  
Tecnólogo en Análisis y Desarrollo de Software (ADSO) Ficha 3336128 - SENA
