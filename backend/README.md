# API Adopción de mascotas
> [!WARNING]
> Este proyecto aun está en desarrollo.

<div>
    <a href="https://api-adopcion-mascotas-production.up.railway.app/api/documentation/" target="_blank">
        <img src="/backend/images/ApiBanner.png">
    </a>
</div>

### 1. Descripción del proyecto
Bienvenido a la API de adopción de mascotas, diseñada para agilizar el proceso de adopción de mascotas al proporcionar una interfaz perfecta entre los solicitantes de mascotas y los refugios. Esta API, creada con [Django Rest Framework](https://www.django-rest-framework.org/) y [PostgreSQL](https://www.postgresql.org/), ofrece un sólido conjunto de funcionalidades destinadas a simplificar los procedimientos de adopción de mascotas.

#### 1.1. Características de los usuarios
En el sistema se definen dos tipos de usuarios:
- **Refugios:** Los refugios son organizaciones o personas físicas encargadas de cuidar y facilitar la adopción de mascotas. Interactúan con la plataforma para registrarse, registrar mascotas disponibles para adopción y recibir comunicaciones y notificaciones relacionadas con consultas de adopción.

- **Administradores:** Los administradores son usuarios con privilegios elevados que supervisan y administran la plataforma. Tienen acceso a funcionalidades que les permiten administrar la información del refugio, ver registros de correo electrónico y realizar tareas administrativas para garantizar el buen funcionamiento del proceso de adopción.

#### 1.2. Requerimientos funcionales
- **Registro de refugio**: El proceso de registro de refugios está diseñado para ser sencillo e integral. Los refugios pueden proporcionar detalles esenciales durante el registro, como información de contacto, personal responsable e incluso cargar el logotipo del refugio. Esto no sólo ayuda a presentar una imagen profesional, sino que también agiliza la comunicación entre los refugios y los posibles adoptantes, fomentando una experiencia de adopción más fluida en general.

- **Registro de mascotas para refugios**: La funcionalidad de registro de mascotas  permite a los refugios exhibir a sus mascotas de manera efectiva. Los refugios autenticados pueden proporcionar información completa sobre cada mascota, incluido su nombre, raza, edad, historial médico y fotografías. Este perfil detallado no sólo mejora la visibilidad de las mascotas sino que también aumenta sus posibilidades de adopción.

- **Autenticación**: Los mecanismos de autenticación estan diseñados para proteger datos confidenciales y garantizar que solo los usuarios autorizados puedan acceder y administrar los recursos o datos del sistema. Se utiliza **JSON Web Token** para el inicio de sesión de usuarios y el control de acceso basado en roles. Esto garantiza que los usuarios puedan autenticarse de forma segura y acceder al sistema mientras mantienen la seguridad e integridad de los datos durante todo el proceso.

- **Envío de correos electrónicos a los refugios**: Se envían notificaciones automáticas por correo electrónico a los refugios para comunicarse con respecto a consultas de adopción, actualizaciones y notificaciones administrativas.

Los **administradores** tendrán acceso a funcionalidades que les facilitara la gestión de la plataforma desde el panel de administración:

- **Administrar información del refugio:** los administradores pueden ver y administrar toda la información relacionada con los refugios registrados, incluidos detalles de contacto, listados de mascotas y procesos de adopción.
- **Ver registros de correo electrónico:** los administradores pueden acceder a un registro de todos los correos electrónicos enviados desde la plataforma, incluidas consultas de adopción, notificaciones y comunicaciones con refugios.

#### 1.3. Arquitectura del proyecto
La estructura del proyecto es la siguiente:

```
└── 📁src
    └── 📁apps
    └── 📁settings
        └── 📁environments
            └── base.py
            └── development.py
            └── production.py
            └── testing.py
        └── asgi.py
        └── urls.py
        └── wsgi.py
    └── 📁tests
    └── manage.py
    └── pytest.ini
    └── requirements.txt
```

- **[src](./src/):** este es el directorio raíz del poryecto. Contiene todos los modulos, configuraciones  globales y pruebas del código.

- **[apps](./src/apps/):** este directorio contiene las aplicaciones Dajngo. Está dividido en varios subdirectorios, cada uno de los cuales representa un servicio o aplicación. Tambien podras encontras algunos ficheros auxiliares en donde cada servicio podra hacer uso de ellos respectivamente.

- **[settings](./src/settings/):** Contiene archivos de configuración para la API. Incluye configuraciones para los diferentes entornos de desarrollo, producción y pruebas, configuraciones de los punto finales de la API, configuraciones ASGI y WSGI, etc.

- **[tests](./src/tests/):** Contiene pruebas unitarias y de implementación del código de cada aplicación.

- **[manage.py](./src/manage.py):** esta es una utilidad de línea de comandos que te permite interactuar con tu proyecto Django de varias maneras.

- **[requirements.txt](./src/requirements.txt):** este archivo se utiliza para administrar dependencias para un proyecto de Python. Enumera todos los paquetes de Python de los que depende el proyecto.

- **[pytest.ini](./src/pytest.ini):** Este archivo contiene la configuración para pytest, un marco de prueba para Python.


## 2. Instalación del proyecto
> [!NOTE]
> Asegúrese que Python 3.11.5 esté instalado en su sistema operativo.

Primero debes seguir las siguientes instrucciones y dependiendo de que manera quieres realizar la instalación seguiras los pasos para instalar el proyecto de manera manual o utilizando Docker.

- **Clonar repositorio:** Para clonar este repositorio ejecuta los siguientes comandos.
    
    ```bash
    git clone https://github.com/No-Country/c17-71-m-python.git
    cd c17-71-m-python/backend
    ```
    
- **Crear y activar entorno virtual:** Creares un entorno virtual con el siguiente comando, en este entorno instalaremos todas las dependencias de este proyecto.
    
    ```bash
    python3 -m venv <nombre_del_entorno>
    ```
    
    Por ultimo activamos el entorno con el siguiente comando.
    
    ```bash
    # Linux y macOS
    source <nombre_del_entorno>/bin/activate
    
    # Windows
    .<nombre_del_entorno>\Scripts\activate
    ```
    
- **Configurar variables de entorno:** Crea un archivo con el nombre _.env_ dentro del directorio _src_. En este archivo se definiran todas las variables de entorno de este proyecto. Las variables que se deben configurar son las siguientes.

    ```.env
    KEY_DJANGO=value

    # SMTP settings
    EMAIL_HOST_USER=<tu correo electrónico>
    EMAIL_HOST=smtp.gmail.com
    EMAIL_HOST_PASSWORD=<contraseña de aplicación de tu correo>
    EMAIL_PORT=587
    EMAIL_USE_TLS=true
    ```

    El valor de la variable `KEY_DJANGO` lo puedes obtener ejecutando los siguientes comandos. Primero iniciamos el intérprete de Python.

    ```bash
    python3
    ```
    El siguiente comando te va retornar el valor de `KEY_DJANGO` que deberas copiar en el archivo _.env_.

    ```bash
    from django.core.management.utils import get_random_secret_key; print(get_random_secret_key()); exit()
    ```

### 2.1. Instalación manual

- **Paso 1 (instalar dependencias):** Para instalar las teconologias y paquetes que usa el proyecto usa el siguiente comando. Asegurate estar en el directotio raíz.
    
    ```bash
    pip install -r "requirements.txt"
    ```
    
- **Paso 2 (realizar migraciones):** Migramos los modelos del proyecto necesarios para el funcionamiento del servidor con el siguiente comando.
    
    ```bash
    python3 src/manage.py migrate --settings=settings.environments.development
    ```
    
- **Paso 3 (poblar las tablas auxiliares):** La tabla `pets` utiliza tablas auxiliares que se utilizan para el registro de mascotas, para poblar estas tablas debes ejecutar los siguientes comandos.
    
    ```bash
    python3 src/manage.py addpettypes --settings=settings.environments.development
    python3 src/manage.py addpetsextypes --settings=settings.environments.development
    ```
    
- **Paso 4 (iniciar el servidor):** Para iniciar el servidor de manera local ejecuta el siguiente comando.
    
    ```bash
    python3 src/manage.py runserver --settings=settings.environments.development
    ```
    
### 2.1. Instalación con Docker

- **Paso 1 (Construir imagen):** para construir la imagen del contenedor de este pryecto debes ejecutar el siguiente comando.
    
    ```bash
    docker build -t api-adopcion-mascotas .
    ```
    
- **Paso 2 (Correr imagen):** para iniciar el contenedor de este pryecto debes ejecutar el siguiente comando.
    
    ```bash
    docker run -p 8000:8000 api-adopcion-mascotas
    ```
    
De esta manera podrás usar todas las funcionalidades que este proyecto tiene para ofrecer. Es importante que hayas seguido todos los pasos explicados en el orden establecido.

> [!WARNING]
> Si vas a realizar contribuciones deberas instalar los hooks de Git que se estan utilizando en este proyecto.

## 3. Instalación de hooks

Los ganchos de Git son scripts que Git ejecuta antes o después de eventos como: `commits`, `push` y `receive`. Son una característica integrada de Git y se utilizan para automatizar tareas en el flujo de trabajo de desarrollo de software. Por ejemplo, puede utilizar un _hook_ de **pre-commit** para ejecutar el conjunto de pruebas configuradas antes de cada _commit_, evitando confirmaciones con pruebas fallidas.

Este repositorio tiene configurados dos _hooks_ que se encargaran de validar que el código fuente de la API este correctamente formateado siguiendo el estándar [PEP8](https://peps.python.org/pep-0008/), y que el mensaje del _commit_ sigua el estándar [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/). Para instalar estas validaciones debes ejecutar el siguiente comando.

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

## 4. Tests
Para correr las pruebas del proyecto debes ejecutar el siguiente comando.

```bash
pytest src/tests
```

## 5. Integrantes del equipo backend

| Nombre | Enlaces | Rol | 
|----------|----------|----------|
| Amanda Pares | [Git Hub](https://github.com/AParesFermandez) - [LinkedIn](https://www.linkedin.com/in/amanda-pares-fern%C3%A1ndez-761689171/) | Backend |
| Nico Xynos | [Git Hub](https://github.com/nicoxynos5) - [LinkedIn](https://www.linkedin.com/in/nicoxynos/) | Backend |
| Carlos Aguirre | [Git Hub](https://github.com/The-Asintota) - [LinkedIn](https://www.linkedin.com/in/carlosaguirredev/) | Backend |