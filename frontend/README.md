
# Plataforma de Adopción de Mascotas - Frontend

Este es el frontend de una plataforma en línea diseñada para facilitar la adopción de mascotas rescatadas. Permite a los usuarios buscar y solicitar la adopción de mascotas, así como a los refugios de animales registrar mascotas en adopción y gestionar el proceso de adopción para encontrarles hogares amorosos. 
## Features (aun en desarrollo)

- Búsqueda y solicitud de adopción de mascotas en línea.
- Registro y gestión de mascotas en adopción por parte de los refugios.


## Tech Stack (aun en desarrollo)
- Vite para la configuración del entorno de desarrollo, con la URL del backend especificada en vite.config.js.
- Tailwind CSS y CSS para el estilo.
- React Router para la gestión de rutas.
- Axios para el manejo de solicitudes HTTP.
- Firebase para almacenar las imágenes del front (logos de los refugios e imágenes de las mascotas), enviando la URL al backend.


## Estructura de carpetas (aun en desarrollo)
La estructura del proyecto es la siguiente :

```
└── 📁src
    └── 📁assets
    └── 📁components
    └── 📁context
    └── 📁hooks
    └── 📁pages

```
## Installation

Primero debes clonar este repositorio utilizando los siguientes comando en tu consola.


```bash
  git clone https://github.com/No-Country/c17-71-m-python.git

  cd c17-71-m-python/frontend

  npm install
  npm run dev
```
    
## Configuración de Firebase
- Deberás crear un proyecto en Firebase (para el almacenamiento de las imagenes) para obtener las credenciales y la configuración adecuada (https://firebase.google.com/?hl=es-419).
- Crea un archivo .env para la configuración de Firebase. Asegúrate de incluir las variables necesarias en tu archivo .env. Aquí tienes un ejemplo:

```bash
    VITE_FIREBASE_API_KEY="tu-api-key"
    VITE_FIREBASE_AUTH_DOMAIN="tu-auth-domain"
    VITE_FIREBASE_PROJECT_ID="tu-project-id"
    VITE_FIREBASE_STORAGE_BUCKET="tu-storage-bucket"
    VITE_FIREBASE_MESSAGING_SENDER_ID="tu-messaging-sender-id"
    VITE_FIREBASE_APP_ID="tu-app-id"
```

- Luego, asegúrate de agregar el archivo .env a tu archivo .gitignore para que no se suba al repositorio.
- Utiliza estas variables de entorno en tu aplicación para conectarla con Firebase.
## Integrantes del equipo frontend

| Nombre | Rol | 
|----------|----------|
| [Angely Bonaldy](https://github.com/anggifit) | Frontend |
| [Fabian Mederos](https://github.com/juabiDev) | Frontend |

