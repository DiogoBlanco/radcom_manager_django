from django.urls import path
from . import views

app_name = 'contratos'

urlpatterns = [
    # URL home
    path('', views.contratos, name='contratos')
]
