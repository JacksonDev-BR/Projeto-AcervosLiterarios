from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('acervos/nova/', views.dasshboard, name='dasshboard')
]