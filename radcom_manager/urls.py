from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contratos.urls')),
    path('clientes/', include('clientes.urls')),
    path('atendimentos/', include('atendimentos.urls')),
    path('anotacoes/', include('anotacoes.urls')),
]
