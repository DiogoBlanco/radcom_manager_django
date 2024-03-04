from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('app/admin/', admin.site.urls),
    path('app/', include('clientes.urls')),
    path('app/contratos/', include('contratos.urls')),
    path('app/atendimentos/', include('atendimentos.urls')),
    path('app/anotacoes/', include('anotacoes.urls')),
    path('app/arquivos/', include('arquivos.urls')),
    path('app/auth/', include('authentication.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
