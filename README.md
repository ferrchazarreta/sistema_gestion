## Descripción del Proyecto
Desarrollar un sistema web para la gestión de una concesionaria de autos utilizando Django.

## Especificaciones del Sistema
	• Modelos de Base de Datos
 	• Autenticación de Usuarios
  	• Roles de Usuarios
	• Usuario Staff
  	• Usuario No Staff
  	• Carga de Imágenes
	• Restricciones de Acceso

 ## Requisitos Técnicos
	• Desarrollar el proyecto utilizando Django>=4.x.
	• Seguir las mejores prácticas de desarrollo, incluyendo el uso de templates, modelos, vistas (View) y formularios de Django (Forms).
	• Asegurar la correcta validación de datos en los formularios.
	• Implementar autenticación y autorización utilizando el sistema de usuarios de Django.
	• Utilizar archivos estáticos y de media correctamente configurados para la gestión de imágenes.
	• Generar al menos dos métodos que estén incluidos en el context_processors 	

## Instalación

1. Clonar este repositorio de manera local

```bash
git clone git@github.com:ferrchazarreta/sistema_gestion.git
```

2. Situarce en el directorio del proyecto:

```bash
cd sistema_gestion
```

## Ejecución

Para ejecutar la aplicacion segui estos pasos:

Para Linux
```bash
sudo python3 -m venv env
```

Para Windows
```bash
sudo py -3 -m venv env
```
Activar el entorno virtual
```bash
sudo source/env/Scripts/activate
```

Instalar los requerimientos

```bash
pip install -r requirements.txt
```
Realizar las migraciones correspondientes
```bash
python manage.py makemigration
```
```bash
python manage.py migrate
```
Correr el proyecto
```bash
python manage.py runserver
```


## Integrantes
- Chazarreta Fernando
- Gurrea Mateo
- Lombardi Simon
