from django.urls import path
from .views import learn_Django, start, all_data
urlpatterns = [
    path('dj/', learn_Django),
    path('start/',start),
    path('all/',all_data, name ='all_data'),
]
