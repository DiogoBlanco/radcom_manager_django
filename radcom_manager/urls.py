from django.conf import settings
from django.contrib import admin, auth
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('clientes.urls')),
    path('contratos/', include('contratos.urls')),
    path('atendimentos/', include('atendimentos.urls')),
    path('anotacoes/', include('anotacoes.urls')),
    path('arquivos/', include('arquivos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
