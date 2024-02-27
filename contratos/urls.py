from django.urls import path
from . import views

app_name = 'contratos'

urlpatterns = [
    # URL home
    path('', views.contratos, name='contratos'),
    path('adicionar/', views.add_contract, name='add_contrato'),
    path('<int:contract_id>/editar', views.edit_contract, name='edit_contrato'),
    path('/<int:contract_id>/apagar',
         views.delete_contract, name='apagar_contrato')
]
