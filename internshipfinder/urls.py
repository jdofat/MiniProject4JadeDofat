# https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Django URLs^

# https://docs.djangoproject.com/en/6.0/intro/tutorial01/
# urls.py setup^ 

# https://docs.djangoproject.com/en/4.0/ref/urls/
# django.urls.path() and include() ^ 

# https://www.geeksforgeeks.org/django-url-patterns-python/        
# URLConf/urlpatterns ^


# https://www.w3schools.com/django/django_urls.php                 
# help with urls.py^


# https://django-tutorial.dev/course/django-for-beginners/project-structure/urlspy/
# URL structure  ^


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('internships.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

# this connect different parts of the project to the main URL system
# connects /admin/ to admin site
# sends root pages to main internships app
# uses django login/logout/password URLs --> /accounts/
