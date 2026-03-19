from django.urls import path
from .views import learn_Django
urlpatterns = [
    path('dj/', learn_Django),
   
]
