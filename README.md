# Proyecto Arcerojas Predial

Este proyecto es una aplicación web para la gestión de predios construida con Django y Docker.

------
### Contenido
- ![Requisitos previos](#requisitos-previos)
- ![Configuración inicial](#configuración-inicial)
- ![Configuración con Docker](#configuración-con-docker)
- ![Pruebas en Postman](#pruebas-en-postman)
- ![Ejecución de Tests](#ejecución-de-tests)

------
### Requisitos previos
- Docker y Docker Compose
- git
- Python (recomendado versión 3.8+)
- Pip (gestor de paquetes de Python)
- Postman

-----
## Configuración inicial
### Clonar el repositorio

- git clone https://github.com/Magno-12/prueba_tecnica_consultores/tree/master
- cd [NOMBRE_DEL_REPOSITORIO]

-----
## Configurar el entorno virtual
### Instalar virtualenv:

- pip install virtualenv

### Crear un nuevo entorno virtual:
- virtualenv venv

### Activar el entorno virtual:
## En Windows:
- venv\Scripts\activate

## En macOS y Linux:
- source venv/bin/activate

-----
## Instalar las dependencias
### Con el entorno virtual activado, instala las dependencias:

- pip install -r requirements.txt

-----
## Configuración con Docker
### Construcción y ejecución
Construye la imagen y ejecuta los contenedores:

- docker-compose build
- docker-compose up

-----
## Migraciones
### Una vez que el contenedor esté en funcionamiento, abre una nueva terminal y ejecuta:

- docker-compose exec web python manage.py migrate

-----
## Crear un superusuario
### Para acceder al panel de administración de Django:

- docker-compose exec web python manage.py createsuperuser

-----
## Pruebas en Postman
### Configura Postman para manejar el token CSRF:

Accede a la página principal del proyecto en tu navegador para obtener la cookie csrftoken.
En Postman, añade un header X-CSRFToken con el valor del token CSRF.(opcional)
Endpoints:

### Cargar archivos JSON:

- Método: POST
- URL: http://localhost:8000/upload/
- Body: form-data
- Clave: file y nombre file, y sube un archivo .json.

![image](https://github.com/Magno-12/prueba_tecnica_consultores/assets/66977118/608b2921-980a-4fd7-8e39-208588e1e57d)

-----
## Ejecución de Tests
1. Asegúrate de que los contenedores de Docker estén en ejecución.
2. Ejecuta los tests usando el siguiente comando:

- docker-compose exec web coverage run manage.py test

-----
## Swagger para ver los endpoint en detalle: 
- http://localhost:8000/swagger/
