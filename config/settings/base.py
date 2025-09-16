import os
from pathlib import Path
import environ

# TODO: Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# TODO: Configurar entorno con variables del .env
env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# TODO: Configuración básica de Django
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = []

# TODO: Apps instaladas en el proyecto
INSTALLED_APPS = [
    # Django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Librerías externas
    'graphene_django',

    # Apps internas
    'application.apps.ApplicationConfig',
    'core.apps.CoreConfig',
    'infrastructure.apps.InfrastructureConfig',
]

# TODO: Middleware del proyecto
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# TODO: Archivo de rutas principal
ROOT_URLCONF = 'config.urls'

# TODO: Configuración de la base de datos PostgreSQL
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

# TODO: Configuración de GraphQL
GRAPHENE = {"SCHEMA": "config.schema.schema"}

# TODO: Configuración de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # opcional
        'APP_DIRS': True,  # busca templates en cada app
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

# TODO: URL base para archivos estáticos
STATIC_URL = '/static/'
