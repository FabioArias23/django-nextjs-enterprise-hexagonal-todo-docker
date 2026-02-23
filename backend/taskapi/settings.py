import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: En producción esto debe venir de una variable de entorno
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-+$$2mqp^8+$(z3s&+#(_fhy7qjev1x7w^afeedjnou5_^)lsz5')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# ✅ ALLOWED HOSTS: Incluimos el nombre del servicio de Docker y localhost
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'django-backend', '0.0.0.0']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'tasks',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # ✅ Siempre primero
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'taskapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'taskapi.wsgi.application'

# 🧠 LÓGICA DE DETECCIÓN DE ENTORNO (SENIOR)
# Si ejecutamos en Windows local, el host será 'localhost'. 
# Si ejecutamos en Docker, docker-compose inyectará la variable 'DATABASE_HOST' como 'db'.
DB_HOST = os.environ.get('DATABASE_HOST', 'localhost')

# Si el host es localhost (Windows), debemos apuntar al puerto mapeado 5499.
# Si el host es 'db' (Docker), usamos el puerto interno 5432.
DB_PORT = os.environ.get('DATABASE_PORT', '5499' if DB_HOST == 'localhost' else '5432')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'task_manager_db'),
        'USER': os.environ.get('DATABASE_USER', 'postgres_user'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'postgres_password'),
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

# ✅ CONFIGURACIÓN REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # Para la demo, usamos AllowAny para que se vean las tareas sin Auth0 aún.
        'rest_framework.permissions.AllowAny', 
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ CORS: Muy importante para que React conecte
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
CORS_ALLOW_ALL_ORIGINS = True # Úsalo solo en desarrollo si el anterior falla