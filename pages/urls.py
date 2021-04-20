from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('About', views.about, name='About'),
    path('Services', views.services, name='Services'),
    path('Contact', views.contact, name='Contact'),

]
