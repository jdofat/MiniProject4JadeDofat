# Django WSGI : https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
# get_wsgi_application : https://docs.djangoproject.com/en/5.2/ref/applications/#django.core.wsgi.get_wsgi_application
# venv in dj : https://docs.djangoproject.com/en/5.2/topics/settings/#envvar-DJANGO_SETTINGS_MODULE
# django deployment : https://docs.djangoproject.com/en/5.2/howto/deployment/
# WSGI ? : https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/


import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internshipfinder.settings")
application = get_wsgi_application()

# this should set up django so the app can run on a server

# tells serv which settings file to use
# uses internshipfinder.settings

# WSGI
