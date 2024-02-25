from django.urls import path
from . import views

app_name = 'atendimentos'

urlpatterns = [
    path('', views.services, name='atendimentos'),
    path('adicionar/', views.add_service, name='add_atendimento'),
    path('<int:service_id>/editar', views.edit_service, name='edit_atendimento'),
    path('<int:service_id>/apagar',
         views.delete_service, name='apagar_atendimento')

]
