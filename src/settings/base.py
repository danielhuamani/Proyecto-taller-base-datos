"""
Django settings for demo project.
"""
from os.path import dirname, join, realpath
from unipath import Path
from util import get_env

BASE_DIR = Path(__file__).ancestor(2)
ENV = get_env(BASE_DIR)

DEBUG = True
SECRET_KEY = 'my-dev-secret-key'
AUTH_SECRET_KEY = 'my-auth-secret-key'
# CONN_MAX_AGE = 5 * 60  # 5 minutos
# TOS_AUTH_SALT = 'demo'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'XE',
        'USER': 'danielhuamani',
        'PASSWORD': 'danielhuamani',
        'HOST': 'localhost',
        'PORT': '1521',
    }
}
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local apps

    # # 'apps.usuarios',
    'apps.sistema',
    'apps.idioma',
    'apps.alumno_profesor',
    'apps.programacion',
    # 'apps.miembros',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (BASE_DIR.child('templates'),),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request'
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'apps.sistema.backend.AuthBackend',
)

# Internationalization

LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static and Media files
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
)

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'
