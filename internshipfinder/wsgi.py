# Django WSGI Overview: https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
# get_wsgi_application Reference: https://docs.djangoproject.com/en/5.2/ref/applications/#django.core.wsgi.get_wsgi_application
# Environment Variables in Django: https://docs.djangoproject.com/en/5.2/topics/settings/#envvar-DJANGO_SETTINGS_MODULE
# Django Deployment Guide: https://docs.djangoproject.com/en/5.2/howto/deployment/
# WSGI vs ASGI Explanation: https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/


import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internshipfinder.settings")
application = get_wsgi_application()
