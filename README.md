# Asistente Académico IA

Prototipo desarrollado para Prácticas Profesionalizantes III.

## Problema

Los estudiantes necesitan organizar materias, actividades y fechas de entrega desde un solo lugar.

## Solución

El sistema recibe una actividad académica, analiza la fecha de entrega y el nivel de dificultad, determina su prioridad y genera una recomendación.

## Funciones implementadas

* Registro de materia y actividad.
* Selección de fecha de entrega.
* Selección del nivel de dificultad.
* Cálculo de días restantes.
* Generación de una recomendación.
* Almacenamiento en SQLite.
* Historial de actividades.
* Consulta de clima mediante una API externa.
* Configuración con variables de entorno.
* Pruebas desde el navegador.

## Tecnologías

* Python
* Django
* HTML y CSS
* SQLite
* Requests
* Python Dotenv
* Open-Meteo API

## Árbol de contexto

```text
Asistente_academico_IA/
├── asistente/
│   ├── migrations/
│   ├── templates/
│   │   └── asistente/
│   │       └── inicio.html
│   ├── models.py
│   ├── servicios_clima.py
│   ├── urls.py
│   └── views.py
├── configuracion/
│   ├── settings.py
│   └── urls.py
├── .env.example
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

## Variables de entorno

Crear un archivo llamado `.env` en la carpeta principal, tomando como referencia el archivo `.env.example`.

```env
WEATHER_API_URL=https://api.open-meteo.com/v1/forecast
WEATHER_LATITUDE=-32.89
WEATHER_LONGITUDE=-68.84
WEATHER_CITY=Mendoza
```

## Instalación y ejecución

Las siguientes instrucciones permiten instalar y ejecutar el proyecto en otra computadora.

### 1. Crear el entorno virtual

```text
py -m venv venv
```

### 2. Activar el entorno virtual en Windows

```text
venv\Scripts\activate
```

### 3. Instalar las dependencias

```text
python -m pip install -r requirements.txt
```

### 4. Crear las tablas de la base de datos

```text
python manage.py migrate
```

### 5. Iniciar el servidor

```text
python manage.py runserver
```

### 6. Abrir la aplicación

Ingresar desde el navegador a:

```text
http://127.0.0.1:8000/
```

## Seguridad

El archivo `.env` no se incluye en el repositorio porque puede contener configuraciones privadas.

El archivo `.env.example` presenta las variables necesarias sin exponer información sensible.

La carpeta `venv` y la base de datos local `db.sqlite3` tampoco se incluyen en el repositorio.

## Pruebas realizadas

* Carga de una actividad académica.
* Cálculo de los días restantes.
* Identificación de fechas vencidas.
* Generación de prioridades.
* Generación de recomendaciones.
* Almacenamiento de actividades en SQLite.
* Visualización del historial.
* Consulta de información meteorológica externa.
* Prueba de la interfaz desde el navegador.

## Estado del proyecto

Prototipo funcional en entorno local.

El sistema permite registrar actividades académicas, analizar su prioridad, generar recomendaciones, guardar la información en SQLite y consultar el clima mediante una API externa.