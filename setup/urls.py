from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acervos/', include('acervos.urls')),
    path('usuarios/', include('usuarios.urls')),
    # Ao acessar http://127.0.0.1:8000/, vai direto para a rota principal do app usuarios
    path('', include('usuarios.urls')),
]