# API Adopción de mascotas
> [!NOTE]
> Este proyecto aun está en desarrollo.

<div>
    <a href="" target="_blank">
        <img src="/backend/images/ApiBanner.png">
    </a>
</div>

En este repositorio encontrarás el código fuente de la API para la plataforma de gestión de inmobiliaria Bonpland. Para desarrollar este API nos hemos apoyado de un marco de trabajo como [Django Rest Framework](https://www.django-rest-framework.org/).

## 1. Descripción del proyecto

La inmobiliaria opera principalmente a través de sus oficinas físicas y busca aprovechar la tecnología para ampliar su presencia en el mercado digital. La creación de una plataforma en línea no solo mejorará su visibilidad sino también la eficiencia de sus servicios.

### 1.1. Características de los usuarios
Por definir...

### 1.2. Requerimientos funcionales
Por definir...

### 1.3. Estructura
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


## 2. Instalación en local

Primero debes clonar este repositorio utilizando los siguientes comando en tu consola.

```bash
git clone https://github.com/No-Country/c17-71-m-python.git
cd c17-71-m-python/backend
```

### 2.1. Instalación manual

> [!NOTE]
> Asegúrese que Python 3.11.5 esté instalado en su sistema operativo.

- **Paso 1 (instalar dependencias):** Para instalar las teconologias y paquetes que usa el proyecto usa el siguiente comando. Asegurate estar en el directotio raíz.

    ```bash
    pip install -r "requirements.txt"
    ```

- **Paso 2 (configurar variables de entorno):** Crea un archivo con el nombre _.env_ dentro del directorio raíz. Dentro de este archivo se definiran todas las variables de entorno de este proyecto.

    ```.env
    KEY_DJANGO=value
    ```

    El valor de la variable `KEY_DJANGO` lo puedes obtener ejecutando los siguientes comandos. El ultimo comando retorna el valor de la variable que deberas copiar en el archivo _.env_.

    ```bash
    python3
    from django.core.management.utils import get_random_secret_key; print(get_random_secret_key()); exit()
    ```

- **Paso 4 (realizar migraciones):** Migramos los modelos del proyecto necesarios para el funcionamiento del servidor con el siguiente comando.

    ```bash
    python3 manage.py migrate --settings=settings.environments.development
    ```

- **Paso 5 (poblar las tablas auxiliares de la tabla pets):** La tabla `pets` utiliza tablas auxiliares que se utilizan para el registro de mascotas, para poblar estas tablas debes ejecutar los siguientes comandos.

    ```bash
    python3 manage.py addpettypes --settings=settings.environments.development
    python3 manage.py addpetsextypes --settings=settings.environments.development
    ```

- **Paso 6 (Iniciar el servidor):** Para iniciar el servidor de manera local ejecuta el siguiente comando.

    ```bash
    python3 manage.py runserver --settings=settings.environments.development
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

## 3. Instalación de hooks

> [!NOTE]
> Si vas a contribuir al proyecto debes ejecutar estos comandos.

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
| Nombre | Rol | 
|----------|----------|
| [Amanda Pares](https://github.com/AParesFermandez) | Backend |
| [Nico Xynos](https://github.com/nicoxynos5) | Backend |
| [Carlos Andres Aguirre Ariza](https://github.com/The-Asintota) | Backend |