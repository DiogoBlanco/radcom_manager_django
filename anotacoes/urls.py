from django.urls import path
from . import views
app_name = 'anotacoes'

urlpatterns = [
    path('', views.annotations, name='anotacoes')
]
