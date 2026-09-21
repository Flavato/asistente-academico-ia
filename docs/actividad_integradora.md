# Actividad integradora del Asistente Académico IA

## Problema seleccionado

Los estudiantes necesitan organizar materias, tareas y fechas de entrega, especialmente cuando tienen varias actividades pendientes con diferentes niveles de dificultad.

## Solución desarrollada

Se desarrolló un prototipo web con Django denominado Asistente Académico IA. El sistema recibe una actividad, analiza la fecha de entrega y el nivel de dificultad, establece una prioridad y genera una recomendación.

También guarda las actividades en SQLite, muestra un historial y consulta información meteorológica mediante la API de Open-Meteo.

## Tres superficies

### Gestor de Agentes

Está representado por la lógica desarrollada en `views.py` y `servicios_clima.py`.

Sus funciones son:

- Recibir los datos del estudiante.
- Calcular los días restantes.
- Determinar la prioridad.
- Generar una recomendación.
- Consultar una API externa.
- Guardar la actividad en SQLite.

### Editor

Está representado por Visual Studio Code.

Desde el editor se realizaron las siguientes tareas:

- Creación del proyecto Django.
- Organización de carpetas y archivos.
- Desarrollo del modelo de datos.
- Creación de la vista y la plantilla.
- Configuración de variables de entorno.
- Documentación mediante Markdown.
- Control de versiones con Git.

### Prueba de Navegador

Está representada por la interfaz web que utiliza el estudiante.

Desde el navegador se comprobó:

- Carga del formulario.
- Envío de actividades.
- Generación de recomendaciones.
- Visualización del clima.
- Consulta del historial.
- Persistencia de los datos.

## Modo de agente seleccionado

Se utilizó un agente asistente con herramientas.

Se considera adecuado porque recibe información del usuario, aplica reglas para tomar una decisión, consulta una herramienta externa y devuelve una recomendación.

El prototipo no utiliza todavía un modelo generativo externo. La toma de decisiones se realiza mediante reglas controladas y comprensibles implementadas en Python.

## Artefactos desarrollados

- Lista de tareas.
- Plan de implementación.
- README.
- Árbol de contexto.
- Variables de entorno.
- Archivo `.env.example`.
- Archivo `.gitignore`.
- Modelo de datos.
- Migración de SQLite.
- Informe de pruebas.
- Capturas de funcionamiento.
- Repositorio de GitHub.
- Planificación en Google Calendar.

## Integraciones

### SQLite

Se utiliza para guardar las actividades y conservar el historial aunque se actualice la página.

### Open-Meteo

Se utiliza como API externa para consultar la temperatura, la sensación térmica y el estado meteorológico de Mendoza.

### Google Calendar

Se utiliza para registrar y organizar la fecha de revisión y entrega del prototipo.

### GitHub

Se utiliza para compartir el código, conservar el historial de cambios y documentar el proyecto.

## Pruebas realizadas

### Prueba 1 Fecha vencida

Se ingresó una fecha anterior a la actual.

Resultado obtenido:

- El sistema calculó días negativos.
- Estableció la prioridad “Fecha vencida”.
- Recomendó consultar con el docente.

### Prueba 2 Entrega del día

Se ingresó una actividad con fecha de entrega correspondiente al mismo día.

Resultado obtenido:

- El sistema calculó cero días restantes.
- Estableció la prioridad “Urgente”.
- Recomendó completar primero los puntos obligatorios.

### Prueba 3 Almacenamiento

Se registró una actividad y luego se actualizó la página.

Resultado obtenido:

- La actividad permaneció visible en el historial.
- Se comprobó el almacenamiento en SQLite.

### Prueba 4 API externa

Se abrió la aplicación con conexión a Internet.

Resultado obtenido:

- Se mostró la ciudad de Mendoza.
- Se mostró la temperatura actual.
- Se mostró la sensación térmica.
- Se mostró el estado meteorológico.

### Prueba 5 Protección de datos

Se ejecutó `git status` antes de subir el proyecto.

Resultado obtenido:

- `.env` no fue incluido.
- `venv` no fue incluido.
- `db.sqlite3` no fue incluido.
- `.env.example` sí fue incluido.

## Beneficios

- Ayuda a organizar actividades académicas.
- Establece prioridades automáticamente.
- Ofrece recomendaciones simples.
- Conserva un historial de tareas.
- Integra información proveniente de Internet.
- Centraliza diferentes funciones en una sola interfaz.
- Permite documentar y compartir el proyecto.

## Desafíos encontrados

Durante el desarrollo se presentaron dificultades con la instalación de Django, el registro de la aplicación, la configuración de rutas y la ubicación de archivos.

También se produjeron errores por nombres incorrectos, como `requirements.txtSS`, y una ruta inicial que generaba una respuesta 404.

Estos problemas fueron solucionados revisando los mensajes de la terminal, corrigiendo las rutas y comprobando cada etapa antes de continuar.

## Posibles mejoras

- Agregar inicio de sesión.
- Permitir editar y eliminar tareas.
- Incorporar materias registradas.
- Agregar notificaciones automáticas.
- Integrar Google Calendar directamente con Django.
- Permitir filtrar las actividades por prioridad.
- Incorporar una IA generativa para producir recomendaciones más personalizadas.
- Adaptar el prototipo como módulo del sistema ASIST.

## Conclusión

El prototipo permitió aplicar los conceptos de agentes de IA, arquitectura por superficies, variables de entorno, API externa, base de datos, documentación Markdown, pruebas en navegador y control de versiones.

La experiencia demostró que la IA y las herramientas automáticas ayudan durante el desarrollo, pero la persona debe revisar los resultados, interpretar los errores y mantener el control del proyecto.