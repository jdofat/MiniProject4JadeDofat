#  Django settings
# https://docs.djangoproject.com/en/stable/topics/settings/

#  project structure (where settings.py comes from)
# https://docs.djangoproject.com/en/stable/intro/tutorial01/#creating-a-project

#  SQLite setup
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

#  STATIC_URL, STATICFILES_DIRS
# https://docs.djangoproject.com/en/stable/howto/static-files/

# LOGIN_REDIRECT_URL/Auth
# https://docs.djangoproject.com/en/stable/ref/settings/#auth

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# https://docs.djangoproject.com/en/5.2/ref/settings/
# so django will show detailed error pages:

SECRET_KEY = 'dev-secret-key'

DEBUG = True

ALLOWED_HOSTS = []

#  INSTALLED_APPS : which apps the project is using
# https://docs.djangoproject.com/en/stable/ref/settings/#installed-apps

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'internships',
]

#  MIDDLEWARE for request/response processing
# https://docs.djangoproject.com/en/stable/ref/middleware/

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'internshipfinder.urls'

#  TEMPLATES: for connecting data & page rendering-- presentation of my site
# https://docs.djangoproject.com/en/stable/ref/settings/#templates

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


# https://www.reddit.com/r/learnpython/comments/1dboq9h/i_am_not_able_to_understand_what_is_wsgi_and_why/
# handle HTTP requests to give backend a framwork in a format it can process
WSGI_APPLICATION = 'internshipfinder.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# password rules, language and time zone
# https://docs.allauth.org/en/dev/account/configuration.html
# https://www.loopwerk.io/articles/2025/django-i18n-date-formats/

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

# allows database tables to handle more records
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
