# MiniCore Ventas - Ejercicio MVC

## Descripción General

MiniCore Ventas es una aplicación web desarrollada en Python utilizando el framework Flask.  
El proyecto aplica el patrón de diseño Modelo–Vista–Controlador (MVC) y tiene como objetivo gestionar la información de vendedores y calcular sus comisiones a partir de los registros de ventas.  

La aplicación fue desplegada en la nube mediante la plataforma Render.

---

## Arquitectura del Proyecto

El proyecto está estructurado de acuerdo con el patrón MVC:

MiniCore_Ventas-main/
│
├── app.py # Archivo principal de la aplicación (configuración de Flask y base de datos)
├── controllers/
│ └── venta_controller.py # Controlador principal, define rutas y lógica de negocio
├── models/
│ └── vendedor.py # Modelo de datos (clase Vendedor)
├── utils/
│ └── database.py # Configuración del motor SQLAlchemy
├── templates/
│ └── resumen.html # Vista HTML (interfaz de usuario)
├── static/ # Archivos estáticos (CSS, JS)
├── data.sql # Script SQL inicial con estructura y datos base
├── db.sqlite3 # Base de datos local (autogenerada en Render)
├── requirements.txt # Dependencias del proyecto
└── Procfile # Comando de ejecución para Render (Gunicorn)


---

## Tecnologías Utilizadas

| Componente | Descripción |
|-------------|-------------|
| Lenguaje de programación | Python 3.12 |
| Framework web | Flask |
| ORM | SQLAlchemy |
| Servidor de producción | Gunicorn |
| Base de datos | SQLite |
| Sistema de plantillas | Jinja2 |
| Plataforma de despliegue | Render.com |

---

## Despliegue en Render

La aplicación fue desplegada exitosamente en Render y se encuentra disponible en el siguiente enlace:

**URL de producción:** [https://ejerciciomvc.onrender.com](https://ejerciciomvc.onrender.com)

### Configuración de despliegue

- **Runtime:** Python 3.12.0  
- **Build Command:**
  ```bash
  pip install -r requirements.txt

## Start command

gunicorn app:app

## Variables de entorno

PYTHON_VERSION=3.12.0
FLASK_SECRET_KEY=dev
