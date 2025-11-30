# Django manage.py : https://docs.djangoproject.com/en/5.2/ref/django-admin/
# execute_from_command_line Reference: https://docs.djangoproject.com/en/5.2/ref/django-admin/#django.core.management.execute_from_command_line
# DJANGO_SETTINGS_MODULE Environment Variable: https://docs.djangoproject.com/en/5.2/topics/settings/#envvar-DJANGO_SETTINGS_MODULE
# Understanding sys.argv in Python : https://docs.python.org/3/library/sys.html#sys.argv
# Python os module documentation: https://docs.python.org/3/library/os.html


import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internshipfinder.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
