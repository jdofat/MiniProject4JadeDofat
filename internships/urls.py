# django urls and path: https://docs.djangoproject.com/en/5.2/topics/http/urls/
# url converters (like int:pk): https://docs.djangoproject.com/en/5.2/topics/http/urls/#path-converters
# views in urls: https://docs.djangoproject.com/en/5.2/intro/tutorial03/#writing-more-views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("search/", views.search, name="search")
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('saved/', views.saved, name='saved'),
]
