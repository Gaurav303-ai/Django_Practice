from django.urls import path
from .views import django, python

urlpatterns = [
    path('dy/',django),
    path('py/',python)
]