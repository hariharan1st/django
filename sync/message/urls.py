""" messages urls """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.create, name='index')
]
