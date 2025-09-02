"""
Configuración principal de Django para el proyecto.

Este archivo define la configuración global del proyecto, incluyendo:
- Variables de entorno
- Aplicaciones instaladas
- Middleware
- Configuración de base de datos
- Configuración de GraphQL y REST Framework
- Idioma, zona horaria y archivos estáticos

Se recomienda utilizar variables de entorno para las configuraciones
sensibles o dependientes del entorno (ej. SECRET_KEY, credenciales de BD)
"""

import os
from pathlib import Path
import environ



# BASE DIR DEL PROYECTO
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# VARIABLES DE ENTORNO
# TODO: Instalar django-environ -> pip install django-environ
# TODO: Crear archivo `.env` en la raíz del proyecto con las variables necesarias
env = environ.Env(
    DEBUG=(bool, True)  # Define el tipo de la variable DEBUG
)

# TODO: Cargar el archivo `.env` ubicado en la raíz del proyecto
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# CONFIGURACIÓN BÁSICA
# TODO: Cambiar SECRET_KEY en producción
SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])



# APLICACIONES INSTALADAS
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # TODO: Verificar instalación de dependencias de terceros
    'graphene_django',              # GraphQL
    'rest_framework',               # API REST
    'rest_framework_simplejwt',     # JWT Authentication

    # Apps internas
    'core',
    'infrastructure',
    'application',
]


# MIDDLEWARE

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



# CONFIGURACIÓN DE URLS Y WSGI
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'



# TODO: Crear carpeta `templates/` en el proyecto para plantillas globales
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# BASE DE DATOS
# TODO: Crear variables en .env -> DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# =========================
# GRAPHQL
# =========================
GRAPHENE = {
    "SCHEMA": "config.schema.schema"  # TODO: Definir schema GraphQL en config/schema.py
}


# =========================
# VALIDACIÓN DE PASSWORDS
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    
]


# =========================
# REST FRAMEWORK
# =========================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # TODO: Cambiar según necesidades del proyecto
    )
}


# =========================
# CONFIGURACIÓN GENERAL
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Evita warnings con IDs

# Idioma y zona horaria
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/La_Paz'
USE_I18N = True
USE_TZ = True

# TODO: Crear carpetas `static/` y `media/` en el proyecto
""" STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"] """
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"
