from django.urls import path
from .views import learn_Django, start
urlpatterns = [
    path('dj/', learn_Django),
    path('start/',start)
]
