from django.urls import path
from . import views

app_name = 'atendimentos'

urlpatterns = [
    path('', views.services, name='atendimentos')
]
