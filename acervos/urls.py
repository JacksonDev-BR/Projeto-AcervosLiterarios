from django.urls import path
from acervos.views import index 

urlpatterns = [
    path('', index),
]