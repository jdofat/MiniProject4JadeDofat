# https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Django URL dispatcher docs^

# https://docs.djangoproject.com/en/6.0/intro/tutorial01/
# Django “Writing your first app” tutorial (urls.py setup)^ 

# https://docs.djangoproject.com/en/4.0/ref/urls/
# Reference for django.urls.path() and include() ^ 

# https://www.geeksforgeeks.org/django-url-patterns-python/        
# GeeksforGeeks overview of Django URLConf / urlpatterns ^


# https://www.w3schools.com/django/django_urls.php                 
# W3Schools Django tutorial for setting up urls.py ^


# https://django-tutorial.dev/course/django-for-beginners/project-structure/urlspy/
# Third-party tutorial on Django project URL structure  ^


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('internships.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
