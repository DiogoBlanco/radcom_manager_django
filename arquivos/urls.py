from django.urls import path
from . import views

app_name = 'arquivos'

urlpatterns = [
    path('', views.file, name='arquivos'),
    path('adicionar/', views.add_file, name='add_arquivo'),
    path('<int:file_id>/editar', views.edit_file, name='edit_arquivo'),
]
