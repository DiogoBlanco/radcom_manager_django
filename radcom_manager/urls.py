from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contratos.urls')),
    path('clientes/', include('clientes.urls')),
    path('atendimentos/', include('atendimentos.urls')),
    path('anotacoes/', include('anotacoes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
