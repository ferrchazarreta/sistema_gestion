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
python3 -m venv env
```

Para Windows

```bash
py -3 -m venv env
```

Activar el entorno virtual

```bash
source/env/Scripts/activate
```

Instalar los requerimientos

```bash
install -r requirements.txt
```

Realizar las migraciones correspondientes

```bash
manage.py makemigration
```

```bash
manage.py migrate
```

Correr el proyecto

```bash
manage.py runserver
```

## API Endpoints

A continuación, se detallan los endpoints disponibles para cada entidad en el sistema:

### Countries

- **GET**: Obtener lista de países
  `http://127.0.0.1:8000/api_v1/countries/`
- **POST**: Crear un nuevo país
  `http://127.0.0.1:8000/api_v1/countries/`
- **PUT**: Actualizar un país existente
  `http://127.0.0.1:8000/api_v1/countries/{id}/`
- **DELETE**: Eliminar un país
  `http://127.0.0.1:8000/api_v1/countries/{id}/`

### Modelos

- **GET**: Obtener lista de modelos
  `http://127.0.0.1:8000/api_v1/modelos/`
- **POST**: Crear un nuevo modelo
  `http://127.0.0.1:8000/api_v1/modelos/`
- **PUT**: Actualizar un modelo existente
  `http://127.0.0.1:8000/api_v1/modelos/{id}/`
- **DELETE**: Eliminar un modelo
  `http://127.0.0.1:8000/api_v1/modelos/{id}/`

### Brands

- **GET**: Obtener lista de marcas
  `http://127.0.0.1:8000/api_v1/brands/`
- **POST**: Crear una nueva marca
  `http://127.0.0.1:8000/api_v1/brands/`
- **PUT**: Actualizar una marca existente
  `http://127.0.0.1:8000/api_v1/brands/{id}/`
- **DELETE**: Eliminar una marca
  `http://127.0.0.1:8000/api_v1/brands/{id}/`

### Fuels

- **GET**: Obtener lista de tipos de combustible
  `http://127.0.0.1:8000/api_v1/fuels/`
- **POST**: Crear un nuevo tipo de combustible
  `http://127.0.0.1:8000/api_v1/fuels/`
- **PUT**: Actualizar un tipo de combustible existente
  `http://127.0.0.1:8000/api_v1/fuels/{id}/`
- **DELETE**: Eliminar un tipo de combustible
  `http://127.0.0.1:8000/api_v1/fuels/{id}/`

### Transmissions

- **GET**: Obtener lista de tipos de transmisión
  `http://127.0.0.1:8000/api_v1/transmissions/`
- **POST**: Crear un nuevo tipo de transmisión
  `http://127.0.0.1:8000/api_v1/transmissions/`
- **PUT**: Actualizar un tipo de transmisión existente
  `http://127.0.0.1:8000/api_v1/transmissions/{id}/`
- **DELETE**: Eliminar un tipo de transmisión
  `http://127.0.0.1:8000/api_v1/transmissions/{id}/`

### Gamas

- **GET**: Obtener lista de gamas
  `http://127.0.0.1:8000/api_v1/gamas/`
- **POST**: Crear una nueva gama
  `http://127.0.0.1:8000/api_v1/gamas/`
- **PUT**: Actualizar una gama existente
  `http://127.0.0.1:8000/api_v1/gamas/{id}/`
- **DELETE**: Eliminar una gama
  `http://127.0.0.1:8000/api_v1/gamas/{id}/`

### Conditions

- **GET**: Obtener lista de condiciones
  `http://127.0.0.1:8000/api_v1/conditions/`
- **POST**: Crear una nueva condición
  `http://127.0.0.1:8000/api_v1/conditions/`
- **PUT**: Actualizar una condición existente
  `http://127.0.0.1:8000/api_v1/conditions/{id}/`
- **DELETE**: Eliminar una condición
  `http://127.0.0.1:8000/api_v1/conditions/{id}/`

### Bodyworks

- **GET**: Obtener lista de tipos de carrocería
  `http://127.0.0.1:8000/api_v1/bodyworks/`
- **POST**: Crear un nuevo tipo de carrocería
  `http://127.0.0.1:8000/api_v1/bodyworks/`
- **PUT**: Actualizar un tipo de carrocería existente
  `http://127.0.0.1:8000/api_v1/bodyworks/{id}/`
- **DELETE**: Eliminar un tipo de carrocería
  `http://127.0.0.1:8000/api_v1/bodyworks/{id}/`

### Cars

- **GET**: Obtener lista de autos
  `http://127.0.0.1:8000/api_v1/cars/`
- **POST**: Crear un nuevo auto
  `http://127.0.0.1:8000/api_v1/cars/`
- **PUT**: Actualizar un auto existente
  `http://127.0.0.1:8000/api_v1/cars/{id}/`
- **DELETE**: Eliminar un auto
  `http://127.0.0.1:8000/api_v1/cars/{id}/`

### Reviews

- **GET**: Obtener lista de reseñas de un vehículo
  `http://127.0.0.1:8000/api_v1/cars/{vehiculo_id}/reviews/`
- **POST**: Crear una nueva reseña para un vehículo
  `http://127.0.0.1:8000/api_v1/cars/{vehiculo_id}/reviews/`
- **PUT**: Actualizar una reseña existente
  `http://127.0.0.1:8000/api_v1/cars/{vehiculo_id}/reviews/{id}/`
- **DELETE**: Eliminar una reseña
  `http://127.0.0.1:8000/api_v1/cars/{vehiculo_id}/reviews/{id}/`

### Usuarios

- **GET**: Obtener lista de usuarios
  `http://127.0.0.1:8000/api_v1/usuarios/`
- **POST**: Crear un nuevo usuario
  `http://127.0.0.1:8000/api_v1/usuarios/`
- **PUT**: Actualizar un usuario existente
  `http://127.0.0.1:8000/api_v1/usuarios/{id}/`
- **DELETE**: Eliminar un usuario
  `http://127.0.0.1:8000/api_v1/usuarios/{id}/`

### Clientes

- **GET**: Obtener lista de clientes
  `http://127.0.0.1:8000/api_v1/clientes/`
- **POST**: Crear un nuevo cliente
  `http://127.0.0.1:8000/api_v1/clientes/`
- **PUT**: Actualizar un cliente existente
  `http://127.0.0.1:8000/api_v1/clientes/{id}/`
- **DELETE**: Eliminar un cliente
  `http://127.0.0.1:8000/api_v1/clientes/{id}/`

## Integrantes

- Chazarreta Fernando
- Gurrea Mateo
- Lombardi Simon

```

```
