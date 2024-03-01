from django.urls import path
from . import views

app_name = 'arquivos'

urlpatterns = [
    path('', views.index, name='arquivos'),
    path('adicionar/', views.add_files, name='add_arquivos'),

]
