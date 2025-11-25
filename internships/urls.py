from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('saved/', views.saved, name='saved'),
]
