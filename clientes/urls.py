from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.customers, name='clientes'),
    path('adicionar/', views.add_customer, name='add_cliente'),
    path('<int:customer_id>/editar', views.edit_customer, name='edit_cliente'),
    path('<int:customer_id>/detalhes', views.customer_detail, name='detalhes'),
    path('<int:customer_id>/apagar',
         views.delete_customer, name='apagar_cliente'),
]
