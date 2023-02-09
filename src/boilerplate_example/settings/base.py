from pathlib import Path

from decouple import config, Csv
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent.parent

VENV_PATH = BASE_DIR.parent

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

STATICFILES_DIRS = [BASE_DIR / 'static']

STATIC_ROOT = VENV_PATH / 'static_root'
MEDIA_ROOT = VENV_PATH / 'media'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

SECRET_KEY = config('SECRET_KEY')

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'boilerplate_example.apps.core',
    'boilerplate_example.apps.people'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'boilerplate_example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'boilerplate_example.wsgi.application'

LOCALE_PATHS = (
    (BASE_DIR / 'locale'),
)

LANGUAGES = [
    ('es', _('Spanish')),
    ('en', _('English')),
]

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Havana'
USE_I18N = True
USE_TZ = True

AUTH_USER_MODEL = 'people.User'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
