from django.urls import path
from . import views
app_name = 'anotacoes'

urlpatterns = [
    path('', views.annotations, name='anotacoes'),
    path('adicionar/', views.add_annotation, name='add_anotacao'),
    path('<int:annotation_id>/editar',
         views.edit_annotation, name='edit_anotacao'),
    path('<int:annotation_id>/apagar',
         views.delete_annotation, name='apagar_anotacao')
]
