from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='Cars'),
    path('<int:id>', views.car_detail, name='Car_detail'),
    path('search', views.search, name='Search'),
]
