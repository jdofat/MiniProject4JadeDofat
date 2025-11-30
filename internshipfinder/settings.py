#  Django settings
# https://docs.djangoproject.com/en/stable/topics/settings/

#  project structure (where settings.py comes from)
# https://docs.djangoproject.com/en/stable/intro/tutorial01/#creating-a-project

#  INSTALLED_APPS 
# https://docs.djangoproject.com/en/stable/ref/settings/#installed-apps

#  MIDDLEWARE documentation
# https://docs.djangoproject.com/en/stable/ref/middleware/

#  SQLite setup
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

#  TEMPLATES 
# https://docs.djangoproject.com/en/stable/ref/settings/#templates

#  STATIC_URL, STATICFILES_DIRS
# https://docs.djangoproject.com/en/stable/howto/static-files/

# LOGIN_REDIRECT_URL/Auth
# https://docs.djangoproject.com/en/stable/ref/settings/#auth

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dev-secret-key'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'internships',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'internshipfinder.urls'

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

WSGI_APPLICATION = 'internshipfinder.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
